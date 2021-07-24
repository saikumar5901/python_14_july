#keys in dictionary
dict = {"Name": 'TANNEERU SAI KUMAR', "Roll No": '69', "College": 'Aurora'}
print("keys Values Items before Dictionary Updation: ")
#Keys in dictionary
keys = dict.keys()
print(keys)


#values in dictionary
values = dict.values()
print(values)


#items in dictionary
items = dict.items()
print(items)

#adding an element to the dictionary
dict.update({"Address": 'Ramanthapur'})
print("\nAfter Dictionary is Updated: ")
print(keys)
print(dict)

#Access Dictionary Items
print("\nAfter Access Dictionary Item: ")
x = dict["Name"]
print(x)
#Changing Dictionary Items
print("\nAfter Changing Dictionary Item: ")
dict["Roll No"] = 22
print(dict)

#Removing Dictionary Items
print("\nAfter Removing Dictionary Item: ")
dict.pop("Address")
print(dict)

#Copying Dictionary
print("\nAfter Copying Dictionary: ")
mydict = dict.copy()
print(mydict)