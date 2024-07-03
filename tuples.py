mytuples=(10,20,30,"apple",20.5)
type(mytuples)
len(mytuples)
#access
print(mytuples[2])
print(mytuples[-2])
print(mytuples[1:4])
print(mytuples[-2:4])
print(mytuples.index(30))
print(20 in mytuples)
print(5 in mytuples)
#convert to list
y=list(mytuples)
print(y)
y[1]="banana"
print(y)
mytuples=tuple(y)
print(mytuples)
#mytuples unpack
fruits=("apple","banana","cherry")
(green,yellow,red)=fruits
print(green)
print(yellow)
print(red)
vegitables=("pappaya","tomato","chilli","cucumber","carot")
print(vegitables)
(green,yellow,*red)=vegitables
print(green)
print(yellow)
print(red)
#joint
tuple3=fruits+vegitables
print(tuple3)
#*
mytuples=tuple3*2
print(mytuples)
#count
mytuples.count("apple")

