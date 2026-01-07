import pandas as pd
x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}
df = pd.DataFrame(x)
# print(df)

#accessing coloumns
id_column = df[['ID']]
# print(id_column)

# accessing mulitple columns
multi_columns = df[['Name','Department']]
# print(multi_columns)



## creating a data frame 

a = {
    'Student': ['David','Samule','Terry','Evan'], 'Age': [27, 24, 22, 32], 
    'Country': ['Uk', 'Canda', 'China', 'Usa']
}

user_info = pd.DataFrame(a)
# print(user_info)

#retriving its columns
name_age = user_info[['Student','Age']]
# print(name_age)

#viewing in series
in_series = user_info['Student']
# print(in_series)

# aceesing using loc and iloc 
# print(user_info.iloc[0,1]) #27 here iloc takes index
# print(user_info.loc[0,'Age']) #27 here loc takes labels


# slicing particular datas
print(user_info.loc[0:2,'Student':'Country']) # print 3 user with  col Student to country
print(user_info.iloc[0:2, 1:3]) #print 2 users with age to country