<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Software Sustainability Institute Consultancy</title>
    <link rel="shortcut icon" href="../common/delimited-favicon-v4.ico">
  </head>
  <body>
   <h1>Software Sustainability Institute Consultancy</h1>

<script>
// CSV data file.
var data_file = 'data/ssi-consultancy.csv';
// Names of columns in CSV data by which data can be grouped, and
// corresponding labels buttons to select these columns.
// A "none" entry provides a default view with the data ungrouped.
var columns = [
               { name: "none", label: "Overview" },
               { name: "Primary Funder" , label: "Funder" },
               { name: "Type", label: "Via"},
               { name: "Research Field", label: "Research Field" }
               ];
// Name of column in CSV data used to label console log info.
var name_column = "Project Name";
// Name of column in CSV data used to calculate bubble radii.
var radius_column = "PMs";
// Rows of data with values of radius_column below this threshold are
// not drawn.
var radius_threshold = 0.1;
// Name of column in CSV data used to calculate bubble colour.
var colour_column = "PMs";
// Ranges of values used to map colour_column values to colours, and
// also to create the legend.
var colour_bins = [
                  { label: "Less than 0.25 months", bound: 0.25, fill: "#fee5d9" },
                  { label: "0.25-0.5 months", bound: 0.5, fill: "#fcbba1" },
                  { label: "0.5-1 months", bound: 1, fill: "#fc9272" },
                  { label: "1-2 months", bound: 2, fill: "#fb6a4a" },
                  { label: "2-3 months", bound: 3, fill: "#de2d26" },
                  { label: "More than 3 months", bound: Number.MAX_VALUE, fill: "#a50f15" }
                  ];

// Label for legend showing the ranges of values of colour_column.
var legend_label = "Staff Effort (months)";

function assign_colour_bin(field, bin) {
  value = parseFloat(field);
  return value < colour_bins[bin].bound;
}

function bubble_caption(d) {
  return "Name: " + d["Project Name"] +
    "<br/>Primary funder: " + d["Primary Funder"] +
    "<br/>Other funders: " + d["Other Funders"] +
    "<br/>Institution: " + d["Institution"] +
    "<br/>Field: " + d["Research Field"] +
    "<br/>Via: " + d["Type"] +
    "<br/>Effort: " + d["PMs"] + " staff months";
}
</script>

   <?php include 'prototype.php'; ?>
   <?php include 'graph_bubbles.php'; ?>

<script>
var width = 400;
var height = 500;
</script>

    <?php include 'ssi_consultancy_pie.php'; ?>

    <h1>Consultancy effort by funder</h1>
    <div id="pieX"></div>
<script>
function pie_countX(row) {
   return row["Effort"];
};
function typeX(d) {
    d.count =+ d.count;
    return d;
};
var colour_bins_pieX = [
    { label: "1", bound: 1, fill: "#e0e2fe" },
    { label: "5", bound: 5, fill: "#c5c9fd" },
    { label: "10", bound: 10, fill: "#a6acff" },
    { label: "20", bound: 20, fill: "#515cfd" },
    { label: "Over 20", bound: Number.MAX_VALUE, fill: "#0000ff" }
];
show_pie("data/funders_effort.csv", "#pieX", "Funder", typeX, pie_countX, colour_bins_pieX);
</script>

    <h1>Consultancy projects by funder</h1>
    <div id="pieY"></div>
<script>
function pie_countY(row) {
   return 1;
};
function typeY(d) {
    d.count =+ d.count;
    return d;
};
var colour_bins_pieY = [
    { label: "1", bound: 1, fill: "#e0e2fe" },
    { label: "2", bound: 2, fill: "#c5c9fd" },
    { label: "3-5", bound: 5, fill: "#a6acff" },
    { label: "6-10", bound: 10, fill: "#515cfd" },
    { label: "Over 10", bound: Number.MAX_VALUE, fill: "#0000ff" }
];
show_pie("data/ssi-consultancy.csv", "#pieY", "Primary Funder", typeY, pie_countY, colour_bins_pieY);
</script>

    <?php include 'projectsfunder_barchart.php'; ?>
    <h1>Number of consultancy projects per funder</h1>
    <div id="chartX"></div>
<script>
var chart_location="#chartX";
function chart_countX(row) {
   return 1;
};
function typeZ(d) {
    d.Projects =+ d.Projects;
    return d;
};
show_chart("data/ssi-consultancy.csv", "#chartX", "Primary Funder", typeZ, chart_countX);
</script>

  </body>
</html>
