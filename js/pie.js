/**
 * D3 pie chart
 *
 * This version derived from original downloaded from
 * https://bl.ocks.org/mbostock/3887235#index.html on 02/03/2016.
 *
 * Copyright (C) 2016, Mike Bostock
 * Changes Copyright (C) 2016, The University of Edinburgh.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Requires styles for:
 *
 * .arc text - pie chart labels.
 * .arc path - pie chart wedge dividers.
 */

/**
 * Callback function called for each row in turn, to calculate totals
 * which determine the size of each wedge.
 *
 * @callback pieCallback
 * @param {string[]} row - single row of data.
 * @return {number} value - value derived from row.
 */

/** 
 * Draws pie chart.
 *
 * @param {string} data_file - file with comma-separated values
 * (CSV). 
 * @param {string} id_tag - ID of HTML tag in which the pie chart is
 * drawn. 
 * @param {string} wedge_column - pie chart will have one wedge for
 * each unique value in this column. 
 * @param {pieCallback} aggregate - callback function called to
 * get value for a row which is used to calculate the totals for each
 * unique  wedge_column value, and determines the size of the wedges.
 * @param {Object[]} colour_bins - colours for wedge. 
 * @param {integer} colour_bins[].bound - if the total calculated for
 * a wedge_column value is less than or equal to this value then the
 * corresponding fill colour is used to colour the wedge.
 * @param {string} colour_bins[].fill - a colour code (e.g. "#e0e2fe").
 * @param {integer} area_width - drawing area width. 
 * @param {integer} area_height - drawing area height. 
 */
function draw_pie(data_file, 
                  id_tag, 
                  wedge_column, 
                  aggregate, 
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
        // value returned by aggregate for each row.
        var categories = {};
        raw_data.forEach(function(row) {
            if (!categories[row[wedge_column]]) {
                categories[row[wedge_column]] = 0;
            }
            categories[row[wedge_column]] += parseFloat(aggregate(row));
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
                value = parseFloat(value);
                if (value <= colour_bins[k].bound)
                {
                    return colour_bins[k].fill;
                }
            }
            return colour_bins[colour_bins.length - 1].fill;
        };
    });
};
