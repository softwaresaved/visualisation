/**
 * D3 pie chart
 *
 * Derived from original downloaded from Pie Chart
 * https://bl.ocks.org/mbostock/3887235#index.html
 * on 05/08/2016.
 *
 * Changes: Wrapped code within a function; replaced hard-coded
 * file name, column names, labels with arguments passed in via
 * function call, draws legend.
 *
 * Uses styles: .arc text, .arc path, .wedge-value, .legend text
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
 */

/**
 * Draw pie chart.
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
    var element = d3.select(id_tag_link);
    var svg = element.append("svg")
        .attr("width", width)
        .attr("height", height);

    var svg_g = svg
        .append("g")
        .attr("transform", "translate(" + width/2 + "," + height/2 + ")");

    var legend_g = svg
        .append("g")
        .attr("transform", "translate(" + ((width/2)+radius) + "," + 0 + ")");

    var tooltip = element.append("div")
        .attr("class", "wedge-value")
        .style("position", "absolute")
        .style("visibility", "hidden");

    d3.csv(data_file, type, function(error, data) {
        if (error) throw error;

        var g = svg_g.selectAll(".arc")
            .data(pie(data))
            .enter().append("g")
            .attr("class", "arc")
            .on("mouseover", function(d){return tooltip.style("visibility", "visible").text(d.data[label_column] + ": " + d.data[value_column]);})
            .on("mousemove", function(){return tooltip.style("top", (d3.event.pageY-10)+"px").style("left",(d3.event.pageX+10)+"px");})
            .on("mouseout", function(){return tooltip.style("visibility", "hidden");})

        g.append("path")
            .attr("d", arc)
            .style("fill", function(d) { return colours[d.index]; }
        );

        // As labels can be obscured by wedges, draw another
        // pie chart with labels only.
        var g_labels = svg_g.selectAll(".arc-labels")
            .data(pie(data))
            .enter().append("g")
            .attr("class", "arc-labels");
        g_labels.append("text")
            .attr("transform", function(d) { return "translate(" + labelArc.centroid(d) + ")"; })
            .attr("dy", ".35em")
            .text(function(d) {
                if (d.data[value_column] > 0) {
                    return d.data[label_column] +
                        "\n(" + d.data[value_column] + ")";
               } else {
                   return "";
               };
            });

        // Draw legend.
        var labels = [];
        var i = 0;
        data.forEach(function(d)
        {
            labels.push({"label": d[label_column], "colour": colours[i]});
            i++;
        });

        var legend_edge = 20;
        var legend_pad = 10;
        var legend_height = legend_edge + legend_pad;

        var legend = legend_g.selectAll('.legend')
            .data(labels)
            .enter()
            .append('g')
            .attr('class', 'legend')
            .attr('transform', function(d, i) {
                return 'translate(' + 0 + ',' + (i * legend_height) + ')';
            });
        legend.append('rect')
            .attr('width', legend_edge)
            .attr('height', legend_edge)
            .style("fill", function(d) { return d["colour"]; })
           .style('stroke', colours);
        legend.append('text')
            .attr('x', legend_edge + legend_pad)
            .attr('y', legend_edge - (legend_pad/2))
            .text(function(d) { return d["label"]; });
    });
};
