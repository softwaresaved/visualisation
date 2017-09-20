/**
 * D3 pie chart
 *
 * This version derived from original downloaded from
 * Pie Chart https://bl.ocks.org/mbostock/3887235#index.html
 * on 05/08/2016.
 *
 * Copyright (C) 2016, Mike Bostock
 * Changes Copyright (C) 2016-2017, The University of Edinburgh.
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

/** Fill colours for pie chart wedges. */
var fill_colour = [
    "#f9fc99",
    "#fce19f",
    "#ffaf47",
    "#ff8747",
    "#ff6547",
    "#ff4747",
    "#ffa3c9",
    "#f8a3ff",
    "#bba3ff",
    "#a3dbff",
    "#a3ffbb"];
// Changes from original code:
// Replaced hard-coded colours array with fill_colour.

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
 * @param {integer[]} bound - upper-bounds for values to be placed
 * in a wedge. If a value_column value is less than or equal to
 * bound[N] then fill_colour[N % (fill_colour.length - 2)] is used
 * to colour the corresponding wedge.
 * bound.length must be <= fill_colour.length.
 * @param {integer} width - drawing area width.
 * @param {integer} height - drawing area height.
 */
function draw_pie(data_file,
                  id_tag,
                  label_column,
                  value_column,
                  width,
                  height,
                  bound) {

    // Changes from original code:
    // Code in function so can draw multiple charts on same page.
    // Hard-coded width and height replaced with parameters
    // so can configure drawing area size.
    // Replaced hard-coded colours array with bound to allow
    // future refactoring for configurable colours.

    // Changes from original code:
    // Moved type within draw_chart so can draw multiple charts
    // on same page.
    // Replaced d.population with d[value_column] to allow data column
    // to be configured via function argument, so can use different
    // data sets.
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

    // Changes from original code:
    // Original replaced hard-coded "body" tag. Updated to specify
    // tag to replace via its ID, provided as function argument,
    // so can draw multiple charts on same page.
    var id_tag_link = "#" + id_tag;
    var svg = d3.select(id_tag_link).append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

    // Changes from original code:
    // Replaced d3.tsv with d3.csv.
    d3.csv(data_file, type, function(error, data) {
        if (error) throw error;

        var g = svg.selectAll(".arc")
            .data(pie(data))
            .enter().append("g")
            .attr("class", "arc");

        // Changes from original code:
        // Replaced hard-coded colours array with colour_bins parameter
        // so can configure pie chart colours.
        g.append("path")
            .attr("d", arc)
            .style("fill", function(d) { return get_slice_colour(d.data[value_column]); });

        // Changes from original code:
        // Replaced d.data.age with d.data[value_column] to allow data column
        // to be configured via function argument, so can use different
        // data sets.
        g.append("text")
            .attr("transform", function(d) {
                return "translate(" + labelArc.centroid(d) + ")";
            })
            .attr("dy", ".35em")
            .text(function(d) { return d.data[label_column]; });

        // Changes from original code:
        // Added function to return colour bin values.
        function get_slice_colour(value) {
            for (var k = 0; k < bound.length; k++) {
                value  = parseFloat(value);
                if (value <= parseFloat(bound[k]))
                {
                    return fill_colour[k % (fill_colour.length - 2)];
                }
            }
            return fill_colour[fill_colour.length - 1];
        };
    });
};
