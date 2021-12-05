import urllib
import pandas as pd
from bs4 import BeautifulSoup

url = "file:///C:/Users/suman.pandey/Desktop/My_work/Customer_input/doxygen/html/_l_l_r.html"
#csv_save_path =r"c:\Wiki_html_to_csv.csv"
csv_save_path = r"C:\Users\suman.pandey\Desktop\My_work\Pyth\dataLLR1.xlsx"
headline_section = "dt"
headline_class = None
extract_tags = ["dd"]
data_sep = "\n"

client = urllib.request.urlopen(url)
soup = BeautifulSoup(client, 'html.parser')

#row = soup.find('li')
#print(row)

data_df = pd.DataFrame(columns=["Title", "Description"])
headlines = soup.find_all(headline_section, class_=headline_class)
for headline in headlines:
    section_data = []
    title = headline.text
    for tag_name in extract_tags:
        tag = headline.find_next(tag_name)
        # Loop while tag = something other than None
        while tag:
            section_data.append(tag.text)
            break
            # If next sibling is not 'tag_name', tag = None 
            tag = tag.find_next_sibling(tag_name)
    # Append data to dataframe only if section_data is not empty
    if section_data:
        description = data_sep.join(section_data)
        data_df = data_df.append({"Title": title, "Description": description}, ignore_index=True)
data_df
#data_df.to_xlsx(csv_save_path, index=False)
data_df.to_excel(csv_save_path, index=False)

