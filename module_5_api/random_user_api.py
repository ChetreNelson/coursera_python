from randomuser import RandomUser
import pandas as pd


r = RandomUser()
random_user_list = r.generate_users(10)
# print(random_user_list)
# for user in random_user_list:
#     print("Name: ",user.get_full_name() ,"Email :", user.get_email())

users = []
for user in random_user_list:
    users.append({"Name":user.get_full_name(), "Email":user.get_email(), "Gender":user.get_gender()})
table = pd.DataFrame(users)
print(table). # visualizing data in table using dataframe

# random_user_api has following methods
# get_cell()
# get_city()
# get_dob()
# get_email()
# get_first_name()
# get_full_name()
# get_gender()
# get_id()
# get_id_number()
# get_id_type()
# get_info()
# get_last_name()
# get_login_md5()
# get_login_salt()
# get_login_sha1()
# get_login_sha256()
# get_nat()
# get_password()
# get_phone()
# get_picture()
# get_postcode()
# get_registered()
# get_state()
# get_street()
# get_username()
# get_zipcode()