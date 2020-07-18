
#-----------(1)------------
#Write a Python script to sort (ascending and descending) a dictionary by value.

# import operator
#
# d = {1:3,6:2,7:1,0:0,5:8,9:2}
#
# sorted_d = dict(sorted(d.items(),key= operator.itemgetter(1)))
# print('Dictionary in ascending order by value:',sorted_d)
#
# sorted_d = dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
# print('Dictionary in Descending order by value:',sorted_d)

#<<--------------------------------------------------------------------->>
#------------(2)------------------
#Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}


# d = {0:10,1:20}
#
# d.update({2:30})
# print(d)

#<<---------------------------------------------------------------->>
#--------------(3)----------------
# Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dict4 = {}
#
# for i in (dic1,dic2,dic3):
#     dict4.update(i)
# print(dict4)

#<<------------------------------------------------------------------->>
#------------------(4)-----------------------
#Write a Python script to check whether a given key already exists in a dictionary.

#<<---------------ONE METHOD--------------------->>

# dict1 = {
#     'name': 'kamran',
#     'age': 24,
#     'location': 'Bangalore'
# }
#
# if 'name' in dict1:
#     print('present')
# else:
#     print('Not present')

#<<-----------------SECOND METHOD--------------------->>

# d = {1:10,2:20,3:30,4:40,5:50,6:60,7:70}
#
# def check_key(key):
#     if key in d:
#         print('Present')
#     else:
#         print('Not Present')
#
# check_key(5)
# check_key(10)


#<<---------------------------------------------------->>
#-----------(5)--------------
#Write a Python program to iterate over dictionaries using for loops.

# d = {1:10,2:20,3:30,4:40,5:50,6:60,7:70}
#
# for key,value in d.items():
#     print(key,'------',value)

#<<--------------------------------------------------------->>
#------------------(6)-------------
#Write a Python script to generate and print a dictionary that contains a number
# (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# n = int(input('Enter the number: '))
# dict = {}
#
# for i in range(1,n + 1):
#     dict[i] = i**2
# print(dict)

#<<-------------------------------------------------------->>
#---------------(7)-------------
#Write a Python program to sum all the items in a dictionary.

# d = {1:10,2:20,3:30,4:40}
#
# print(sum(d.values()))

#<<------------------------------------------------------->>
#---------------(8)--------------
#Write a Python program to multiply all the items in a dictionary.

# d = {1:10,2:20,3:30,4:40}
#
# result = 1
#
# for key in d:
#     result = result * d[key]
# print(result)

#<<-------------------------------------------------------->>
#-------------(9)-------------
#Write a Python program to remove a key from a dictionary.

# d = {1:10,2:20,3:30,4:40}

# d.pop(1)
# print(d)
#
# if 2 in d:
#     del d[2]
# print(d)


#<<----second method------->>
# def remove_key(dic,target):
#     for i in list(dic):
#         if i == target:
#             dic.pop(i)
#     return dict(dic)
#
# dic = {1:3,6:9,4:50,3:9}
# target = int(input('Enter the target: '))
# print(remove_key(dic,target))

#<<--------------------------------------------------------->>
#---------------(10)---------------
# Write a Python program to map two lists into a dictionary.

# key = ['red','blue','green','black']
# value = ['aisha','ruhi','imran','kamran']
#
# detail = dict(zip(key,value))
# print(detail)
# print(type(detail))

#<<<--------SECOND METHOD--------------->>>
# keys = ['red', 'green', 'blue']
# values = ['#FF0000','#008000', '#0000FF']
# lst = []
# for i in range(len(keys)):
#     lst.append((keys[i],values[i]))
# print(dict(lst))


#<<----------------------------------------------------->>
#----------------(11)---------------
#Write a Python program to get the maximum and minimum value in a dictionary.

# d = {'x':500,'y':583,'z':800}
#
# key_max = max(d.keys())
# key_min = min(d.keys())
#
# print('Maximum value:',d[key_max])
# print('Minimum value:',d[key_min])

#<<-------------------------------------------------------------->>
#---------------(12)--------------
#Write a Python program to remove duplicates from Dictionary.

# student_data = {
#     'st1':{
#         'name': 'kamran',
#         'age': 24,
#         'location': 'Bangalore'
#     },
#     'st2': {
#
#         'name': 'kamran',
#         'age': 24,
#         'location': 'Bangalore'
#
#     },
#     'st3': {
#         'name': 'aisha',
#         'age': 23,
#         'location': 'Delhi'
#     },
#     'st4': {
#         'name': 'ruhi',
#         'age': 28,
#         'location': 'Rath'
#     }
# }
#
# print(student_data)
#
# result = {}
#
# for key,value in student_data.items():
#     if value not in result.values():
#         result[key] = value
# print(result)

#<<------------------------------------------------------------>>
#--------------(13)---------------
#Write a Python program to check a dictionary is empty or not.

# d = {'x':500,'y':583,'z':800}
#
# if not bool(d):
#     print('Dictionary is empty')
# else:
#     print('Dictionary is not empty')

#<<--------------------------------------------------------->>
#----------------(14)----------------

#Write a Python program to combine two dictionary adding values for common keys.
#d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})


# from collections import Counter
#
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
#
# d3 = Counter(d1) + Counter(d2)
# print(d3)


#<<---------------------------------------->>

#Write a Python program to create a dictionary of keys x, y,
# and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary. Go to the editor
# {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# 15
# 25
# 35
# x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
# y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
# z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]


# from pprint import pprint
#
# dict_nums = dict(x = list(range(11,20)),y = list(range(20,30))
#                  ,z = list(range(30,40)))
#
#
# pprint(dict_nums)
# print(dict_nums['x'][4])
# print(dict_nums['y'][4])
# print(dict_nums['z'][4])
#
#
# for key,value in dict_nums.items():
#     print(key,'has value:',value)

# print('x has value',dict_nums['x'])
# print('y has value',dict_nums['y'])
# print('z has value',dict_nums['z'])


#<<------------------------------------>>

#Write a Python program to match key values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y

# d1 = {'key1': 1, 'key2': 3, 'key3': 2}
# d2 = {'key1': 1, 'key2': 2}
# d3={}
# for i,j in d1.items():
#     for x,y in d2.items():
#         if i ==x and j==y:
#             d3[i]=j
# print('match key and value:',d3)


#<<------------------------------------------>>

#  Write a Python program to sort Counter by value.
# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]







