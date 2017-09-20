/**
 * D3 horizontal bar chart
 *
 * This version derived from original downloaded from
 * Bar Chart IIc http://bl.ocks.org/mbostock/7341714#index.html
 * on 04/08/2016.
 *
 * Copyright (C) 2016, Mike Bostock
 * Changes Copyright (C) 2016-2017, The University of Edinburgh and
 * The University of Southampton.
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
 * .chart rect - bar colour.
 * .chart text - bar label colour.
 */

/**
 * Draws horizontal bar chart.
 *
 * @param {string} data_file - file with comma-separated values
 * (CSV).
 * @param {string} id_tag - ID of HTML tag in which the bar chart is
 * drawn.
 * @param {string} label_column - bar chart will have one Y axis bar for
 * each unique value in this column.
 * @param {string} value_column - bar chart will have one Y axis bar for
 * each unique value in this column. Value determines size of bar.
 * @param {integer} area_width - drawing area width.
 */
function draw_bar_horiz(data_file,
                        id_tag,
                        label_column,
                        value_column,
                        area_width) {

    // Changes from original code:
    // Code in function so can draw multiple charts on same page.

    // Changes from original code:
    // Moved type within draw_chart so can draw multiple charts
    // on same page.
    // Replaced d.value with d[value_column] to allow data column
    // to be configured via function argument, so can use different
    // data sets.
    function type(d) {
        d[value_column] = +d[value_column];
        return d;
    }

    // Changes from original code:
    // 420 replaced with area_width and 500 so can configure drawing
    // area size.
    var width = area_width;
    var barHeight = 20;

    // Changes from original code:
    // Width of bar area decremented by 200 to allow space for labels
    // after bars.
    var x = d3.scaleLinear()
        .range([0, width - 200]);

    // Changes from original code:
    // Original replaced hard-coded "body" tag. Updated to specify
    // tag to replace via its ID, provided as function argument,
    // so can draw multiple charts on same page.
    var id_tag_link = "#" + id_tag;
    var chart = d3.select(id_tag_link)
        .attr("width", width);

    // Changes from original code:
    // Replaced d3.tsv with d3.csv.
    d3.csv(data_file, type, function(error, data) {
        // Changes from original code:
        // Added error handler.
        if (error) {
            throw error;
        }

        x.domain([0, d3.max(data, function(d) { return d[value_column]; })]);

        chart.attr("height", barHeight * data.length);

        var bar = chart.selectAll("g")
            .data(data)
            .enter().append("g")
            .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; });

        bar.append("rect")
            .attr("width", function(d) { return x(d[value_column]); })
            .attr("height", barHeight - 1);

        // Changes from original code:
        // Replaced d.value with d[label_column] to allow data column
        // to be configured via function argument, so can use different
        // data sets, and to label bar with label and not value.
        // x function adds 3 so label is drawn after end of column.
        bar.append("text")
            .attr("x", function(d) { return x(d[value_column]) + 3; })
            .attr("y", barHeight / 2)
            .attr("dy", ".35em")
            .text(function(d) { return d[label_column] + " (" + d[value_column] + ")"; });
    });
};
