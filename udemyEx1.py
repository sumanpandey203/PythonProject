from functools import reduce#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize(string):
    return string.upper()

print(list(map(capitalize, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def is_smart_student(score):
    return score > 50

print(list(filter(is_smart_student, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, (my_numbers + scores)))

myList = [5,3,4]
print(list(map(lambda num: num**2,myList)))

mySort =[(0,2),(9,9),(4,3),(10,-1)]
# mySort.sort()
# print(mySort)

(mySort.sort(key=lambda x: x[1]))
print(mySort)

some_List = ['a','b','c','b','d','m','n','n']
dublicate = []


dublicate = list(set([num for num in some_List if some_List.count(num) >1 ]))
set_dub = set(dublicate)
print(dublicate)
#print(set_dub)

def hello():
    
    return ('helloooo')

greet = hello

print(hello())

print('testing is done ',greet())