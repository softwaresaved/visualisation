// Pie chart.
// Based on D3 example at 
// https://bl.ocks.org/mbostock/3887235.
// 
// Requires styles for:
// .arc text - pie chart labels
// .arc path - pie chart wedge dividers

// Draw pie chart
// - data_file - name of file with comma-separated values.
// - location_tag - ID of tag in HTML document in which the pie chart
//   is drawn (e.g. "#pie").
// - category_column - each unique value in this column will have its
//   own wedge in the pie chart.
// - pie_count - callback function which, for a specific row, returns
//   a value which is added to the total value computed for the
//   category_column value for that row.
// - colour_bins - ordered list of dictionaries each with a numerical
//   "bound" value and a "fill" colour. 
// - area_width - drawing area width.
// - area_height - drawing area height.

function draw_pie(data_file, 
                  location_tag, 
                  category_column, 
                  pie_count, 
                  colour_bins,
                  area_width,
                  area_height) {

    function type(d) {
        d.value =+ d.value;
        return d;
    };

    d3.csv(data_file, type, function(error, raw_data) {
        if (error) {
            throw error;
        }

        console.log("Pie chart location tag: " + location_tag);
        console.log("Number of rows: " + raw_data.length);

        var radius = Math.min(area_width, area_height) / 2;

        var arc = d3.svg.arc()
            .outerRadius(radius - 10)
            .innerRadius(0);

        var labelArc = d3.svg.arc()
            .outerRadius(radius - 40)
            .innerRadius(radius - 40);

        var pie = d3.layout.pie()
            .sort(null)
            .value(function(d) { return d.value; });

        var svg = d3.select(location_tag).append("svg")
            .attr("width", area_width)
            .attr("height", area_height)
            .append("g")
            .attr("transform", "translate(" + area_width / 2 + "," + area_height / 2 + ")");

        // Iterate through raw_data. For each distinct value in
        // category_column, compute a value based upon the
        // value returned by pie_count for each row.
        var categories = {};
        raw_data.forEach(function(row) {
            if (!categories[row[category_column]]) {
                categories[row[category_column]] = 0;
            }
            categories[row[category_column]] += pie_count(row);
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
        
        var g = svg.selectAll(".arc")
            .data(pie(data))
            .enter().append("g")
            .attr("class", "arc");

        g.append("path")
            .attr("d", arc)
            .style("fill", function(d) { 
                return get_slice_colour(d.data.value); 
            });

        g.append("text")
            .attr("transform", function(d) { 
                return "translate(" + labelArc.centroid(d) + ")"; 
            })
            .attr("dy", ".35em")
            .text(function(d) { return d.data.category; });


        function get_slice_colour(value) {
            for (var k = 0; k < colour_bins.length; k++) {
                value = parseInt(value);
                if (value <= colour_bins[k].bound)
                {
                    return colour_bins[k].fill;
                }
            }
            return colour_bins[colour_bins.length - 1].fill;
        };
    });
};
