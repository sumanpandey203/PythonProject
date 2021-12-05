import math
import numpy as np
import matplotlib.pyplot as plt

MQ11 = 0.2064
MQ12 = 0.2423
MQ21 = 0.2193
MQ22 = 0.2563

LD11 = 0.000636
LD12 = 0.0006185
LD21 = 0.0006335
LD22 = 0.000616

# LD11 = -1704
# LD12 = -1667
# LD21 = -1633
# LD22 = -1594

LQ11 = -2217
LQ12 = -2151
LQ21 = -2162
LQ22 = -2095

def magnetic_flux(X1,Y1,X,Y,X2,Y2,):
    A1 = ((X2-X)*(Y2-Y))/((X2-X1)*(Y2-Y1))
    A2 = ((X-X1)*(Y2-Y))/((X2-X1)*(Y2-Y1))
    A3 = ((X2-X)*(Y-Y1))/((X2-X1)*(Y2-Y1))
    A4 = ((X-X1)*(Y-Y1))/((X2-X1)*(Y2-Y1))
    P_m = A1 *MQ11 +A2 *MQ21+A3*MQ12+A4*MQ22

    #P_d = ((X2-X)*(Y2-Y))/((X2-X1)*(Y2-Y1))*LD11 + ((X-X1)*(Y2-Y))/((X2-X1)*(Y2-Y1))*LD21+((X2-X)*(Y-Y1))/((X2-X1)*(Y2-Y1))*LD12+ ((X-X1)*(Y-Y1))/((X2-X1)*(Y2-Y1))*LD22
    return P_m
my_Inter_m = magnetic_flux(0,-800,90,-700,160,-600) 
print("The M of the magnetic flux is (my process) =",my_Inter_m)

def my_inter_Mx(X1,Y1,X,Y,X2,Y2,):
    P_iXd_iq1 = MQ11- ((MQ11-MQ21)*(X1-X))/(X1-X2)
    P_iXd_iq2 = MQ12- ((MQ12-MQ22)*(X1-X))/(X1-X2)

    P_xd_xq = P_iXd_iq1 - ((P_iXd_iq1-P_iXd_iq2)*(Y1-Y))/(Y1-Y2)

    return P_xd_xq
my_Inter_mag = my_inter_Mx(0,-800,90,-700,160,-600) 
print("The M of the magnetic flux is (my customer) =",my_Inter_mag)
def interpolation_d(X,Y,X1,Y1,X2,Y2,):
    A1 = ((X2-X)*(Y2-Y))/((X2-X1)*(Y2-Y1))
    A2 = ((X-X1)*(Y2-Y))/((X2-X1)*(Y2-Y1))
    A3 = ((X2-X)*(Y-Y1))/((X2-X1)*(Y2-Y1))
    A4 = ((X-X1)*(Y-Y1))/((X2-X1)*(Y2-Y1))
    P_d = A1 *LD11 +A2 *LD21+A3*LD12+A4*LD22

    #P_d = ((X2-X)*(Y2-Y))/((X2-X1)*(Y2-Y1))*LD11 + ((X-X1)*(Y2-Y))/((X2-X1)*(Y2-Y1))*LD21+((X2-X)*(Y-Y1))/((X2-X1)*(Y2-Y1))*LD12+ ((X-X1)*(Y-Y1))/((X2-X1)*(Y2-Y1))*LD22
    return P_d

#my_Inter_d = interpolation_d(-180,-1120,-200,-1150,-150,-1100) 
# my_Inter_d = interpolation_d(-30,-1180,-50,-1200,0,-1150) 
my_Inter_d = interpolation_d(-30,-1180,-50,-1150,0,-1200) 
print("The Ld of the Interpolation is (my process) =",my_Inter_d)

def interpolation_q(X,Y,X1,Y1,X2,Y2,):
    A1 = ((X2-X)*(Y2-Y))/((X2-X1)*(Y2-Y1))
    A2 = ((X-X1)*(Y2-Y))/((X2-X1)*(Y2-Y1))
    A3 = ((X2-X)*(Y-Y1))/((X2-X1)*(Y2-Y1))
    A4 = ((X-X1)*(Y-Y1))/((X2-X1)*(Y2-Y1))

    P_q = A1 *LQ11 +A2 *LQ21+A3*LQ12+A4*LQ22

    return P_q

my_Inter_q = interpolation_q(-810,-680,-850,-650,-800,-600)  
print("The Lq of the Interpolation is(my_process) =",my_Inter_q)

def my_inter_Ld(X,Y,X1,Y1,X2,Y2,):
    P_iXd_iq1 = LD11- ((LD11-LD21)*(X1-X))/(X1-X2)
    P_iXd_iq2 = LD12- ((LD12-LD22)*(X1-X))/(X1-X2)

    P_xd_xq = P_iXd_iq1 - ((P_iXd_iq1-P_iXd_iq2)*(Y1-Y))/(Y1-Y2)

    return P_xd_xq
def my_inter_Lq(X,Y,X1,Y1,X2,Y2,):
    P_iXd_iq1 = LQ11- ((LQ11-LQ21)*(X1-X))/(X1-X2)
    P_iXd_iq2 = LQ12- ((LQ12-LQ22)*(X1-X))/(X1-X2)

    P_xd_xq = P_iXd_iq1 - ((P_iXd_iq1-P_iXd_iq2)*(Y1-Y))/(Y1-Y2)

    return P_xd_xq

#my_Ld = my_inter_Ld(-180,-1120,-200,-1150,-150,-1100) 
#my_Ld = my_inter_Ld(-30,-1180,-50,-1200,0,-1150) 
my_Ld = my_inter_Ld(-30,-1180,-50,-1150,0,-1200)   
my_Lq = my_inter_Lq(-810,-680,-850,-650,-800,-600) 

print("The Ld of the Interpolation is  =",my_Ld)
print("The Lq of the Interpolation is  =",my_Lq)


