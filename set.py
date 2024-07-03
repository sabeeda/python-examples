myset={"banana","cherry","mango","apple","mango"}
print(myset)
print(len(myset))
print(type(myset))
print("mango" in myset)
print("graps" not in myset)
#add
myset.add("orange")
print(myset)
#2sett creating
thisset={"tomato","pappaya","chilli"}
thisset.update(myset)
print(thisset)
#remove
myset.remove("apple")
print(myset)
#pop
myset.pop()
print(myset)
#
myset.clear()
print(myset)
#del
del myset
print(myset)

#union/joint cheyan
set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)
print(set3)
set4={"banana","naval","apple","mango"}
set5={"sabeeda","anil","hasib","nandu"}
myset=set1.union(set3,set4,set5)
myset2=set1|set2|set4|set5
print(myset)
#update
set4.update(set2)
print(set4)
#intersection(senter bagam)
set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set1.intersection(set2)
#
set3=set1&set2
print(set3)
#
set1.intersection_update(set2)
print(set1)
#diffrence
set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set1-set2
set1.difference(set2)
#diffrence update
set1.difference_update(set2)
print(set1)
#symmetric diffrence
set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set1.symmetric_difference(set2)
#^
set1^set2
set1.symmetric_difference_update(set2)
print(set1)


x={"A","B","C"}
Y={"F","E","D","C","B","A"}
z=x.issubset(Y)
print(z)
x<=Y

X={"apple","banana","cherry"}
y={"google","microsoft","facebook"}
x.isdisjoint(y)

