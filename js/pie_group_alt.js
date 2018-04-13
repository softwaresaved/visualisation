/**
 * D3 multiple pie charts.
 *
 * Uses styles: text, .arc path, .legend rect .legend text
 * 
 * Copyright (c) 2018, The University of Edinburgh.
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
 * Draws a set of pie charts.
 *
 * @param {string} data_file - file with comma-separated values
 * (CSV). The first column is assumed to hold categories. Subsequent
 * columns are assumed to hold counts for each category. For example:
 * the first column could be a set of answers e.g. "N/A", "Not at
 * all", "Moderately", "Significantly", "Game-Changing" and
 * subsequent columns questions for which these categories were
 * the available responses.
 * There will be one pie chart for each of these columns.
 * Each pie chart will have one wedge per value in the first
 * column.
 * @param {string} id_tag - ID of HTML tag in which the pie charts
 * are drawn.
 * @param {string} prefix_id_tag - prefix for IDs of HTML tags for
 * individual pie charts.
 * @param {integer} width - width for each pie chart.
 * @param {integer} height - height for each pie chart.
 * @param {string} colourScheme - comma-separated string of colour
 * names. These are used to determine wedge colours. The number of
 * colours must match the number of categories in the first column,
 * which are assumed to be unique. 
 */
function draw_pie_charts(data_file,
                         id_tag,
                         prefix_id_tag,
                         width,
                         height,
                         colour_scheme) {

    var graphs = d3.select("#" + id_tag)
    d3.csv(data_file, function(error, data) {
        if (error) throw error;
        var headers = d3.keys(data[0]);
        var categoryHeader = headers[0];
        var numHeaders = headers.length;
        var i = 0;
        for (i = 1; i < numHeaders; i++)
        {
            var div = graphs.append("div").attr("id", prefix_id_tag + "div" + i);
            div.append("text").html(headers[i]);
            div.append("div").attr("id", prefix_id_tag + i).classed("pie", true);
            draw_pie(data_file, prefix_id_tag + i, categoryHeader, headers[i], width, height, colour_scheme);
        }
    });
};
