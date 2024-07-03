mydict={"brand":"ford","model":"mustand","year":1964}
print(mydict)
type(mydict)
mydict.keys()
#values
mydict.values()
mydict["model"]
mydict.get("model")
#creating dic
phonebook=dict({"name":"sabeeda","country":"india","telephone":2404})
print(phonebook)
person=dict([("name","aiza"),("country","india"),("telephone",12354)])
print(person)
#marksheet
marksheet=dict({"name":["haseeb","anil","nandu"],"english":[55,6,90],"matchs":[88,66,75]})
print(marksheet)
marksheet["english"]
#changes varthan
phonebook["name"]="jone"
print(phonebook)
#add cheyyan
phonebook["place"]="kerala"
print(phonebook)
#update akan/replace
phonebook.update({"place":"pmna"})
print(phonebook)
phonebook.update({"state":"kerala"})
print(phonebook)
#removed
phonebook.pop("state")
print(phonebook)
#last item cancelled
phonebook.popitem()
print(phonebook)
#delete
del phonebook["name"]
print(phonebook)
#clear
phonebook.clear()
print(phonebook)
del phonebook
print(phonebook)
#length
len(marksheet)
print(mydict)
mydict.setdefault("color","white")
print(mydict)
#copy
mydict2=mydict.copy()
print(mydict2)
dict3=dict(mydict)
print(dict3)
dict4=dict(mydict.items())
print(dict4)
#store data of single student
jessa = {'name': 'Jessa', 'state': 'Texas', 'city': 'Houston', 'marks': 75}
emma = {'name': 'Emma', 'state': 'Texas', 'city': 'Dallas', 'marks': 60}
kelly = {'name': 'Kelly', 'state': 'Texas', 'city': 'Austin', 'marks': 85}
#nested dictonary
class_six = {'student1': jessa, 'student2': emma, 'student3': kelly}

#get student3s name and mark
print("student 3 name:",class_six['student3']['city'])
print('student 3 marks:',class_six['student3']['marks'])
#maxmum,minimum
dict1={"c":42,"b":95,"a":35}
print(sorted(dict1.items()))
print(sorted(dict1.values()))
print(sorted(dict1))
print(max(dict1))
print(min(dict1))
