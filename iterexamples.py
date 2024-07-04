list1=[12,3,4,55,43]
list2=iter(list1)
next(list2)
ages = [5, 12, 17, 18, 24, 32]

#
for a in ages:
    if a >=18:
        print(a)
        
# filter     
def fulc(a):
    if a <18:
        return True
    else:
        return False
list(filter(fulc,ages))

#(numerical data type)

import numpy as np
list1=[1,2,3,4,6,7,8]
ar1=np.array(list1)
ar1
#
list2=[22,12,66,6.6,"sabeeda",True,False]
ar2=np.array(list2)
ar2
#
ar1.sum()
ar1.max()
ar1.min()
ar1.mean()

ar1.shape
list3=[[1,2,3,4,6,7,8],[1,2,3,4,6,7,8]]
ar3=np.array(list3)
ar3
ar3.shape

#0D

list4=[23]
ar4=np.array(list4)
ar4
ar4.shape

#1Dimensions

list1=[1,2,3,4,5,6]
ar1=np.array(list1)
ar1
ar1.shape

#2D

list2=[[1,2,3,4,5,6,7],[2,4,5,6,7,8,9]]
ar2=np.array(list2)
ar2
ar2.shape

#3D

list3=[[1,3,4,5,4],[4,5,6,8,9],[1,4,4,4,5,8]]
ar3=np.array(list3)
ar3
ar3.shape