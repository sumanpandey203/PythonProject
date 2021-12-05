import numpy as np
import matplotlib.pyplot as plt

y_cal = 1
gamma = 120
theta_0 = range(360)
list_of_gamma = [gamma for j in range(360)]

theta = [y_cal for x in theta_0]

x1 = []
x2 = []
x3 = []
y1 = []
y2 = []
y3 = []
angle = []
angle1 = []

angle = list (np.array(theta_0)-np.array(list_of_gamma))
angle1 = list (np.array(theta_0)+np.array(list_of_gamma))
#print (angle1)

def my_dqCal(I1,I2,I3):
    x1 = I1*np.cos(theta)
    x2 = I2*np.cos(angle)
    x3 = I3*np.cos(angle1)

    y1 = I1*np.sin(theta)
    x2 = I2*np.sin(angle)
    y3 = I3*np.sin(angle1)

    dq_Id = 2/3*(x1+x2+x3)
    dq_Iq = 2/3*(-y1-y1-y3)
    
    #print(f" {dq_Id}, {dq_Iq} ")
    print(dq_Id , "," , dq_Iq)


    plt.plot(dq_Id, dq_Iq) 

    # naming the x axis 
    plt.xlabel('x - axis') 
   # plt.xscale('Log')
# naming the y axis 
    plt.ylabel('y - axis') 
   # plt.yscale('Log')
  
# giving a title to my graph 
    plt.title('Dq-Calculation!') 
  
# function to show the plot 
    plt.grid(True)
    plt.show() 

    return dq_Id,dq_Iq
yx = my_dqCal(2,3,4)
#print( my_dqCal(2,3,4))

