# An international firm that is looking to expand its business
#  in different countries across the world has recruited you. You have 
#  been hired as a junior Data Engineer and are tasked with creating a script that can extract the 
#  list of the top 10 largest economies of the world in descending order
#   of their GDPs in Billion USD (rounded to 2 decimal places), as logged by the International Monetary Fund (IMF).


import numpy as np 
import pandas as pd

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

URL="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

table = pd.read_html(URL)
df = table[3]

df.columns = range(df.shape[1])
df = df[[0,2]]
df = df.iloc[1:11,:]
df.columns = ['Country','GDP']

df['GDP'] = df['GDP'].astype(int)
df['GDP'] = np.round(df['GDP']/1000,2)
df.rename(columns = {'GDP' : 'GDP (Billion USD)'}, inplace = True)

# df.rename(columns = {'GDP' : 'GDP ( in billions USD)'})
df.to_csv('./largest_economics.csv')
print(df)
val='1,2,3,4'.split(',')
print(val)