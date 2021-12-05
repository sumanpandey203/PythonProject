
# importing the required module
import numpy as np
import matplotlib.pyplot as plt
y_cal = 4.7/52.7
my_list =[]
my_list1 =[]

x_chord = range(0,49)
x_chord1 = range(49,1000)

my_list = [y_cal*x for x in x_chord]
my_list1 = [my_list[-1] for x in x_chord1]

print(*my_list, sep = ',' )
#print(*my_list, sep ="\n")

plt.plot(x_chord, my_list) 
plt.plot(x_chord1, my_list1)  
# naming the x axis 
plt.xlabel('x - axis') 
plt.xscale('Log')
# naming the y axis 
plt.ylabel('y - axis') 
plt.yscale('Log')
  
# giving a title to my graph 
plt.title('U_Kl30_Calculation!') 
  
# function to show the plot 
plt.grid(True)
plt.show() 

print(my_list)


    