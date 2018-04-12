/**
 * D3 horizontal bar chart
 *
 * Derived from original downloaded from Horizontal Bar Chart
 * https://bl.ocks.org/curran/e842c1b64974666c60fc3e437f8c8cf9
 * on 11/04/2018.
 * 
 * Changes: Wrapped code within a function; replaced hard-coded
 * file name, column names, labels with arguments passed in via
 * function call; inserts <svg> element instead of assuming one has
 * been defined in HTML; tool-tip displays value of each bar on
 * mouse-over.
 *
 * Uses styles: body, .domain, rect, .tick line, .tick text,
 * .axis-label, .bar-value
 *
 * Copyright (c) 2017, Curran Kelleher
 * Changes Copyright (c) 2018, The University of Edinburgh.
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
 * Draw horizontal bar chart.
 *
 * @param {string} data_file - file with comma-separated values
 * (CSV).
 * @param {string} id_tag - ID of HTML tag in which the bar chart is
 * drawn.
 * @param {string} label_column - bar chart will have one Y axis bar for
 * each unique value in this column.
 * @param {string} value_column - bar chart will have one Y axis bar for
 * each unique value in this column. Value determines length of bar.
 * @param {integer} width - drawing area width.
 * @param {integer} height - drawing area height.
 */
function draw_bar_horiz(data_file,
                        id_tag,
                        label_column,
                        value_column,
                        width,
                        height) {

    const id_tag_link = "#" + id_tag;
    const element = d3.select(id_tag_link);
    const svg = element.append("svg")
        .attr("width", width)
        .attr("height", height);

    const tooltip = element.append("div")
        .attr("class", "bar-value")
        .style("position", "absolute")
        .style("visibility", "hidden");

    const xValue = d => d[value_column];
    const xLabel = value_column;
    const yValue = d => d[label_column];
    const yLabel = label_column;

    const margin = { left: 300, right: 30, top: 30, bottom: 75 };
    const innerWidth = width - margin.left - margin.right;
    const innerHeight = height - margin.top - margin.bottom;

    const g = svg.append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

    const xAxisG = g.append('g')
        .attr('transform', `translate(0, ${innerHeight})`);
    const yAxisG = g.append('g');

    xAxisG.append('text')
      .attr('class', 'axis-label')
      .attr('x', innerWidth / 2)
      .attr('y', 55)
      .text(xLabel);

    const xScale = d3.scaleLinear();
    const yScale = d3.scaleBand()
        .paddingInner(0.3)
        .paddingOuter(0);

    const xTicks = 10;

    const xAxis = d3.axisBottom()
        .scale(xScale)
        .ticks(xTicks)
        .tickPadding(5)
        .tickSize(-innerHeight);
    const yAxis = d3.axisLeft()
        .scale(yScale)
        .tickPadding(5)
        .tickSize(-innerWidth);

    const row = d => {
        return {
          [label_column]: d[label_column],
          [value_column]: +d[value_column]
        };
      };

    d3.csv(data_file, row, function(error, data) {
        if (error) throw error;

        xScale
            .domain([0, d3.max(data, xValue)])
            .range([0, innerWidth])
            .nice(xTicks);
        xAxisG.call(xAxis);

        yScale
            .domain(data.map(yValue).reverse())
            .range([innerHeight, 0]);
        yAxisG.call(yAxis);
        yAxisG.selectAll('.tick line').remove();

        g.selectAll('rect').data(data)
            .enter().append('rect')
            .attr('x', 0)
            .attr('y', d => yScale(yValue(d)))
            .attr('width', d => xScale(xValue(d)))
            .attr('height', d => yScale.bandwidth())
            .on("mouseover", function(d){return tooltip.style("visibility", "visible").text(d[value_column]);})
            .on("mousemove", function(){return tooltip.style("top", (d3.event.pageY-10)+"px").style("left",(d3.event.pageX+10)+"px");})
            .on("mouseout", function(){return tooltip.style("visibility", "hidden");})
    });
};
