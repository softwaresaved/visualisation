<style>
.bar {
  fill: steelblue;
}

.bar:hover {
  fill: brown;
}

.axis {
  font: 10px sans-serif;
}

.axis path,
.axis line {
  fill: none;
  stroke: #000;
  shape-rendering: crispEdges;
}

.x.axis path {
  display: none;
}
</style>
<script>
function show_chart(data_file, chart_location, category_column, type, chart_count)
{

  d3.csv("data/ssi-consultancy.csv", type, function(error, raw_data) {
    if (error) throw error;

  var margin = {top: 20, right: 20, bottom: 100, left: 40},
      width = 400 - margin.left - margin.right,
      height = 300 - margin.top - margin.bottom;

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

  var svg = d3.select(chart_location).append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
    .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


var category_column="Primary Funder";

    var categories = {};
    raw_data.forEach(function(row) {
      if (!categories[row[category_column]]) {
          categories[row[category_column]] = 0;
      }
      categories[row[category_column]] += chart_count(row);
    });

    var data = [];
    Object.keys(categories).forEach(function(key) {
        data.push({
            Funder: key,
            Projects: categories[key]
        });
    });

//TODO SORT DATA

    x.domain(data.map(function(d) { return d.Funder; }));
    y.domain([0, d3.max(data, function(d) { return d.Projects; })]);

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
        .attr("x", function(d) { return x(d.Funder); })
        .attr("width", x.rangeBand())
        .attr("y", function(d) { return y(d.Projects); })
        .attr("height", function(d) { return height - y(d.Projects); });

    svg.selectAll(".bar")
        .data(data)
      .enter().append(".bar")
        .style("width", function(d) { return d.Projects * 10 + "px"; })
        .text(function(d) { return d.Projects; });

function type(d) {
  d.Projects = +d.Projects;
  return d;
}
});
};

</script>
