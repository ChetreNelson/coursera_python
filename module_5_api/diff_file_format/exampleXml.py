
import pandas as pd
import requests

import xml.etree.ElementTree as etree

# url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Sample-employee-XML-file.xml"
# data = requests.get(url)

# with open('dummyxml.xml','wb') as f:
#     f.write(data.content)


# reading the file using etree 

tree = etree.parse('dummyxml.xml')
root = tree.getroot()

columns = ["firstname", "lastname", "title", "division", "building", "room"]
dataframe = pd.DataFrame(columns=columns)

for node in root:
    firstname = node.find("firstname").text
    lastname = node.find("lastname").text
    title = node.find("title").text
    division = node.find("division").text
    building = node.find("building").text
    room = node.find("room").text
    # Create a DataFrame for the current row
    row_df = pd.DataFrame([[firstname, lastname, title, division, building, room]], columns=columns)
    dataframe = pd.concat([dataframe, row_df],ignore_index = True)
# print(dataframe)


# easy method using panda but first have to install the xml parser recommended lxml
file = pd.read_xml('dummyxml.xml', xpath = '/employees/details')
print(file)

dataframe.