import random
min = 1
max = 6
roll_again = "yes"

while roll_again == "yes": 

    print ("Rolling the dice")
    print ("The values are....")
    print (random.randint(min,max))
    print(random.randint(min,max)) 

    roll_ = input("rollthe dice again=")
    roll_again = roll_