<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>ARCHER Code Usage</title>
    <link rel="shortcut icon" href="../common/delimited-favicon-v4.ico">
  </head>
  <body>

<script>
var data_file = 'data/d3codes_summary.csv';
var category_names = ["Overview",
		      "Code Type",
		      "Research Area",
		      "Programming Language",
		      "Licence Type"];
var categories = ["none",
		  "CodeType",
		  "ResArea",
		  "ProgLang",
		  "LicType"];
var legend_text = "Number of Users";
var name_column = "Code";
var scaling_column = "Usage";
var level_column = "Users";
var cull_threshold = 10;
var scale_bins = [
		  { label: "Less than 5 users", count: 5, fill: "#fee5d9" },
		  { label: "5-10 users", count: 10, fill: "#fcbba1" },
		  { label: "10-20 users", count: 20, fill: "#fc9272" },
		  { label: "20-50 users", count: 50, fill: "#fb6a4a" },
		  { label: "50-100 users", count: 100, fill: "#de2d26" },
		  { label: "More than 100 users", count: 5000, fill: "#a50f15" }
		  ];

function bubble_caption(d) {
  return "Name: " + d.Code + "<br/>Usage: " + d.Usage + " node hours<br/>Jobs: " + d.Jobs +
    "<br/>Usage Rank: " + d.Rank + "<br/>Users: " + d.Users;
}
</script>

    <?php include 'usage.php'; ?>
  </body>
</html>
