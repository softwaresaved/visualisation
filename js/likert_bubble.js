/**
 * D3 Likert bubble chart
 *
 * Uses styles: body, .domain, rect, .tick line, .tick text,
 * .axis-label, .bubble-value
 *
 * Copyright (c) 2018, The University of Edinburgh.
 *
 * Permission is hereby granted, free of charge, to any person
 * obtaining a copy of this software and associated documentation
 * files (the "Software"), to deal in the Software without
 * restriction, including without limitation the rights to use, copy,
 * modify, merge, publish, distribute, sublicense, and/or sell copies
 * of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions: 
 *
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software. 
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
 * LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
 * OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
 * WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 
 */

/**
 * Draws Likert bubble bar chart.
 *
 * @param {string} data_file - file with comma-separated values
 * (CSV). First row is assumed to contain statements and first column
 * is assumed to contain responses, or vice versa.
 * @param {string} id_tag - ID of HTML tag in which the bar chart is
 * drawn.
 * @param {string} row_statements_column_responses - if "true" then
 * first row of data_file contains statements, which are rendered on the
 * Y axis and first column contains responses, which are rendered on
 * the X axis. If "false", then vice versa.
 * @param {string} min_colour - colour to shade bubbles corresponding
 * to minimum values. Colours for other values are interpolated between
 * this and min_colour. 
 * @param {string} max_colour - colour to shade bubbles corresponding
 * to maximum values.
 * @param {integer} width - drawing area width.
 * @param {integer} height - drawing area height.
 */
function draw_likert_bubble(data_file,
                            id_tag,
                            row_answers_column_questions,
                            min_colour,
                            max_colour,
                            width,
                            height) {

    const id_tag_link = "#" + id_tag;
    const element = d3.select(id_tag_link);
    const svg = element.append("svg")
        .attr("width", width)
        .attr("height", height)

    const tooltip = element.append("div")
        .attr("class", "bubble-value")
        .style("position", "absolute")
        .style("visibility", "hidden");

    const margin = { left: 500, right: 30, top: 100, bottom: 200 };
    const innerWidth = width - margin.left - margin.right;
    const innerHeight = height - margin.top - margin.bottom;
    const radius = 40;

    const g = svg.append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

    const xAxisG = g.append('g')
        .attr('transform', `translate(0, ${innerHeight})`);
    const yAxisG = g.append('g');

    const xScale = d3.scalePoint();
    const yScale = d3.scalePoint();

    const xAxis = d3.axisBottom()
        .scale(xScale)
        .tickPadding(radius)
        .tickSize(-innerHeight);

    const yAxis = d3.axisLeft()
        .scale(yScale)
        .tickPadding(radius)
        .tickSize(-innerWidth);

    d3.csv(data_file, function(error, data) {
        if (error) throw error;

        var row_categories = d3.keys(data[0]);
        // Get/remove 1st element, header of column categories.
        var column_categories_header = row_categories.splice(0, 1);
        console.log("Row categories:\n" + row_categories);

        var column_categories = [];
        data.forEach(function(r)
        {
            column_categories.push(r[column_categories_header]);
        });
        console.log("Column categories:\n" + column_categories);

        var data_filtered = []
        data.forEach(function(row)
        {
            var column_category = row[column_categories_header];
            row_categories.forEach(function(row_category)
            {
                data_filtered.push(
                    { 
                      "row_category": row_category,
                      "column_category": column_category,
                      "value": +row[row_category]
                    }
                );
            });
        });

        var max = d3.max(data_filtered, function(d) { return d["value"]; });

        var x_categories = column_categories;
        var y_categories = row_categories;
        var x_value = "column_category";
        var y_value = "row_category";
        if (! row_answers_column_questions)
        {
            x_categories = row_categories;
            y_categories = column_categories;
            x_value = "row_category";
            y_value = "column_category";
        }

        xScale
            .domain(x_categories)
            .range([0, innerWidth]);
        xAxisG.call(xAxis);
        xAxisG.selectAll(".tick").selectAll("text")
            .attr("y", 0)
            .attr("x", -radius)
            .attr("transform", "rotate(-45)")
            .style("text-anchor", "end");

        yScale
            .domain(y_categories)
            .range([0, innerHeight]);
        yAxisG.call(yAxis);

        var valueScale = d3.scaleLinear().domain([0, max]).range([0, radius]);
        var colourScale = d3.scaleLinear().domain([0, max]).range([min_colour, max_colour]);

        g.selectAll("circle").data(data_filtered)
          .enter().append("circle")
          .attr("cx", function(d) { return xScale(d[x_value]); })
          .attr("cy", function(d) { return yScale(d[y_value]); })
          .attr("r", function (d) { return valueScale(d["value"]); })
          .attr("fill", function (d) { return colourScale(d["value"]); })
          .attr("stroke", "black")
          .attr("stroke-width", 1)
          .on("mouseover", function(d){ return tooltip.style("visibility", "visible").text(d["value"]); })
          .on("mousemove", function(){ return tooltip.style("top", (d3.event.pageY-10)+"px").style("left",(d3.event.pageX+10)+"px"); })
          .on("mouseout", function(){ return tooltip.style("visibility", "hidden"); })
    });
}
