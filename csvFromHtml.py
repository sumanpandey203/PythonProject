import urllib
import pandas as pd
from bs4 import BeautifulSoup
import csv

url = "file:///C:/Users/suman.pandey/Desktop/My_work/Customer_input/safetycontroller-aurix_docs/doxygen_docu/html/_l_l_r.html"
#csv_save_path =r"c:\Wiki_html_to_csv.csv"
csv_save_path = r"C:\Users\suman.pandey\Desktop\My_work\Pyth\data1.csv"

client = urllib.request.urlopen(url)
soup = BeautifulSoup(client, 'html.parser')



# Step 3: Analyze the HTML tag, where your content lives
# Create a data dictionary to store the data.
data = {}
#Get the table having the class el
gdp_table = soup.find("a", attrs={"class": "el"})
gdp_table_data = gdp_table.find_all("el")  # contains 2 rows

# Get all the headings of Lists
headings = []
for td in gdp_table.find_all("anchor"):
    # remove any newlines and extra spaces from left and right
    headings.append(td.b.text.replace('\n', ' ').strip())

# Get all the 3 tables contained in "gdp_table"
for table, heading in zip(gdp_table.find_all("a"), headings):
    # Get headers of table i.e., Rank, Country, GDP.
    t_headers = []
    for th in table.find_all("el"):
        # remove any newlines and extra spaces from left and right
        t_headers.append(th.text.replace('\n', ' ').strip())
    
    # Get all the rows of table
    table_data = []
    for tr in table.tbody.find_all("anchor"): # find all tr's from table's tbody
        t_row = {}
        # Each table row is stored in the form of
        # t_row = {'Rank': '', 'Country/Territory': '', 'GDP(US$million)': ''}

        # find all td's(3) in tr and zip it with t_header
        for td, th in zip(tr.find_all("anchor"), t_headers): 
            t_row[th] = td.text.replace('\n', '').strip()
        table_data.append(t_row)

    # Put the data for the table with his heading.
    data[heading] = table_data
print(data)

# Step 4: Export the data to csv
"""
For this example let's create 3 seperate csv for 
3 tables respectively
"""
for topic, table in data.items():
    # Create csv file for each table
    with open(f"{topic}.csv", 'w') as out_file:
        # Each 3 table has headers as following
        headers = [ 
            "Title",
            "Description",
            "LLR ID"
        ] # == t_headers
        writer = csv.DictWriter(out_file, headers)
        # write the header
        writer.writeheader()
        for row in table:
            if row:
                writer.writerow(row)

print("hello asmita")