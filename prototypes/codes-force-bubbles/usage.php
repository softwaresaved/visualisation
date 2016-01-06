    <script>
    var data_file = 'data/d3codes_summary.csv';
    var category_names = ["Overview",
			  "Code Type",
			  "Research Area",
			  "Programming Language",
			  "Licence Type"];
    var categories = ["none",
		      "CodeType",
		      "ResArea",
		      "ProgLang",
		      "LicType"];
     </script>

    <style>
        @import url("css/bootstrap_min.css");
        circle {
          stroke: #333333;
          stroke-width: 2px;
        }
        .label {
          fill: black;
          font-size: 12px;
        }
        #chart {
           display: block;
           padding-left: 20px;
        }
    </style>
    <div class="btn-group" data-toggle="buttons" style="display: none">
      <label class="btn btn-danger" id=0>
        <input type="radio" name="options">
        <script>
	document.write(category_names[0]);
        </script>
      </label>
      <label class="btn btn-danger" id=1>
        <input type="radio" name="options">
        <script>
	document.write(category_names[1]);
        </script>
      </label>
      <label class="btn btn-danger" id=2>
        <input type="radio" name="options">
        <script>
	document.write(category_names[2]);
        </script>
      </label>
      <label class="btn btn-danger" id=3>
        <input type="radio" name="options">
        <script>
	document.write(category_names[3]);
        </script>
      </label>
      <label class="btn btn-danger" id=4>
        <input type="radio" name="options">
        <script>
	document.write(category_names[4]);
        </script>
      </label>
    </div>
    <div id="chart"></div>
    <script src="js/d3.min.js"></script>
    <script src="js/jquery.js"></script>
    <script src="js/bootstrap.js"></script>
    <script src="js/underscore.js"></script>
    <script>
      // Load the data and set up the visualisation
      d3.csv(data_file, function (error, data) {

        // Get the max usage in the data
        var max_usage = d3.max(data, function(d) { return parseInt(d.Usage, 10); } );
        // Map the range of values to a custom scale to produce nice radii
        var radius_scale = d3.scale.pow().exponent(0.5).domain([0, max_usage]).range([2, 50]);

        // Define the size of the chart box
        var width = 700, height = 700;

        var userCat = [
                       { label: "Less than 5 users", count: 5, fill: "#fee5d9" },
                       { label: "5-10 users", count: 10, fill: "#fcbba1" },
                       { label: "10-20 users", count: 20, fill: "#fc9272" },
                       { label: "20-50 users", count: 50, fill: "#fb6a4a" },
                       { label: "50-100 users", count: 100, fill: "#de2d26" },
                       { label: "More than 100 users", count: 5000, fill: "#a50f15" }
        ];

        // Define a custom colour scale
        var fill = d3.scale.ordinal().range([
                                             "#a50f15",
                                             "#de2d26",
                                             "#fb6a4a",
                                             "#fc9272",
                                             "#fcbba1",
                                             "#fee5d9"
                                          ]);
        

        // Setup the SVG area
        var svg = d3.select("#chart").append("svg")
        	.attr("class", "vis")
            .attr("width", width)
            .attr("height", height);

        // Loop over data setting radii and centres 
        for (var j = 0; j < data.length; j++) {
          if (parseInt(data[j].Usage) < 10) {
             // If we have very low usage cull from the data
             console.log("Splicing " + data[j].Code);
             data.splice(j, 1);
             // Indexing has chaged, make sure we don't miss any elements
             j--;
          } else {
             // Get radius from custom mapped range we defined
             data[j].radius = radius_scale(parseInt(data[j].Usage, 10));
             data[j].x = Math.random() * width;
             data[j].y = Math.random() * height;
             // Create category for number of users
             nuser = parseInt(data[j].Users);
             if (nuser < 5) {
                data[j].UserLevel = userCat[0].fill;
             } else if (nuser < 10) {
                data[j].UserLevel = userCat[1].fill;
             } else if (nuser < 20) {
                data[j].UserLevel = userCat[2].fill;
             } else if (nuser < 50) {
                data[j].UserLevel = userCat[3].fill;
             } else if (nuser < 100) {
                data[j].UserLevel = userCat[4].fill;
             } else {
                data[j].UserLevel = userCat[5].fill;
             }
          }
        }

        // Set up misc parts, padding for the bubbles and the maximum radius
        var padding = 2;
        var maxRadius = d3.max(_.pluck(data, 'radius'));

        // Get the centres of gravity - one for each unique value of the specified property
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
        var nodes = svg.selectAll("circle")
          .data(data);

        nodes.enter().append("circle")
          .attr("class", "node")
          .attr("cx", function (d) { return d.x; })
          .attr("cy", function (d) { return d.y; })
          .attr("r", function (d) { return d.radius; })
          .attr("data-legend", function (d) { return d.Code; })
          .style("fill", function (d) { return d.UserLevel; })
          .style("stroke", "#333")
          .style("stroke-width", "2px")
          .on("mouseover", function (d) { showPopover.call(this, d); })
          .on("mouseout", function (d) { removePopovers(); })

        var force = d3.layout.force();

        d3.select(".visdesc")
           .style("display", "block");
        d3.select(".btn-group")
           .style("display", "block");

        // Setup legend
        var lwidth = width;
        var lheight = 30;
  
        var legRectSize = 18;
        var legSpace = 4;

        var lsvg = d3.select("#chart").insert("svg", ".vis")
            .attr("class", "legend-box")
            .attr("width", lwidth)
            .attr("height", lheight);

        var legend = lsvg.selectAll(".legend")
               .data(userCat)
               .enter()
               .append("g")
               .attr("class", "legend")
               .attr("transform", function(d, i) {
                    var h = legRectSize + legSpace;
                    // Hardcoded 6 colour categories for the moment
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
              .on("mouseout", function (d) { removePopovers(); })

        lsvg.append("text")
              .attr("x", width - legRectSize*userCat.length - 115)
              .attr("y", legRectSize + legSpace)
              .text("Number of Users");
        

        // Draw the initial layout (uncategorised)
        draw();

        // Attach the listerners to the buttons
        $( ".btn" ).click(function() {
	    draw(categories[this.id]);
        });

        // Overarching function called by clicking on a button - redraw the
        // visualisation
        function draw (varname) {
          var centers = getCenters(varname, [width, height]);
          force.on("tick", tick(centers, varname));
          labels(centers);
          force.start();
        }

        // Shift the bubbles to the centres of gravity
        function tick (centers, varname) {
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
        function labels (centers) {
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

        function removePopovers () {
          $('.popover').each(function() {
            $(this).remove();
          }); 
        }

        // Set up the popup boxes so that we can show more information when you hover over a bubble
        function showPopover (d) {
          $(this).popover({
            placement: 'auto top',
            container: 'body',
            trigger: 'manual',
            html : true,
            content: function() { 
              return "Name: " + d.Code + "<br/>Usage: " + d.Usage + " node hours<br/>Jobs: " + d.Jobs +
                     "<br/>Usage Rank: " + d.Rank + "<br/>Users: " + d.Users; }
          });
          $(this).popover('show')
        }
        function showLegPopover (d) {
            $(this).popover({
              placement: 'auto bottom',
              container: 'body',
              trigger: 'manual',
              html : true,
              content: function() { 
                return d.label; }
            });
            $(this).popover('show')
          }

        // This function ensures that bubbles do not overlap (it computes the 
        // pairwise repulsion). alpha sets the level of repulsion.
        function collide(alpha) {
          var quadtree = d3.geom.quadtree(data);
          return function (d) {
            var r = d.radius + maxRadius + padding,
                nx1 = d.x - r,
                nx2 = d.x + r,
                ny1 = d.y - r,
                ny2 = d.y + r;
            quadtree.visit(function(quad, x1, y1, x2, y2) {
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
    </script>
