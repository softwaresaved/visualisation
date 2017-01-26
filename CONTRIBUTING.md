# Contributing code

If you wish to contribute code - visualisations and data - to this repository then please follow these steps:

1. Fork this repository into your own GitHub account.
   - You can view the visualisations at http://USERNAME.github.io/visualisation
2. Read [README](./README.md) and [Implementation Details](./Implementation.md). These explain:
   - How to view visualisations locally.
   - What data sets and JavaScript are used by each page in HTML.
   - What Python scripts are used to download data and preprocess data.
   - What files go where in the repository.
3. Look at the html/, src/, data/, js/ and css/ directories to see how they are structured and their files are named.
4. Develop your visualisation:
   - Place HTML into a sub-directory of html/.
   - Place data into a sub-directory of data/.
   - Place Python download and preprocessing scripts into src/.
   - Ensure your files have meaningful names and respect the naming scheme already used.
5. If you need to add JavaScript libraries or fragments downloaded from third-parties, then:
   - Add the JavaScript to js/ and any related CSS to css/ before you make any changes to it.
   - Add the JavaScript's licence to licences/ and add a new entry for the JavaScript in the Third-party Code section of [README](./README.md).
   - If you make any changes to the JavaScript then add a comment indicating the change you made. See existing JavaScript in js/ for examples. Commenting your changes can help make it easier to update the JavaScript if the original version you downloaded is updated with bug fixes or enhancements.
6. If you change existing code in the repository, then:
   - For Python, rerun the related Python scripts.
   - For Python and JavaScript, view the visualisations that depend on the changed code, to ensure they look OK.
7. Update [Implementation Details](./Implementation.md) with notes on your visualisation.

When you are ready to contribute your changes, submit a pull request. mikej888 will review the changes and, if OK, merge them.

If changes are pushed to this repository, without going via a pull request, then mikej888 will:

1. Create a new branch with the changes.
2. Delete the changes from the default gh-pages branch.
