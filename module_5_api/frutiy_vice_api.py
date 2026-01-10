import requests
import pandas as pd
base_url = "https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all"
get_req = requests.get(base_url)
# print(get_req.json())

# df1 = pd.DataFrame(get_req.json())
# print(df1)

# to flatened the sub dict 
df2 = pd.json_normalize(get_req.json())
print(df2)

# can drop the column as well
df2.drop(columns=['family'],inplace = True)
print(df2)