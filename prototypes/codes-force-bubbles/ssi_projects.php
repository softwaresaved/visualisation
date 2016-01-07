<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Software Sustainability Institute Consultancy</title>
    <link rel="shortcut icon" href="../common/delimited-favicon-v4.ico">
  </head>
  <body>

<script>
// CSV data file.
var data_file = 'data/SSIConsultancyProjects.csv';
// Names of columns in CSV data by which data can be grouped, and
// corresponding labels buttons to select these columns.
// A "none" entry provides a default view with the data ungrouped.
var columns = [
               { name: "none", label: "Overview" },
               { name: "Funder" , label: "Funder" },
               { name: "Institution", label: "Institution" },
               { name: "Type", label: "Type" },
               { name: "Research Field", label: "Research Field" }
               ];
// Name of column in CSV data used to label console log info.
var name_column = "Project Name";
// Name of column in CSV data used to calculate bubble radii.
var radius_column = "Effort";
// Rows of data with values of radius_column below this threshold are
// not drawn.
var radius_threshold = 0.1;
// Name of column in CSV data used to calculate bubble colour.
var colour_column = "Effort";
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
var legend_label = "Staff Effort";

function bubble_caption(d) {
  return "Name: " + d["Project Name"] +
    "<br/>Funder: " + d["Funder"] +
    "<br/>Institution: " + d["Institution"] +
    "<br/>Field: " + d["Research Field"] +
    "<br/>Type: " + d["Type"] +
    "<br/>Effort: " + d["Effort"] + " staff months";
}
</script>

   <?php include 'usage.php'; ?>
  </body>
</html>
