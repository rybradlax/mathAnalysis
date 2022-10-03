# mathAnalysis

corrAnalysis.py
This program enables you to import two datasets and derive correlational coefficient from them as well as produce a graph containing the relevant data.

USAGE
Define corrAnalysis object containing an array (list or tuple), another array (list or tuple) of data to compare (they must be of the same length), a label for the x axis (second array) and y axis (first array) in string form.

run the chart() function on this object and it will display a chart of the values and their correlational coefficient with the relevant labels and title (xlabel v. ylabel).

You can also access the other functions (mean, correlationCoefficient) to return the means of each array and their coefficient and store them as variables.


bladFinance.py
This program enables you to gather yield curve data over a certain time frame from the U.S. Treasury.

USAGE


Run getDailyTreasuryInterestRates(monthYear, toPresent) and input a boolean for toPresent to determine whether you want it to gather and compile data from the selected timeframe to the present day, inputing a string in yyyymm (int) format with toPresent declared as false (cannot input true if gathering monthly data) will gather data for the selected month in each day, inputting a year in yyyy (int) format will gather data for an entire year for each day, if toPresent is true it will gather data for each year up until the present day and compile it into the dataframe.

Returns a pandas dataframe.
