# # # # # How to access data from dictionary? Key, value and both.
# # # # # 1. using in operator
  
# # # # # initializing dictionary
# # # # test_dict = {"Geeks" : 1, "for" : 2, "geeks" : 3}
  
# # # # # Printing dictionary
# # # # print ("Original dictionary is : " + str(test_dict))
  
# # # # # using in operator to
# # # # # get key and value
# # # # print ("Dict key-value are : ")
# # # # for i in test_dict :
# # # #     print(i, test_dict[i])

# # # # 2. using list comprehension
  
# # # # initializing dictionary
# # # test_dict = {"Geeks" : 1, "for" : 2, "geeks" : 3}
  
# # # # Printing dictionary
# # # print ("Original dictionary is : " + str(test_dict))
  
# # # # using list comprehension to
# # # # get key and value
# # # print ("Dict key-value are : ")
# # # print([(k, test_dict[k]) for k in test_dict])

# # # # 3. using dict.items()
  
# # # # initializing dictionary
# # # test_dict = {"Geeks" : 1, "for" : 2, "geeks" : 3}
  
# # # # Printing dictionary
# # # print ("Original dictionary is : " + str(test_dict))
  
# # # # using dict.items() to
# # # # get key and value
# # # print ("Dict key-value are : ")
# # # for key, value in test_dict.items():
# # #     print (key, value)

# # # # 4. using enumerate()
  
# # # # initializing dictionary
# # # test_dict = {"Geeks" : 1, "for" : 2, "geeks" : 3}
  
# # # # Printing dictionary
# # # print ("Original dictionary is : " + str(test_dict))
  
# # # # using enumerate() to
# # # # get key and value
# # # print ("Dict key-value are : ")
# # # for i in enumerate(test_dict.items()):
# # #     print (i)

# # # 5. 
# # dictA = {1:'Mon',2:'Tue',3:'Wed',4:'Thu',5:'Fri'}
# # #Given dictionary
# # print("Given Dictionary: ",dictA)
# # # Print all keys and values
# # print("Keys and Values: ")
# # for i in dictA :
# #    print(i, dictA[i])

# # 6. # get vs [] for retrieving elements
# my_dict = {'name': 'Jack', 'age': 26}

# # Output: Jack
# print(my_dict['name'])

# # Output: 26
# print(my_dict.get('age'))