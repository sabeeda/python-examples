#iter

list1=[12,3,4,55,43]
list2=iter(list1)
next(list2)

#forloop iter

ages = [5, 12, 17, 18, 24, 32]
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
import numpy as np

ar4=np.array(23)
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

list3=[[1,3,4,15,4],[4,5,61,8,9],[1,4,16,9,5]]
ar3=np.array(list3)
ar3
ar3.shape
sabi=ar3.reshape(5,3)
sabi
#first row select cheyan
sabi[0]
#colum selection
sabi[:,0]
sabi[0,2]
sabi[0:2,1]
sabi[2:4,1]
sabi
sabi[2:4]
sabi[2:4,0]
sabi[2:4,0:3]
sabi[2:4,0:3:2]

#arange function
list(range(1,21,3)) #list function
np.arange(1,21,step=3)#array function
#zeros
np.zeros(3)
np.zeros([3,3,3])
#ones
np.ones(4)
np.ones([4,4,4])

#*,+
np.ones(2)
np.ones([3,2,2])*3    #metrix number(group),row,column)

#linspace

np.linspace(1,200,5)

