import json
person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}


# using dump to save the json as file

# with open('person.json','w') as f:
#     json.dump(person,f)


# using dumps which first get as json object and we can write that to the file
# json_object = json.dumps(person, indent = 4)
# with open('person.json','w') as f:
#     f.write(json_object)
# print(json_object)


# reading json file

with open('person.json','r') as f:
    json_obj = json.load(f)

print(json_obj)