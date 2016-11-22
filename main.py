# Standard Python library for making an HTTP request like your browser does
import urllib.request

# Standard Python library for parsing CSV contents
import csv

# Do not worry about this for now
import io

# Third-party library for doing the graphing
import matplotlib.pyplot

# You can visit this URL in your browser to see that it is simply a CSV file
url = 'https://www.google.com/finance/historical?q=AAPL&output=csv'

# Make a request to the above URL just like your browser would do
response = urllib.request.urlopen(url)

# Read in the contents of the CSV response
reader = csv.reader(io.TextIOWrapper(response))

# Turn the CSV file data into a Python list to make it easy to operate on it. This list
# is an array of arrays. You can go download the CSV from the URL above then import it into
# Excel or Google Sheets to see what it actually represents.
data_list = list(reader)

# We pop off the first row of the list because it contains the column headers
headers = data_list.pop(0)

# Initialize an array that we are going use to assemble "Close of day" prices
close_price_data = []

# Iterate over each row in the data_list we created earlier
for row_array in data_list:

    # Try / except allows you to execute code that you know might throw an error in order to
    # gracefully do something when that error happens
    try:
        # The "Close of day" price is the fourth element in the array. We will grab it out
        # of the row_array, convert it to a float (it will be a string from when it was read out
        # of the response earlier), then add it to our close_price_data array
        close_price_data.append(float(row_array[3]))
    except ValueError:
        # There could potentially be a dash for a row that does not contain any data. I knew this
        # from when I visually inspected the CSV file in Excel. When you try to convert the dash into
        # a float, Python will not know what to do and thus will throw an error. Here we catch this ValueError
        # and instead just add a zero value to our close_price_data array.
        close_price_data.append(0)

# This is where we leverage the third-party library that we imported, matplotlib. We can hand it our
# close_price_data array then call .show() to make it display a cool graph. You can see where I figured this
# out by visiting the official tutorial on matplotlib's website -- http://matplotlib.org/users/pyplot_tutorial.html
matplotlib.pyplot.plot(close_price_data)
matplotlib.pyplot.ylabel('AAPL Stock Price')
matplotlib.pyplot.show()


'''
References:
    https://www.google.com/finance/historical?q=AAPL&output=csv
    http://matplotlib.org/users/pyplot_tutorial.html
    http://stackoverflow.com/a/16283926/1747491
    http://stackoverflow.com/a/2023920/1747491
    http://stackoverflow.com/a/17912811/1747491
'''