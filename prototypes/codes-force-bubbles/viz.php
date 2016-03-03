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
var category_column = "Primary Funder";
var data_file = "data/ssi-consultancy.csv";

var width = 400;
var height = 500;

var colour_bins_pie = [
    { label: "1", bound: 1, fill: "#e0e2fe" },
    { label: "2", bound: 2, fill: "#c5c9fd" },
    { label: "3-5", bound: 5, fill: "#a6acff" },
    { label: "6-10", bound: 10, fill: "#515cfd" },
    { label: "Over 10", bound: Number.MAX_VALUE, fill: "#0000ff" }
];
</script>
<!--
     <h1>Number of consultancy projects per funder</h1>
<div id="pieone"/>
<script>
// TODO clarify role of type() function!!!!!
var pie_location="#pieone";
function type(d) {
d.count =+ d.count;
return d;
}
</script>
     <?php include 'ssi_consultancy_pie.php'; ?>
</div>
-->
     <h1>Consultancy effort by funder</h1>
<p/>

<div id="pietwo"/>
<script>
category_column = "Funder";
data_file = "data/funders_effort.csv";
pie_location="#pietwo";
function pie_count(row){
console.log("1");
    return 1;
};
function type(d) {
d.count =+ d.count;
return d;
};
</script>
     <?php include 'ssi_consultancy_pie.php'; ?>
</div>

     <h1>Number of consultancy projects per funder</h1>
<div id="chartone"/>
<script>
var chart_location="#chartone";
function pie_count(row){
console.log("2");
   return row["Effort"];
};
function type(d) {
d.Projects =+ d.Projects;
return d;
};
</script>
<div>
     <?php include 'projectsfunder_barchart.php'; ?>
</div>
  </body>
</html>
