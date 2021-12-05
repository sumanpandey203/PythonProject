
# printing result  
x = 5
y = int(5)
a=b=c ='Same'
print(a)

print([] is [])
print(10 is 10.0)
print(10 == 10.0)
print("hello" == 'hello')
print("hello" is 'hello')

name = ' asmita '
suman = name.upper()
print(suman)
print(name.strip())
print('Suman'[0])

user = {'Asmita':22,'suman':32, 'relation': 'couple'}

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for x in picture:
    for y in x:
        if y == 1 :
            print("*",end = '')
            
        else:
            print("_",end = '')

    print('')


def checkHig_Even(a):
    ''' Info checking the highest even no from the List  '''
    evenList = []
    for y in a:
        if y % 2 == 0:
            evenList.append(y)
            
    print(evenList)  
    print(len(evenList)) 
    print(f'highest even no is {max(evenList)} from the list {a}')   
   
checkHig_Even([10,2,3,4,8,11])

def mult_2 (listof2):
    nullList =[]
    for x in listof2:
        nullList.append(x*2)
    return nullList

def multByMap_2(item):
    return item*2

my_list =[1,2,3]
your_list = [10,20,30]

zip1 = zip(my_list,your_list)

print(list(zip1))
for y,x in zip(my_list,your_list):
    print(y)
    print(x)

print(type(zip1))

print('with normal process=', mult_2([1,2,3]))
print(list (map(multByMap_2,[1,2,3])))