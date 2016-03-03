// Bar chart.
// Based on D3 example at 
// TODO
// 
// Requires styles for:
// .bar text - bar labels
// .bar:hover - bar mouse over colour
// .axis - axis label
// .axis path - axis lines
// .axis line - axis lines
// .x.axis path - X-axis lines

// Draw bar chart
// - data_file - name of file with comma-separated values.
// - location_tag - ID of tag in HTML document in which the bar chart
//   is drawn (e.g. "#pie").
// - category_column - each unique value in this column will have its
//   own bar in the bar chart.
// - chart_count - callback function which, for a specific row, returns
//   a value which is added to the total value computed for the
//   category_column value for that row.
// - width - drawing area width.
// - height - drawing area height.

function draw_chart(data_file, 
                    location_tag, 
                    category_column, 
                    chart_count,
                    area_width = 500,
                    area_height = 400) {

    function type(d) {
        d.value =+ d.value;
        return d;
    }

    d3.csv(data_file, type, function(error, raw_data) {
        if (error) {
            throw error;
        }
        
        console.log("Bar chart location tag: " + location_tag);
        console.log("Number of rows: " + raw_data.length);

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

        var svg = d3.select(location_tag).append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        // Iterate through raw_data. For each distinct value in
        // category_column, compute a value based upon the
        // value returned by pie_count for each row.
        var categories = {};
        raw_data.forEach(function(row) {
            if (!categories[row[category_column]]) {
                categories[row[category_column]] = 0;
            }
            categories[row[category_column]] += chart_count(row);
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
