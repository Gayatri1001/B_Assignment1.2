# How to iterate backward? E.g to print upto 6.
# Like 6,5,4,3,2,1.
# How we can iterate backward on list?

#1. using reversed()
  
# # Initializing number from which 
# # iteration begins 
# N = 6
  
# # using reversed() to perform the back iteration
# print ("The reversed numbers are : ", end = "")
# for num in reversed(range(N + 1)) :
#     print (num, end = " ")

# ##OUTPUT##
# # The reversed numbers are : 6 5 4 3 2 1 0 

# #2. using range(N, -1, -1)
  
# # Initializing number from which 
# # iteration begins 
# N = 6
  
# # using reversed() to perform the back iteration
# print ("The reversed numbers are : ", end = "")
# for num in range(N, -1, -1) :
#     print (num, end = " ")

