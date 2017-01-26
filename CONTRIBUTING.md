# Contributing code

If you wish to contribute code - visualisations and data - to this 
repository then please follow these steps:

1. Fork this repository.
2. Read [README](./README.md) and [Implementation 
Details](./Implementation.md) to see:
  - How to view visualisations locally.
  - What data sets and JavaScript are used by each page in HTML.
  - What Python scripts are used to download data.
  - What Python scripts are used to preprocess data.
  - What files go where in the repository.
3. Look at the html/, src/, data/ and js/ directories to see how they 
re structured and their files are named.
4. Develop your visualisation:
   - Place HTML into a sub-directory of html/
   - Place data into a sub-directory of data/
   - Place Python download and preprocessing scripts into a 
sub-directory of src/
   - Ensure your files have meaningful names and respect the naming 
scheme already used.

If you need to add JavaScript libraries or fragments downloaded from 
third-parties, then:

1. Add the JavaScript to js/ and any related CSS to css/ before you make 
any changes to it.
   - Ensure your files have meaningful names and respect the naming 
scheme already used.
2. Add the JavaScript's licence to licences/ and add a new entry for the 
JavaScript in the the Third-party Code section of the 
[README](./README.md).
   - For licences, ensure your licence file respects the naming scheme 
already used.
3. If you make any changes to the JavaScript then:
   - Add a comment indicating the change you made. If D3 or other 
JavaScript libraries are updated this can make updating the JavaScript 
here easier.

If you change existing code in this repository, then make sure you rerun 
the related Python scripts and view the visualisations, to ensure they 
are still OK.

When you are ready to contribute your changes, submit a pull request. 
mikej888 will then review the changes and, if OK, merge them.

If changes are pushed to this repository, without going via a pull 
request, then mikej888 will:

1. Create a new branch with the changes.
2. Delete the changes from the default gh-pages branch.

