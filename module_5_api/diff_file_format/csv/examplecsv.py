import pandas as pd
import requests
import os

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"
data = requests.get(url)
# print(data.content)

# path = os.path.join(os.getcwd(), 'example.csv')
# with open(path,'wb') as f:
#     f.write(data.content)

# can direclty load like this as well 

# df = pd.read_csv(url, header = None)
# print(df)

df = pd.read_csv('example.csv', header = None)

df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']

# print(df['First Name']). # acessing single col
# print(df[['First Name','Last Name']]) # acessing multiple col

# print(df.loc[0]) # first row
# print(df.loc[[0,2]]) # here use [[]] nesting type of bracket for particular
# print(df.loc[[0,2],['First Name']])


# print(df.iloc[[0,1,2], [0]]) # 3 perosnas first name

# transform

import numpy as np

ndf = pd.DataFrame(np.array([[1,2,3],[3,4,5]]), columns =['a','b','c'])
print(ndf)

new = ndf.transform(func = ['sqrt'])
print(new)