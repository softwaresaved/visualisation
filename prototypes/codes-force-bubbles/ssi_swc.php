<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Software Sustainability Institute and Software Carpentry</title>
    <link rel="shortcut icon" href="../common/delimited-favicon-v4.ico">
  </head>
  <body>
    <h1>Software Sustainability Institute and Software Carpentry</h1>

<script>
// CSV data file.
var data_file = 'data/ssi-swc.csv';
// Names of columns in CSV data by which data can be grouped, and
// corresponding labels buttons to select these columns.
// A "none" entry provides a default view with the data ungrouped.
var columns = [
               { name: "none", label: "Overview" },
               { name: "Country" , label: "Country" },
               { name: "Domain", label: "Research Field" }
               ];
// Name of column in CSV data used to label console log info.
var name_column = "Date";
// Name of column in CSV data used to calculate bubble radii.
var radius_column = "Attendees";
// Rows of data with values of radius_column below this threshold are
// not drawn.
var radius_threshold = 0;
// Name of column in CSV data used to calculate bubble colour.
var colour_column = "Attendees";
// Ranges of values used to map colour_column values to colours, and
// also to create the legend.
var colour_bins = [
                   { label: "Less than 10", bound: 10, fill: "#e0e2fe" },
                   { label: "10-20", bound: 20, fill: "#c5c9fd" },
                   { label: "20-30", bound: 30, fill: "#a6acff" },
                   { label: "30-40", bound: 40, fill: "#515cfd" },
                   { label: "More than 40", bound: Number.MAX_VALUE, fill: "#0000ff" }
                   ];
// Label for legend showing the ranges of values of colour_column.
var legend_label = "Attendees";

function bubble_caption(d) {
  return "Date: " + d["Date"] +
    "<br/>Department: " + d["Department"] +
    "<br/>Institution: " + d["Institution"] +
    "<br/>Country: " + d["Country"] +
    "<br/>Field: " + d["Domain"] +
    "<br/>Attendees: " + d["Attendees"];
}
</script>

   <?php include 'graph_bubbles.php'; ?>
  </body>
</html>
