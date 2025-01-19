#Dictionaries are used to store data valules as key:value pairs in python
#They are unordered, mutable and don't allow duplicate keys.
#basic dictionary
# dict = {
#     "name": "Abdulla",
#     "age": 25,
#     "city": "New York",
#     "occupation": "Software Engineer",
#     "isSingle": True,
# }
# print(dict["name"])
# dict["name"] = "Topu"
# print(dict["name"])     

# dictionary with nested dictionaries

# myDict = {
#     "name": "John",
#     "age": 25,
#     "address": {
#         "street": "123 Main St",
#         "city": "New York",
#         "state": "NY"
#     },
#     "hobbies": ["realllding", "painting", "cooking"]
# }
# myDictProperty = myDict.get("address").get("street")

# print(myDictProperty)

#Dictionary methods

# dict = {
#     "name": "Abdulla",
#     "age": 25,
#     "city": "New York",
#     "occupation": "Software Engineer",
#     "isSingle": True,
# }

# print(dict.keys())

# print(dict.values())

# print(dict.items())


# typeOfOcc = type(dict.get("occupation"))
                 
# print(typeOfOcc)

# print(dict.get("occupation"))

dict = {
    "name": "Abdulla",
    "age": 25,
    "city": "New York",
    "occupation": "Software Engineer",
    "isSingle": True,
}

newDict = {
    "name" : "Topu", 
    "age" : 27,
    "city" : "Seattle",
    "occupation" : "Project Manager",


}

dict.update(newDict)

print(dict)