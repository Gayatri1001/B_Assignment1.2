# # # # # #Write a program to find number of occurences of each character of each letter 
# # # # # # present in the given string? 

# # # # # # 1. naive method 
  
# # # # # # initializing string 
# # # # # # test_str = "GeeksforGeeks"
  
# # # # # # # using naive method to get count 
# # # # # # # of each element in string 
# # # # # # all_freq = {}
  
# # # # # # for i in test_str:
# # # # # #     if i in all_freq:
# # # # # #         all_freq[i] += 1
# # # # # #     else:
# # # # # #         all_freq[i] = 1
  
# # # # # # # printing result 
# # # # # # print ("Count of all characters in GeeksforGeeks is :\n " +  str(all_freq))

# # # # # # 2. collections.Counter()
# # # # # from collections import Counter
  
# # # # # # initializing string 
# # # # # test_str = "GeeksforGeeks"
  
# # # # # # using collections.Counter() to get 
# # # # # # count of each element in string 
# # # # # res = Counter(test_str)
  
# # # # # # printing result 
# # # # # print ("Count of all characters in GeeksforGeeks is :\n " +  str(res))

# # # # # 3. dict.get()
  
# # # # # initializing string 
# # # # test_str = "GeeksforGeeks"
  
# # # # # using dict.get() to get count 
# # # # # of each element in string 
# # # # res = {}
  
# # # # for keys in test_str:
# # # #     res[keys] = res.get(keys, 0) + 1
  
# # # # # printing result 
# # # # print ("Count of all characters in GeeksforGeeks is : \n"
# # # #                                              +  str(res))

# # # # 4.  set() + count()
  
# # # # initializing string 
# # # test_str = "GeeksforGeeks"
  
# # # # using set() + count() to get count 
# # # # of each element in string 
# # # res = {i : test_str.count(i) for i in set(test_str)}
  
# # # # printing result 
# # # print ("The count of all characters in GeeksforGeeks is :\n "
# # #                                                +  str(res))

# # # 5. # initializing string 
# # inp_str = "GeeksforGeeks"
  
# # # using set() + count() to get count 
# # # of each element in string 
# # out = {x : inp_str.count(x) for x in set(inp_str )} 
  
# # # printing result 
# # print ("Occurrence of all characters in GeeksforGeeks is :\n "+ str(out)) 

# # 6. Using dict.
# # initializing string 
# inp_str = "GeeksforGeeks"
  
# # frequency dictionary
# freq = {} 
    
# for ele in inp_str: 
#     if ele in freq: 
#         freq[ele] += 1
#     else: 
#         freq[ele] = 1
    
# # printing result  
# print ("Occurrence of all characters in GeeksforGeeks is :\n "+ str(freq)) 