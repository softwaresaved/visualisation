<style>
.arc text {
  font: 14px sans-serif;
  text-anchor: middle;
}

.arc path {
  stroke: #fff;
}
</style>
<script>
//Including file needs to define:
//var category_column = "Primary Funder";
//var data_file = "data/ssi-consultancy.csv";
//var colour_bins_pie = [
//    { label: "1", bound: 1, fill: "#e0e2fe" },
//    { label: "2", bound: 2, fill: "#c5c9fd" },
//    { label: "3-5", bound: 5, fill: "#a6acff" },
//    { label: "6-10", bound: 10, fill: "#515cfd" },
//    { label: "Over 10", bound: Number.MAX_VALUE, fill: "#0000ff" }
//];
//var width = 400;
//var height = 500;

d3.csv(data_file, type, function(error, raw_data) {
    if (error) throw error;

    console.log("Number of records: " + raw_data.length);

var radius = Math.min(width, height) / 2;

var arc = d3.svg.arc()
    .outerRadius(radius - 10)
    .innerRadius(0);

var labelArc = d3.svg.arc()
    .outerRadius(radius - 40)
    .innerRadius(radius - 40);

var pie = d3.layout.pie()
    .sort(null)
    .value(function(d) { return d.count; });

var svg = d3.select(pie_location).append("svg")
    .attr("width", width)
    .attr("height", height)
    .append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

console.log("Drawing area: " + pie_location);


    var categories = {};
    raw_data.forEach(function(row) {
      if (!categories[row[category_column]]) {
          categories[row[category_column]] = 0;
      }
      categories[row[category_column]]++;
    });

    var data = [];
    Object.keys(categories).forEach(function(key) {
        data.push({
            category: key,
            count: categories[key]
        });
    });

    var g = svg.selectAll(".arc")
        .data(pie(data))
        .enter().append("g")
        .attr("class", "arc");

    g.append("path")
      .attr("d", arc)
      .style("fill", function(d) { return get_pie_colour(d.data.count); });

    g.append("text")
      .attr("transform", function(d) { return "translate(" + labelArc.centroid(d) + ")"; })
      .attr("dy", ".35em")
      .text(function(d) { return d.data.category; });

function type(d) {
    d.count =+ d.count;
    return d;
};

function get_pie_colour(value) {
    for (var k = 0; k < colour_bins_pie.length; k++) {
        value = parseInt(value);
        if (value <= colour_bins_pie[k].bound)
        {
            return colour_bins_pie[k].fill;
        }
    }
    return colour_bins_pie[colour_bins.pie.length - 1].fill;
};

});


</script>
