import requests
import os
# url='https://www.ibm.com/'

# GET requests
# r = requests.get(url)
# print(r.status_code).  # 200 


# downloading image 
# url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
# path = os.path.join(os.getcwd(), 'image.png')
# r = requests.get(url)
# with open(path,'wb') as f:
#     f.write(r.content)
# downloading txt file from the given link

# url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
# path=os.path.join(os.getcwd(),'example1.txt')
# r=requests.get(url)
# with open(path,'wb') as f:
#     f.write(r.content)


# GET requests with url parameters
base_url = 'http://httpbin.org/get'
payload = {
    'name':'Nelson',
    'age':24
}

request = requests.get(base_url, params = payload)
# print(request.url) #http://httpbin.org/get?name=Nelson&age=24
# print(request.json())
# print(request.text)
# print(request.body) 

#---------------------------------------------------------------------#


# POST requests in python

url_post='http://httpbin.org/post'
payload = {
    'name':'Nelson',
    'age':24
}

req = requests.post(url_post, data = payload)
# print(req.request.body)
print(req.json()['form'])  # {'age': '24', 'name': 'Nelson'}. <='form': {'age': '24', 'name': 'Nelson'}