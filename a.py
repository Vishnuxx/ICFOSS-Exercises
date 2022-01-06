# """
# _______SET_______
#    A set is a mutable and unordered datatype 
# """


# a = {'red' , 'green' , 'blue'}           #mutableset 
# b = {'yellow' , 'red' , 'orange'}
# c = set({3 , 3}) #other way of creating a set

# print(a.union(b)) 
# print(a | b)
# print(a.intersection(b))
# print(a.difference(b))
# print(a-b)
# print(b.symmetric_difference(a))

# s = frozenset({'red' , 'green' , 'blue'}) #immutable set
# print(s)


# #____MEMBERSHI OPERATORS_____

# print('red' in a ) #check if the element is present in the set

# #____ BUILTIN FUNCTIONS____
# # len()
# # max()
# # min()
# # sum()


# #_____ACCESS A DATA IN SET ______

# this_set = {"apple" , "banana" , "cherry"}

# # print(this_set[2])   doesnt support indexing

# for x in this_set:
#     print(x)






# """
# _______DICTIONARY______

#  stores key value pairs
# """

# dic = {
#     'name' : 'bob',
#     'age' : 25 ,
#     'job' : 'Dev' , 
#     'city' : 'triv'
# }

# type(dic)

# print(dic)

# # we can convert two value sequence to dictionary
# l = [
#     ('name' , 'james'),
#     ('age' , 3)
# ]
# print(type(l))
# print(dict(l))


# ##____ACCESSING ELEMENTS FROM DICTIONARY__________

# dic = {
#     'name' : 'bob',
#     'age' : 25 ,
#     'job' : 'Dev' , 
#     'city' : 'triv'
# }

# #__get 

# dic.get('age')

# print(dic['age']) #returns error if the key is not present
# #or
# print(dic.get('age')) # returns nothing if the key id not present


# #__pop
# dic.pop('age')

# #__popitem
# dic.popitem()

# #__clear
# dic.clear()
# print(dic)

# #__.fromkeys
# dic.fromkeys(keys)
# dic.fromkeys(keys , values)


#__iteration through dictionry
dic = {
    'name' : 'bob',
    'age' : 25 ,
    'job' : 'Dev' , 
    'city' : 'triv'
}

for i in dic:
    print(i)

len(dic)