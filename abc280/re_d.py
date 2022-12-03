i = int(input())
import math
import numpy as np
fff=np.exp(i*np.log(i)-i)

# for i in range(100,1001):
#     f=math.factorial(i)
#     ff=1
#     for ii in range(1,i+1,1):
#         ff=ff*ii
#     fff=i*np.log(i)-i
#     j=i+1
#     ffff=0.5*(np.log(2*np.pi)-np.log(j))+j*(np.log(j+1/(12*j-1/10/j))-1)
#     fffff=0.5*(np.log(2*np.pi)-np.log(j)+j*(2*np.log(j)+np.log(j*np.sinh(1/j)+1/810/j**6)-2))
#     print("{0:10d}{1: 18.8f}{2:18.8f}{2:18.8f}".format(i,fff,ffff,fffff))