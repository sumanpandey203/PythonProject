import numpy as np
import math
import matplotlib.pyplot as plt

cont_value = 2/3
const_sq = math.sqrt(3)/2
#print(const_sq)
theta = math.pi/3
gamma = math.pi*2/3
gamma1 = math.pi*4/3
angle = theta-gamma
angle1 = theta+gamma


    
def volt_adc(digit_Adc1,digit_Adc2,digit_Adc3):
    u_volt1 = digit_Adc1*5/(2**12-1)
    u_volt2 = digit_Adc2*5/(2**12-1)
    u_volt3 = digit_Adc3*5/(2**12-1)
         
    return u_volt1,u_volt2,u_volt3
    
def curr_vc(adcV1,adcV2,adcV3):
    measured_curr1 = (0.8772 *2.5-adcV1)*(52800/61.5) 
    measured_curr2 = (0.8772 *2.5-adcV2)*(52800/61.5) 
    measured_curr3 = (0.8772 *2.5-adcV3)*(52800/61.5) 

    return measured_curr1,measured_curr2,measured_curr3
    
def clark_trans(i1,i2,i3):

    x1 = i1
    x2 = (0.5)*i2
    x3 = 0.5*i3

    y1 = 0*i1
    y2 = const_sq*i2
    y3 = const_sq*i3

    i_alpha = cont_value*(x1-x2-x3)
    i_beta = cont_value*(y1+y2-y3)

#park transformation
    x1_1 = i_alpha*np.cos(theta)
    x2_2 = i_beta*np.sin(theta)

    y1_1 = i_alpha*np.sin(theta)
    y2_2 = i_beta*np.cos(theta)

    i_id = x1_1+x2_2
    q_iq = y2_2-y1_1

    return i_id,q_iq
myvolt1,myvolt2,myvolt3 = volt_adc(180,180,110)
print("my volt =",myvolt1,myvolt2,myvolt3)
print(volt_adc(180,180,111))

mycurrt1,mycurrt2,mycurrt3 =  curr_vc(myvolt1,myvolt2,myvolt3)
print(curr_vc(myvolt1,myvolt2,myvolt3))



myClark1,myClark2 =  clark_trans(mycurrt1,mycurrt2,mycurrt3)
print ("my Current = " ,mycurrt1,mycurrt2,mycurrt3)
print("my park=",clark_trans(mycurrt1,mycurrt2,mycurrt3))

i1_x1 = mycurrt1**2*(math.sin(0)**2 + np.cos(0)**2)
i2_x2 = mycurrt2**2*(np.sin(120)**2 + np.cos(120)**2)
i3_x3 = mycurrt3**2*(np.sin(240)**2 + np.cos(240)**2)


rest_x1 = math.sqrt(i1_x1)
rest_x2 = math.sqrt(i2_x2)
rest_x3 = math.sqrt(i3_x3)

res_total = rest_x1 + rest_x2 + rest_x3

print("my vector sum =", res_total )
# myvolt_cal1,myvolt_cal2,myvolt_cal3 = myCalTask.volt_adc(180,180,111)

# print("my volt from digit = ",myvolt_cal1, myvolt_cal2, myvolt_cal3)

# mycurrent1,mycurrent2,mycurrent3 = myCalTask.curr_vc( myCalTask.curr_vc(myvolt_cal1,myvolt_cal2,myvolt_cal3))

# print("my volt from digit = ",mycurrent1,mycurrent2,mycurrent3)

# myClark1,myClark2,myClark3 = myCalTask.clark_trans(mycurrent1,mycurrent2,mycurrent3 )
# print("my volt from digit = ",myClark1,myClark2,myClark3)
   

# def my_dqCal(I1,I2,I3):
#     x1 = I1*np.cos(theta)
#     x2 = I2*np.cos(angle)
#     x3 = I3*np.cos(angle1)

#     y1 = I1*np.sin(theta)
#     x2 = I2*np.sin(angle)
#     y3 = I3*np.sin(angle1)

#     dq_Id = 2/3*(x1+x2+x3)
#     dq_Iq = 2/3*(-y1-y1-y3)
  
#     plt.plot(dq_Id, dq_Iq) 

#     # naming the x axis 
#     plt.xlabel('x - axis') 
#    # plt.xscale('Log')
# # naming the y axis 
#     plt.ylabel('y - axis') 
#    # plt.yscale('Log')
  
# # giving a title to my graph 
#     plt.title('Dq-Calculation!') 
  
# # function to show the plot 
#     plt.grid(True)
#     plt.show() 

#     return dq_Id,dq_Iq

# print( my_dqCal(-20,-30,60))


