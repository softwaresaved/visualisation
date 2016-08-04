/**
 * D3 bar chart
 *
 * This version derived from original downloaded from
 * https://bl.ocks.org/mbostock/3885304#index.html on 02/03/2016.
 *
 * Copyright (C) 2016, Mike Bostock
 * Changes Copyright (C) 2016, The University of Edinburgh and 
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
 * .bar text - bar labels.
 * .bar:hover - bar mouse over colour.
 * .axis - axis label.
 * .axis path - axis lines.
 * .axis line - axis lines.
 * .x.axis path - X-axis lines.
 */

/**
 * Draws bar chart.
 *
 * @param {string} data_file - file with comma-separated values
 * (CSV).
 * @param {string} id_tag - ID of HTML tag in which the bar chart is
 * drawn. 
 * @param {string} bar_column - bar chart will have one X axis bar for
 * each unique value in this column.
 * @param {integer} area_width - drawing area width.
 * @param {integer} area_height - drawing area height.
 */
function draw_chart(data_file, 
                    id_tag, 
		    bar_label_column,
                    bar_column, 
                    area_width,
                    area_height) {

    function type(d) {
        return d;
    }

    var barHeight = 20; // TODO auto-calculate

    var id_tag_link = "#" + id_tag;

    var margin = {top: 20, right: 20, bottom: 100, left: 40},
    width = area_width - margin.left - margin.right,
    height = area_height - margin.top - margin.bottom;

    var x = d3.scale.linear()
        .range([0, width - 200]); // - 200 space for label TODO clean

    var chart = d3.select(id_tag_link)
        .attr("width", width + margin.left + margin.right);

    d3.csv(data_file, type, function(error, data) {
        if (error) {
            throw error;
        }        
	var max = d3.max(data, function(d) { 
	    return +d[bar_column]; });
	// + above casts to numeric value
	console.log("Max: " + max);
        x.domain([0, max]);

	chart.attr("height", barHeight * data.length);

	var bar = chart.selectAll("g")
	    .data(data)
	    .enter().append("g")
	    .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; });

	bar.append("rect")
	    .attr("width", function(d) { return x(d[bar_column]); })
	    .attr("height", barHeight - 1);

	bar.append("text")
	    .attr("x", function(d) { 
		return x(d[bar_column]) + 3; 
	    })
	    .attr("y", barHeight / 2)
	    .attr("dy", ".35em")
	    .text(function(d) { 
		return d[bar_label_column]; });
    });
};
