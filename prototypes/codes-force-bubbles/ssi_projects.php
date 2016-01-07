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
var data_file = 'data/SSIConsultancyProjects.csv';
var category_names = ["Overview",
		      "Funder",
		      "Institution",
		      "Type",
		      "Research Field"];
var categories = ["none",
		  "Funder",
		  "Institution",
		  "Type",
		  "Research Field"];
var legend_text = "Effort";
var name_column = "Project Name";
var scaling_column = "Effort";
var level_column = "Effort";
var cull_threshold = 0.25;
var scale_bins = [
		  { label: "Less than 0.25 months", count: 0.25, fill: "#fee5d9" },
		  { label: "0.25-0.5 months", count: 0.5, fill: "#fcbba1" },
		  { label: "0.5-1 months", count: 1, fill: "#fc9272" },
		  { label: "1-2 months", count: 2, fill: "#fb6a4a" },
		  { label: "2-3 months", count: 3, fill: "#de2d26" },
		  { label: "More than 3 months", count: 5000, fill: "#a50f15" }
		  ];

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
