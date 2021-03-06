# # # # # # # How to delete element from dictionary?
# # # # # # # 1. using del
  
# # # # # # # Initializing dictionary
# # # # # # test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}
  
# # # # # # # Printing dictionary before removal
# # # # # # print ("The dictionary before performing remove is : " + str(test_dict))
  
# # # # # # # Using del to remove a dict
# # # # # # # removes Mani
# # # # # # del test_dict['Mani']
  
# # # # # # # Printing dictionary after removal
# # # # # # print ("The dictionary after remove is : " + str(test_dict))
  
# # # # # # # Using del to remove a dict
# # # # # # # raises exception
# # # # # # del test_dict['Manjeet']

# # # # # # 2. using pop()
  
# # # # # # Initializing dictionary
# # # # # test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}
  
# # # # # # Printing dictionary before removal
# # # # # print ("The dictionary before performing remove is : " + str(test_dict))
  
# # # # # # Using pop() to remove a dict. pair
# # # # # # removes Mani
# # # # # removed_value = test_dict.pop('Mani')
  
# # # # # # Printing dictionary after removal
# # # # # print ("The dictionary after remove is : " + str(test_dict))
# # # # # print ("The removed key's value is : " + str(removed_value))
  
# # # # # print ('\r')
  
# # # # # # Using pop() to remove a dict. pair
# # # # # # doesn't raise exception
# # # # # # assigns 'No Key found' to removed_value
# # # # # removed_value = test_dict.pop('Manjeet', 'No Key found')
  
# # # # # # Printing dictionary after removal
# # # # # print ("The dictionary after remove is : " + str(test_dict))
# # # # # print ("The removed key's value is : " + str(removed_value))

# # # # # 3. Python code to demonstrate
# # # # # removal of dict. pair 
# # # # # using items() + dict comprehension
  
# # # # # Initializing dictionary
# # # # test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}
  
# # # # # Printing dictionary before removal
# # # # print ("The dictionary before performing remove is : " + str(test_dict))
  
# # # # # Using items() + dict comprehension to remove a dict. pair
# # # # # removes Mani
# # # # new_dict = {key:val for key, val in test_dict.items() if key != 'Mani'}
  
# # # # # Printing dictionary after removal
# # # # print ("The dictionary after remove is : " + str(new_dict))

# # # # 4.
# # # thisdict =	{
# # #   "brand": "Ford",
# # #   "model": "Mustang",
# # #   "year": 1964
# # # }
# # # thisdict.popitem()
# # # print(thisdict) 

# # # 5. 
# # thisdict =	{
# #   "brand": "Ford",
# #   "model": "Mustang",
# #   "year": 1964
# # }
# # thisdict.clear()
# # print(thisdict) 

# # 6. 
# # create a dictionary
# squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# # remove a particular item, returns its value
# # Output: 16
# print(squares.pop(4))

# # Output: {1: 1, 2: 4, 3: 9, 5: 25}
# print(squares)

# # remove an arbitrary item, return (key,value)
# # Output: (5, 25)
# print(squares.popitem())

# # Output: {1: 1, 2: 4, 3: 9}
# print(squares)

# # remove all items
# squares.clear()

# # Output: {}
# print(squares)

# # delete the dictionary itself
# del squares