import urllib
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date
import datetime
import re


# Reading an excel file using Python 
import xlrd
outFileName = ""

function_pattern='Global\s*(\S*)'
#function_pattern_class ='Class\s*(\S*)'
description_pattern='LLR-\w+\s'
# arg_url = "file:///C:/Users/suman.pandey/Desktop/My_work/Customer_input/safetycontroller-aurix_docs/doxygen_docu/html/_l_l_r.html"
arg_url = "file:///C:/Users/suman.pandey/Desktop/My_work/Customer_input/doxygen/html/_l_l_r.html"
def getFilenameWithTimeStamp(inpFileName):
    tempString  = str(datetime.datetime.now().strftime("%y-%d-%m_%H%M%S_")) + inpFileName  
    print ("Output Filename :: " +  tempString)    
    return tempString

def flatExcel2TreeExcel(inoutExcelFilename):
    
    inoutExcelFile = xlrd.open_workbook(inoutExcelFilename)    
    sheet = inoutExcelFile.sheet_by_index(0)
    print (sheet.nrows)
    print (sheet.ncols)
    
    #Scanning the Excel rows and columns
    #for i in range( sheet.nrows):
    #    for j in range( sheet.ncols):
    #        print (sheet.cell_value(i,j) )

#Extract only the function name ignoring the Global and post paranthesis with arguments
def getLLRtitle(title):
    rawTitle = regex_title.split(title)
    myTitle= ""
    if len(rawTitle)==3:
        myTitle=rawTitle[1]
    return myTitle

#Extract only the function name ignoring the Global and post paranthesis with arguments Suman


def getLLRDescription(description):
    rawDescription = regex_description.split(description)
    myDescription= ""
    if len(rawDescription)==2:
        myDescription=rawDescription[1]
    return myDescription

def html2excel(url, csv_save_path) :    
    
    outFileHandle= open(outFileName,"w+")

    headline_section = "dt"
    headline_class = None
    extract_tags = ["dd"]
    data_sep = "\n"

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
                break
                # If next sibling is not 'tag_name', tag = None 
                tag = tag.find_next_sibling(tag_name)
        # Append data to dataframe only if section_data is not empty
        if section_data:
            description = data_sep.join(section_data)
            #Extract only the function name ignoring the Global and post paranthesis with arguments           
            data_df = data_df.append({"Title": getLLRtitle(title), "Description": getLLRDescription(description)}, ignore_index=True)
            
    data_df
    #data_df.to_xlsx(csv_save_path, index=False)
    data_df.to_excel(outFileName, index=False)
    outFileHandle.close()
    return

#URL is input argument 1
#output filename is argument 2


#arg_csv_save_path = r"C:\Users\suman.pandey\Desktop\My_work\Pyth\dataLLR.xlsx"

#Assign the filename suffix , rest is timestamp only
arg_csv_save_path = "KatLLR.xlsx"

print ("Starting Program......")

#Create the filename with timestamp so it is unique
outFileName = getFilenameWithTimeStamp(arg_csv_save_path)

#Allocate the regular expression
regex_title = re.compile(function_pattern)
regex_description = re.compile(description_pattern)

#Convert HTML LLR to Excel with Title and Description ONLY
html2excel(arg_url, arg_csv_save_path)

#Convert the above EXCEL and add Filename and Modulename info as 3rd and 4th column
flatExcel2TreeExcel(outFileName)


print ("DONE---------->Html LLR converted to Excel")


