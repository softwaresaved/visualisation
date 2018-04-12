/**
 * Collection of pie charts.
 *
 * Uses styles: text, .arc path, .legend rect, .legend text
 *
 * Copyright (c) 2016-2018, The University of Edinburgh.
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
 * Draws a single pie chart for responses to questionnaire data.
 * Helper method for draw_pie_group below.
 *
 * @param {string} id_tag_link - ID of HTML tag in which the pie charts
 * are drawn, prefixed by "#".
 * @param {string} category_header - name of category header.
 * @param {object} data - data, first row is assumed to be a header
 * row with column names.
 * @param {function} pie - object returned by d3.pie().
 * drawn.
 * @param {string} index - column index for data rendered by the pie chart.
 * @param {string} title - pie chart title.
 * @param {function} colours - function to return colours.
 * @param {integer} width - drawing area width.
 * @param {integer} height - drawing area height.
 * @param {integer} legend_size - legend width/height.
 * @param {integer} legend_spacing - legend spacing.
 * @param {function} arc - object returned by d3.arc().
 */
function draw_pie_member(id_tag_link,
                         category_header,
                         data,
                         pie,
                         index,
                         title,
                         colours,
                         width,
                         height,
                         legend_size,
                         legend_spacing,
                         arc)
{
    var header = d3.keys(data[0]);
    var labels = [];
    data.forEach(function(d)
    {
        labels.push(d[category_header]);
    });
    var svg = d3.select(id_tag_link).append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");
    svg.append("text")
        .attr("y", 150)
        .text(title);
    var g = svg.selectAll(".arc")
        .data(pie(data))
        .enter().append("g")
        .attr("class", "arc");
    g.append("path")
        .attr("d", arc)
        .attr("data-legend", function(d) { return d.data[header[0]]; })
        .attr("data-legend-pos", function(d, i) { return i; })
        .style("fill", function(d) { return colours(d.data[header[0]]); });
    g.append("title")
        .text(function(d) { return d.data[header[index]]; });

    var legend = svg.selectAll('.legend')
        .data(labels)
        .enter()
        .append('g')
        .attr('class', 'legend')
        .attr('transform', function(d, i) {
            var height = legend_size + legend_spacing;
            var offset =  height * colours.length / 2;
            var horz = 10 * legend_size;
            var vert = i * height - offset;
            return 'translate(' + horz + ',' + vert + ')';
        });
    legend.append('rect')
        .attr('width', legend_size)
        .attr('height', legend_size)
        .style('fill', colours)
        .style('stroke', colours);
    legend.append('text')
        .attr('x', legend_size + legend_spacing)
        .attr('y', legend_size - legend_spacing)
        .text(function(d) { return d; });
};

/**
 * Draws a group of pie charts for responses to question data.
 *
 * The data is expected to consist of:
 * * Initial header row with M questions e.g. 
 *   "Improve how you manage your project?",
 *   "Improve the usability of your software?" etc.
 * * Initial column with N categories e.g. "N/A", "Not at all", 
 *   "Moderately" etc.
 * * Data element at (0,0) is a header name for categories.
 * * N rows with the total number of responses for each question/category.
 *
 * @param {string} data_file - file with comma-separated values
 * (CSV), formatted as above.
 * @param {string} category_header - name of category header.
 * @param {string} id_tag - ID of HTML tag in which the pie charts are
 * drawn.
 * @param {string} colour_str - colours for each wedge as ","-concatenated
 * string e.g. "Red,Yellow,Blue". This must have the same number of members
 * as there are categories.
 * @param {integer} width - drawing area width.
 * @param {integer} height - drawing area height.
 */
function draw_pie_group(data_file,
                        category_header,
                        id_tag,
                        colour_str,
                        width,
                        height)
{
    var id_tag_link = "#" + id_tag;
    var colours = d3.scaleOrdinal().range(colour_str.split(","));
    // Fudge factor for individual pie chart radius.
    var radius = Math.min(width - 100, height - 100) / 2;
    // Size of individual pie chart.
    var pie_arc = d3.arc()
        .outerRadius(radius - 10)
        .innerRadius(0);
    // Size of each colour block in the legend.
    var legend_size = 18;
    var legend_spacing = 4;

    d3.csv(data_file, function(error, data)
    {
        // Get column names to use as title for each pie chart.
        var header = d3.keys(data[0]);
        var num_columns = header.length;
        // Convert strings from D3 into numbers.
        data.forEach(function(d)
        {
            for (var i=1; i < num_columns; i++)
            {
                d[header[i]] = +d[header[i]];
            }
        });
        // Create one pie chart for each column of data.
        // This could be changed to a custom layout.
        for (var i=1; i < num_columns; i++)
        {
            draw_pie_member(
                id_tag_link,
                category_header,
                data,
                d3.pie()
                    .sort(null)
                    .value(function(d) { return d[header[i]]; }), 
                i,
                header[i],
                colours,
                width,
                height,
                legend_size,
                legend_spacing,
                pie_arc);
      }
    });
};
