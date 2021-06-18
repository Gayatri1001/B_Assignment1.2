# # # # What is purpose of get(), update(), setdefault() methods of dictionary?

# # # # 1. get()
# # # The get() method is used to avoid such situations. This method returns the value for the given key, 
# # # if present in the dictionary. If not, then it will return None (if get() is used with only one argument).

# # # Syntax : Dict.get(key, default=None)

# # # dic = {"A":1, "B":2}
# # # print(dic.get("A"))
# # # print(dic.get("C"))
# # # print(dic.get("C","Not Found ! "))

# # ##2. update()
# # # The update() method takes either a dictionary or an iterable object of key/value pairs (generally tuples).
# # # If update() is called without passing parameters, the dictionary remains unchanged.

# # # d = {1: "one", 2: "three"}
# # # d1 = {2: "two"}

# # # # updates the value of key 2
# # # d.update(d1)
# # # print(d)

# 2.1
# # # d1 = {3: "three"}

# # # # adds element with key 3
# # # d.update(d1)
# # # print(d)

# # d = {'x': 2}

# # d.update(y = 3, z = 0)
# # print(d)

# # 3. setdefault()
# # Dictionary in Python is an unordered collection of data values, used to store data values like a map, 
# # which unlike other Data Types that hold only single value as an element, Dictionary holds key : value pair.
# # In Python Dictionary, setdefault() method returns the value of a key (if the key is in dictionary). If not, it 
# # inserts key with a value to the dictionary.
 

# # # Python program to show working
# # # of setdefault() method in Dictionary
 
# # # Dictionary with single item
# # Dictionary1 = { 'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}
 
# # # using setdefault() method
# # Third_value = Dictionary1.setdefault('C')
# # print("Dictionary:", Dictionary1)
# # print("Third_value:", Third_value)


# # 3.1
# # Python program to show working
# # of setdefault() method in Dictionary
 
# # Dictionary with single item
# Dictionary1 = { 'A': 'Geeks', 'B': 'For'}
 
# # using setdefault() method
# # when key is not in the Dictionary
# Third_value = Dictionary1.setdefault('C')
# print("Dictionary:", Dictionary1)
# print("Third_value:", Third_value)
 
# # using setdefault() method
# # when key is not in the Dictionary
# # but default value is provided
# Fourth_value = Dictionary1.setdefault('D', 'Geeks')
# print("Dictionary:", Dictionary1)
# print("Fourth_value:", Fourth_value)