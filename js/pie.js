/*
 * D3 pie chart
 *
 * https://bl.ocks.org/mbostock/3887235
 * Copyright 2016, Mike Bostock
 * Licence: GNU General Public License, version 3,
 * https://opensource.org/licenses/GPL-3.0
 * Derived from https://bl.ocks.org/mbostock/3887235#index.html downloaded on 02/03/2016.
 *
 * Requires styles for:
 *
 * .arc text - pie chart labels.
 * .arc path - pie chart wedge dividers.
 */

/** 
 * Draws pie chart. 
 *
 * @param {string} data_file - file with comma-separated values
 * (CSV). 
 * @param {string} id_tag - ID of HTML tag in which the pie chart is
 * drawn. 
 * @param {string} wedge_column - ppie chart will have one wedge for
 * each uniquue value in this column. 
 * @param {function} aggregate - callback function called for each row
 * in turn. It is expected to return an integer or float. The function
 * is used to calculate the totals for each unique bar_column value,
 * and determines the size of the wedges.

 * - colour_bins - ordered list of dictionaries each with a numerical
 *   "bound" value and a "fill" colour. 

 * @param {integer} width - drawing area width. 
 * @param {integer} height - drawing area height. 
 */
function draw_pie(data_file, 
                  id_tag, 
                  wedge_column, 
                  pie_count, 
                  colour_bins,
                  area_width,
                  area_height) {

    function type(d) {
        return d;
    };

    d3.csv(data_file, type, function(error, raw_data) {
        if (error) {
            throw error;
        }

        console.log("Pie chart location tag: " + id_tag);
        console.log("Number of rows: " + raw_data.length);
        var id_tag_link = "#" + id_tag;

        var radius = Math.min(area_width, area_height) / 2;

        var arc = d3.svg.arc()
            .outerRadius(radius - 10)
            .innerRadius(0);

        var labelArc = d3.svg.arc()
            .outerRadius(radius - 40)
            .innerRadius(radius - 40);

        var pie = d3.layout.pie()
            .sort(null)
            .value(function(d) { return d.value; });

        var svg = d3.select(id_tag_link).append("svg")
            .attr("width", area_width)
            .attr("height", area_height)
            .append("g")
            .attr("transform", "translate(" + area_width / 2 + "," + area_height / 2 + ")");

        // Iterate through raw_data. For each distinct value in
        // wedge_column, compute a value based upon the
        // value returned by pie_count for each row.
        var categories = {};
        raw_data.forEach(function(row) {
            if (!categories[row[wedge_column]]) {
                categories[row[wedge_column]] = 0;
            }
            categories[row[wedge_column]] += parseFloat(pie_count(row));
        });
        // Create 2 column data with distinct category values
        // and the values computed above.
        var data = [];
        Object.keys(categories).forEach(function(key) {
            data.push({
                category: key,
                value: categories[key]
            });
        });
        
        var g = svg.selectAll(".arc")
            .data(pie(data))
            .enter().append("g")
            .attr("class", "arc");

        g.append("path")
            .attr("d", arc)
            .style("fill", function(d) { 
                return get_slice_colour(d.data.value); 
            });

        g.append("text")
            .attr("transform", function(d) { 
                return "translate(" + labelArc.centroid(d) + ")"; 
            })
            .attr("dy", ".35em")
            .text(function(d) { return d.data.category; });


        function get_slice_colour(value) {
            for (var k = 0; k < colour_bins.length; k++) {
                value = parseInt(value);
                if (value <= colour_bins[k].bound)
                {
                    return colour_bins[k].fill;
                }
            }
            return colour_bins[colour_bins.length - 1].fill;
        };
    });
};
