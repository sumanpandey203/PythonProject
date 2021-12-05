import urllib
import pandas as pd
from bs4 import BeautifulSoup

url = "file:///C:/Users/suman.pandey/Desktop/My_work/Customer_input/safetycontroller-aurix_docs/doxygen_docu/html/_l_l_r.html"
#csv_save_path =r"c:\Wiki_html_to_csv.csv"
csv_save_path = r"C:\Users\suman.pandey\Desktop\My_work\Pyth\dataTest.csv"
headline_section = "a"
headline_class = "el"
extract_tags = ["p","li"]
#data_sep = "\n"
data_sep = ","

client = urllib.request.urlopen(url)
soup = BeautifulSoup(client, 'html.parser')

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
            # If next sibling is not 'tag_name', tag = None 
            tag = tag.find_next_sibling(tag_name)
    # Append data to dataframe only if section_data is not empty
    if section_data:
        description = data_sep.join(section_data)
        data_df = data_df.append({"Title": title, "Description": description}, ignore_index=True)
data_df

data_df.to_csv(csv_save_path, index=False)

