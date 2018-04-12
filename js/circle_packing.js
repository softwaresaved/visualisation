/**
 * D3 circle packing
 *
 * This version derived from original downloaded from
 * Circle-Packing II
 * http://bl.ocks.org/mbostock/07ec62d9957a29a30e71cad962ff2efd
 * on 10/08/2016.
 *
 * Uses styles: text, .node circle, .node:hover circle
 *
 * Changes: Wrapped code within a function; replaced hard-coded
 * file name, column names, labels with arguments passed in via
 * function call; inserts <svg> element instead of assuming one has
 * been defined in HTML.
 *
 * Copyright (c) 2016, Mike Bostock
 * Changes Copyright (c) 2016-2018, The University of Edinburgh and
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
 */

/**
 * Draws packed circles.
 *
 * @param {string} data_file - file with comma-separated values
 * (CSV).
 * @param {string} id_tag - ID of HTML tag in which the chart is
 * drawn.
 * @param {string} label_column - chart will have one circle for
 * each unique value in this column.
 * @param {string} value_column - chart will have one circle for
 * each unique value in this column. Value determines radius of
 * circle.
 * @param {integer} area_width - drawing area width.
 * @param {integer} area_height - drawing area height.
 */
function draw_circle_chart(data_file,
                           id_tag,
                           label_column,
                           value_column,
                           area_width,
                           area_height) {

    function type(d) {
        d[value_column] = +d[value_column];
        return d[value_column] ? d : null;
    }

    var id_tag_link = "#" + id_tag;
    var element = d3.select(id_tag_link)
        .attr("width", area_width)
        .attr("height", area_height);
    var svg = element.append("svg")
        .attr("width", area_width)
        .attr("height", area_height);
    var g = svg.append("g")
        .attr("width", area_width)
        .attr("height", area_height)
        .attr("transform", "translate(1, 1)");

    var format = d3.format(",d");

    var pack = d3.pack()
        .size([area_width - 2, area_height - 2])
        .padding(3);

    d3.csv(data_file, type, function(error, data) {
        if (error) {
            throw error;
        }

        var circle_id = 0;
        data.forEach(function(row) {
            row.circle_id = circle_id;
            circle_id++;
        });

        var root = d3.hierarchy({children: data})
            .sum(function(d) { return d[value_column]; })
            .sort(function(a, b) { return b[value_column] - a[value_column]; });

        pack(root);

        var node = g
            .selectAll("g")
            .data(root.children)
            .enter().append("g")
            .attr("transform", function(d) {
                return "translate(" + d.x + "," + d.y + ")"; })
            .attr("class", "node");

        node.append("circle")
            .attr("id", function(d) { return "node-" + d.data.circle_id; })
            .attr("r", function(d) { return d.r; });

        node.append("clipPath")
            .attr("id", function(d) { return "clip-" + d.data.circle_id; })
            .append("use")
            .attr("xlink:href", function(d) { return "#node-" + d.data.circle_id + ""; });

        node.append("text")
            .attr("clip-path", function(d) { return "url(#clip-" + d.data.circle_id + ")"; })
            .selectAll("tspan")
            .data(function(d) {
                return d.data[label_column].split(".").pop().split(/(?=[A-Z][^A-Z])/g); })
            .enter().append("tspan")
            .attr("x", 0)
            .attr("y", function(d, i, nodes) {
                return 13 + (i - nodes.length / 2 - 0.5) * 10; })
            .text(function(d) { return d; });

        node.append("title")
            .text(function(d) {
                return d.data[label_column] + "\n" + format(d.data[value_column]); });
    });
};
