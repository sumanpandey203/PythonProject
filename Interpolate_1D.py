import math
import numpy as np
import matplotlib.pyplot as plt

LQ11_q = -2217
LQ12_q = -2151

LQ11_d = -2162
LQ21_d = -2095


LD_q11 = -1704
LD_q21 = -1633

LD_d11 = -1667
LD_d21 = -1594
# LD21 = 0.0006335
# LD22 = 0.000616

# #########for Ld blocked
# def interpolate1D_LD(X,Y,X1,Y1,X2,Y2,):
#     A1 = ((Y2-Y))/((Y2-Y1))
#     A3 = ((Y-Y1))/((Y2-Y1))

#     P_d = A1 *LD_q11 + A3*LD_q21
#     return P_d
# def interpolate1D_LD_d(X,Y,X1,Y1,X2,Y2,):
    
#     A1 = ((X2-X))/((X2-X1))
#     A4 = ((X-X1))/((X2-X1))
#     P_d_d = A1 *LD_d11 + A4*LD_d21
#     return P_d_d
# for i in range(-1149,-1119):
    
#     my_Inter_LD = interpolate1D_LD(-200,i,-200,-1150,-200,-1100)  
#     print("The LD 1D of ", i ,"the Interpolation is(my_process not matched q) =",my_Inter_LD) 
 
# my_Inter_LD_d = interpolate1D_LD_d(-180,-1100,-200,-1110,-150,-1100)  
# print("The LD 1D of the Interpolation is(my_process not matched d) =",my_Inter_LD_d) 


def interpolate1D_LQ(X,Y,X1,Y1,X2,Y2,):
    A1 = ((Y2-Y))/((Y2-Y1))
    A3 = ((Y-Y1))/((Y2-Y1))

    P_d = A1 *LQ11_q + A3*LQ12_q
    return P_d
def interpolate1D_LQ_d(X,Y,X1,Y1,X2,Y2,):
    
    A1 = ((X2-X))/((X2-X1))
    A4 = ((X-X1))/((X2-X1))
    P_d_d = A1 *LQ11_d + A4*LQ21_d
    return P_d_d

    
my_Inter_LQ = interpolate1D_LQ(-850,-680,-850,-650,-850,-600)  
print("The LD 1D of the Interpolation is(my_process not matched q) =",my_Inter_LQ) 
 
my_Inter_LQ_d = interpolate1D_LQ_d(-810,-600,-850,-600,-800,-600)  
print("The LD 1D of the Interpolation is(my_process not matched d) =",my_Inter_LQ_d) 