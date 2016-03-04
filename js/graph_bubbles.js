/**
 * Graph bubbles.
 *
 * https://github.com/aturner-epcc/usage-visualisation
 * Copyright 2015, The University of Edinburgh.
 * Licence: GNU General Public License, version 2.
 * Derived from prototypes/codes-force-bubbles/code_usage.html, https://github.com/aturner-epcc/usage-visualisation/commit/b5749bb711045246abc3edeec4e98b18a28d2c53).
 */

function draw_bubbles(data_file,
                      id_tag,
                      columns,
                      name_column,
                      radius_column,
                      radius_threshold,
                      colour_column,
                      colour_bins,
                      legend_label,
                      assign_colour_bin,
                      bubble_caption) {

    // Load the data and set up the visualisation
    d3.csv(data_file, function (error, data) {

        if (error) {
            throw error;
        }
        console.log("Graph bubbles location tag: " + id_tag);
        var id_tag_link = "#" + id_tag;

        // Get the maximum scale for the data using radius_column
        var max_scale = d3.max(data, function (d) { return parseFloat(d[radius_column]); } );
        // Map the range of values to a custom scale to produce nice radii
        var radius_scale = d3.scale.pow().exponent(0.5).domain([0, max_scale]).range([1,40]);

        // Define the size of the chart box
        var width = 700, height = 700;

        // Get colours from colour_bins and reverse order for drawing custom
        // colour scale
        var colours = [];
        for (var j = 0; j < colour_bins.length; j++) {
            colours[colour_bins.length - j - 1] = colour_bins[j].fill;
        }
        // Define a custom colour scale
        var fill = d3.scale.ordinal().range(colours);

        // Setup the SVG area
        var svg = d3.select(id_tag_link).append("svg")
            .attr("class", "vis")
            .attr("width", width)
            .attr("height", height);

        // Loop over data setting radii and centres
        for (var j = 0; j < data.length; j++) {
            var data_radius = parseFloat(data[j][radius_column]);
            if (data_radius < radius_threshold) {
                // If we have very low value cull from the data
                console.log("Culling " + data[j][name_column] + " as " +
                            radius_column + " " + data_radius +
                            " < threshold " + radius_threshold);
                data.splice(j, 1);
                // Indexing has chaged, make sure we don't miss any elements
                j--;
            } else if (isNaN(data_radius)) {
                // If we have very low value cull from the data
                console.log("Culling " + data[j][name_column] + " as " +
                            radius_column + " is " + data_radius);
                data.splice(j, 1);
                // Indexing has chaged, make sure we don't miss any elements
                j--;
            } else {
                // Get radius from custom mapped range we defined
                data[j].radius = radius_scale(data_radius);
                data[j].x = Math.random() * width;
                data[j].y = Math.random() * height;
                // Use colour_column to get bubble fill colour from colour_bins
                for (var k = 0; k < colour_bins.length; k++) {
                    if (assign_colour_bin(data[j][colour_column], k)) {
                        data[j].Level = colour_bins[k].fill;
                        break;
                    }
                }
            }
        }
        
        // Set up misc parts, padding for the bubbles and the maximum radius
        var padding = 2;
        var maxRadius = d3.max(_.pluck(data, 'radius'));
        
        // Get the centres of gravity - one for each unique value of
        // the specified property
        var getCenters = function (vname, size) {
            var centers, map;
            // Get unique values of the property
            centers = _.uniq(_.pluck(data, vname)).map(function (d) {
                return {name: d, value: 1};
            });
            
            // Define how the gravity centres are layed out - on a grid
            map = d3.layout.treemap()
                .size(size)
                .ratio(1/1);
            // Push the centres into the layout
            map.nodes({children: centers});
            
            return centers;
        };
        
        // Define the bubbles
        var nodes = svg.selectAll("circle").data(data);
        
        nodes.enter().append("circle")
            .attr("class", "node")
            .attr("cx", function (d) { return d.x; })
            .attr("cy", function (d) { return d.y; })
            .attr("r", function (d) { return d.radius; })
            .attr("data-legend", function (d) { return d[name_column]; })
            .style("fill", function (d) { return d.Level; })
            .style("stroke", "#333")
            .style("stroke-width", "2px")
            .on("mouseover", function (d) { showPopover.call(this, d); })
            .on("mouseout", function (d) { removePopovers(); });
        
        var force = d3.layout.force();
        
        d3.select(".visdesc").style("display", "block");
        d3.select(".btn-group").style("display", "block");
        
        // Setup legend
        var lwidth = width;
        var lheight = 30;
        
        var legRectSize = 18;
        var legSpace = 4;
        
        var lsvg = d3.select(id_tag_link).insert("svg", ".vis")
            .attr("class", "legend-box")
            .attr("width", lwidth)
            .attr("height", lheight);
        
        var legend = lsvg.selectAll(".legend")
            .data(colour_bins)
            .enter()
            .append("g")
            .attr("class", "legend")
            .attr("transform", function (d, i) {
                var h = legRectSize + legSpace;
                var vz = legSpace * 2;
                var hz = width - legRectSize * (i+1);
                return "translate(" + hz + "," + vz + ")";
            });
        
        legend.append("rect")
            .attr("width", legRectSize)
            .attr("height", legRectSize)
            .style("fill",  function (d) { return d3.rgb(d.fill); })
            .style("stroke",  function (d) { d.fill; })
            .on("mouseover", function (d) { showLegPopover.call(this, d); })
            .on("mouseout", function (d) { removePopovers(); });
        
        lsvg.append("text")
            .attr("x", (width - legRectSize*colour_bins.length) - 
                  (legend_label.length * 8))
            .attr("y", legRectSize + legSpace)
            .text(legend_label);
        
        // Draw the initial layout (uncategorised)
        draw();
        
        // Attach the listerners to the buttons
        $( ".btn" ).click(function () {
            draw(columns[this.id].name);
        });
        
        // Overarching function called by clicking on a button -
        // redraw the visualisation
        function draw(varname) {
            var centers = getCenters(varname, [width, height]);
            force.on("tick", tick(centers, varname));
            labels(centers);
            force.start();
        }
        
        // Shift the bubbles to the centres of gravity
        function tick(centers, varname) {
            var foci = {};
            for (var i = 0; i < centers.length; i++) {
                foci[centers[i].name] = centers[i];
            }
            return function (e) {
                for (var i = 0; i < data.length; i++) {
                    var o = data[i];
                    var f = foci[o[varname]];
                    o.y += ((f.y + (f.dy / 2)) - o.y) * e.alpha;
                    o.x += ((f.x + (f.dx / 2)) - o.x) * e.alpha;
                }
                nodes.each(collide(.11))
                    .attr("cx", function (d) { return d.x; })
                    .attr("cy", function (d) { return d.y; });
            }
        }
        
        // If we are showing categorised data, set up the category labels
        function labels(centers) {
            svg.selectAll(".label").remove();
            
            svg.selectAll(".label")
                .data(centers).enter().append("text")
                .attr("class", "label")
                .text(function (d) { return d.name })
                .attr("transform", function (d) {
                    return "translate(" + (d.x + (d.dx / 6)) + ", " + (d.y + 20) + ")";
                })
                .style("fill", "black")
                .style("font-size", "12px");
        }
        
        function removePopovers() {
            $('.popover').each(function () {
                $(this).remove();
            });
        }
        
        // Set up the popup boxes so that we can show more information
        // when you hover over a bubble
        function showPopover(d) {
            $(this).popover({
                placement: 'auto top',
                container: 'body',
                trigger: 'manual',
                html : true,
                content: bubble_caption(d)
            });
            $(this).popover('show');
        }
        
        function showLegPopover(d) {
            $(this).popover({
                placement: 'auto bottom',
                container: 'body',
                trigger: 'manual',
                html : true,
                content: function () {
                    return d.label; }
            });
            $(this).popover('show');
        }
        
        // This function ensures that bubbles do not overlap (it
        // computes the pairwise repulsion). alpha sets the level of
        // repulsion.
        function collide(alpha) {
            var quadtree = d3.geom.quadtree(data);
            return function (d) {
                var r = d.radius + maxRadius + padding,
                nx1 = d.x - r,
                nx2 = d.x + r,
                ny1 = d.y - r,
                ny2 = d.y + r;
                quadtree.visit(function (quad, x1, y1, x2, y2) {
                    if (quad.point && (quad.point !== d)) {
                        var x = d.x - quad.point.x,
                        y = d.y - quad.point.y,
                        l = Math.sqrt(x * x + y * y),
                        r = d.radius + quad.point.radius + padding;
                        if (l < r) {
                            l = (l - r) / l * alpha;
                            d.x -= x *= l;
                            d.y -= y *= l;
                            quad.point.x += x;
                            quad.point.y += y;
                        }
                    }
                    return x1 > nx2 || x2 < nx1 || y1 > ny2 || y2 < ny1;
                });
            };
        }
    });
};
