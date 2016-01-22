<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>ARCHER Code Usage</title>
    <link rel="shortcut icon" href="../common/delimited-favicon-v4.ico">
  </head>
  <body>
    <h1>ARCHER application usage</h1>

<script>
// CSV data file.
var data_file = 'data/d3codes_summary.csv';
// Names of columns in CSV data by which data can be grouped, and
// corresponding labels buttons to select these columns.
// A "none" entry provides a default view with the data ungrouped.
var columns = [
               { name: "none", label: "Overview" },
               { name: "CodeType", label: "Code Type" },
               { name: "ResArea", label: "Research Area" },
               { name: "ProgLang", label: "Programming Language" },
               { name: "LicType", label: "Licence Type" },
               ];
// Name of column in CSV data used to label console log info.
var name_column = "Code";
// Name of column in CSV data used to calculate bubble radii.
var radius_column = "Usage";
// Rows of data with values of radius_column below this threshold are
// not drawn.
var radius_threshold = 10;
// Name of column in CSV data used to calculate bubble colour.
var colour_column = "Users";
// Ranges of values used to map colour_column values to colours, and
// also to create the legend.
var colour_bins = [
                  { label: "Less than 5 users", bound: 5, fill: "#fee5d9" },
                  { label: "5-10 users", bound: 10, fill: "#fcbba1" },
                  { label: "10-20 users", bound: 20, fill: "#fc9272" },
                  { label: "20-50 users", bound: 50, fill: "#fb6a4a" },
                  { label: "50-100 users", bound: 100, fill: "#de2d26" },
                  { label: "More than 100 users", bound: Number.MAX_VALUE, fill: "#a50f15" }
                   ];
// Label for legend showing the ranges of values of colour_column.
var legend_label = "Number of Users";

function assign_colour_bin(field, bin) {
  value = parseFloat(field);
  return value < colour_bins[bin].bound;
}

function bubble_caption(d) {
  return "Name: " + d.Code + "<br/>Usage: " + d.Usage + " node hours" +
    "<br/>Jobs: " + d.Jobs +
    "<br/>Usage Rank: " + d.Rank +
    "<br/>Users: " + d.Users;
}
</script>

    <?php include 'graph_bubbles.php'; ?>
  </body>
</html>
