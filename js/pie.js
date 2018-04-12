/**
 * D3 pie chart
 *
 * This version derived from original downloaded from
 * Pie Chart
 * https://bl.ocks.org/mbostock/3887235#index.html
 * on 05/08/2016.
 *
 * Changes: Wrapped code within a function; replaced hard-coded
 * file name, column names, labels with arguments passed in via
 * function call.
 *
 * Uses styles: text, .arc path, .legend rect .legend text
 *
 * Copyright (c) 2016, Mike Bostock
 * Changes Copyright (c) 2016-2018, The University of Edinburgh.
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
 * Draws pie chart.
 *
 * @param {string} data_file - file with comma-separated values
 * (CSV).
 * @param {string} id_tag - ID of HTML tag in which the bar chart is
 * drawn.
 * @param {string} label_column - pie chart will have one wedge for
 * each unique value in this column.
 * @param {string} value_column - bar chart will have one wedge for
 * each unique value in this column. Value determines size of wedge.
 * @param {integer} width - drawing area width.
 * @param {integer} height - drawing area height.
 * @param {string} colourScheme - comma-separated string of colour names. These are used to determine wedge colours. The number of colours must match the number of categories in label_column, which are assumed to be unique.
 */
function draw_pie(data_file,
                  id_tag,
                  label_column,
                  value_column,
                  width,
                  height,
                  colourScheme = null)
{
    var colours = colourScheme.split(",");

    function type(d) {
        d[value_column] = +d[value_column];
        return d;
    }

    var radius = Math.min(width, height) / 2;

    var arc = d3.arc()
        .outerRadius(radius - 10)
        .innerRadius(0);

    var labelArc = d3.arc()
        .outerRadius(radius - 40)
        .innerRadius(radius - 40);

    var pie = d3.pie()
        .sort(null)
        .value(function(d) { return d[value_column]; });

    var id_tag_link = "#" + id_tag;
    var svg = d3.select(id_tag_link).append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

    d3.csv(data_file, type, function(error, data) {
        if (error) throw error;

        var g = svg.selectAll(".arc")
            .data(pie(data))
            .enter().append("g")
            .attr("class", "arc");

        g.append("path")
            .attr("d", arc)
            .style("fill", function(d) {
                var colour = null;

                // d.index corresponds to row index.
                // data[d.index] == d.data.
                // d corresponds to row.
                colour = colours[d.index];
                return colour;
              }
        );

        g.append("text")
            .attr("transform", function(d) {
               return "translate(" + labelArc.centroid(d) + ")";
            })
            .attr("dy", ".35em")
            .text(function(d) {
                return d.data[label_column] +
                    "\n(" + d.data[value_column] + ")";
            });
    });
};
