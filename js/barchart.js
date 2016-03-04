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
 * each uniquue value in this column.
 * @param {function} aggregate - callback function called for each row
 * in turn. It is expected to return an integer or float. The function
 * is used to calculate the totals for each unique bar_column value,
 * and determines the size of the bars on the Y axis.
 * @param {integer} width - drawing area width.
 * @param {integer} height - drawing area height.
 */
function draw_chart(data_file, 
                    id_tag, 
                    bar_column, 
                    aggregate,
                    area_width,
                    area_height) {

    function type(d) {
        return d;
    }

    d3.csv(data_file, type, function(error, raw_data) {
        if (error) {
            throw error;
        }
        
        console.log("Bar chart location tag: " + id_tag);
        console.log("Number of rows: " + raw_data.length);
	var id_tag_link="#" + id_tag;

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

        var svg = d3.select(id_tag_link).append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        // Iterate through raw_data. For each distinct value in
        // bar_column, compute a value based upon the
        // value returned by pie_count for each row.
        var categories = {};
        raw_data.forEach(function(row) {
            if (!categories[row[bar_column]]) {
                categories[row[bar_column]] = 0;
            }
            categories[row[bar_column]] += parseFloat(aggregate(row));
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
        x.domain(data.map(function(d) { return d.category; }));
        y.domain([0, d3.max(data, function(d) { return d.value; })]);
        
        svg.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + height + ")")
            .call(xAxis)
            .selectAll("text")
            .attr("y", 0)
            .attr("x", -9)
            .attr("transform", "rotate(-90)")
            .style("text-anchor", "end");
        
        svg.append("g")
            .attr("class", "y axis")
            .call(yAxis)
            .append("text")
            .attr("transform", "rotate(90)")
            .attr("y", 6);
        
        svg.selectAll(".bar")
            .data(data)
            .enter().append("rect")
            .attr("class", "bar")
            .attr("x", function(d) { return x(d.category); })
            .attr("width", x.rangeBand())
            .attr("y", function(d) { return y(d.value); })
            .attr("height", function(d) { return height - y(d.value); });
        
        svg.selectAll(".bar")
            .data(data)
            .enter().append(".bar")
            .style("width", function(d) { return d.value * 10 + "px"; })
            .text(function(d) { return d.value; });
    });
};
