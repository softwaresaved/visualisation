/**
 * D3 bar chart
 *
 * This version derived from original downloaded from
 * Bar Chart https://bl.ocks.org/mbostock/3885304#index.html 
 * on 05/08/2016.
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
 * @param {string} label_column - bar chart will have one X axis bar for
 * each unique value in this column.
 * @param {string} value_column - bar chart will have one X axis bar for
 * each unique value in this column. Value determines size of bar.
 * @param {integer} area_width - drawing area width.
 * @param {integer} area_height - drawing area height.
 */
function draw_chart(data_file, 
                    id_tag, 
                    label_column, 
                    value_column, 
                    area_width,
                    area_height) {

    // Changes from original code:
    // Code in function so can draw multiple charts on same page.

    // Changes from original code:
    // Moved type within draw_chart so can draw multiple charts
    // on same page.
    // Replaced d.frequency with d[value_column] to allow data column
    // to be configured via function argument, so can use different
    // data sets.
    function type(d) {
        d[value_column] = +d[value_column];
        return d;
    }

    // Changes from original code:
    // bottom: 30 updated to allow more space for labels.
    // 960 replaced with area_width and 500 replaced with area_height
    // so can configure drawing area size.
    var margin = {top: 20, right: 20, bottom: 100, left: 40},
    width = area_width - margin.left - margin.right,
    height = area_height - margin.top - margin.bottom;

    var x = d3.scale.ordinal()
        .rangeRoundBands([0, width], .1);

    var y = d3.scale.linear()
        .range([height, 0]);

    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom");

    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left")
        .tickSize(1,5);

    // Changes from original code:
    // Original replaced hard-coded "body" tag. Updated to specify
    // tag to replace via its ID, provided as function argument,
    // so can draw multiple charts on same page.
    var id_tag_link = "#" + id_tag;
    var svg = d3.select(id_tag_link).append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // Changes from original code:
    // Replaced d3.tsv with d3.csv.
    d3.csv(data_file, type, function(error, data) {
        if (error) throw error;

	// Changes from original code:
	// Replaced d.letter with d[label_column] to allow data column
	// to be configured via function argument, so can use different
	// data sets.
        x.domain(data.map(function(d) { return d[label_column]; }));
        y.domain([0, d3.max(data, function(d) { return d[value_column]; })]);
        
	svg.append("g")
	    .attr("class", "x axis")
	    .attr("transform", "translate(0," + height + ")")
	    .call(xAxis)
	    // Changes from original code:
	    // Draw axis labels vertically so they don't overrite siblings.
            .selectAll("text")
            .attr("y", 0)
            .attr("x", -9)
            .attr("transform", "rotate(-90)")
            .style("text-anchor", "end");

	// Changes from original code:
	// Replaced "Frequency" with label_column, so can use different
	// data sets.
	svg.append("g")
	    .attr("class", "y axis")
	    .call(yAxis)
	    .append("text")
	    .attr("transform", "rotate(-90)")
	    .attr("y", 6)
	    .attr("dy", ".71em")
	    .style("text-anchor", "end")
	    .text(value_column);
	
	svg.selectAll(".bar")
	    .data(data)
	    .enter().append("rect")
	    .attr("class", "bar")
	    .attr("x", function(d) { return x(d[label_column]); })
	    .attr("width", x.rangeBand())
	    .attr("y", function(d) { return y(d[value_column]); })
	    .attr("height", function(d) { return height - y(d[value_column]); });
    });
};
