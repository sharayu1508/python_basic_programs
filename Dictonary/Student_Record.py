stud={
    101:
    {
        "roll no":101,
        "name":"ram",
        "age":18,
        "subject":("Python","Java","Mern"),
        "marks":[90,89,78]
    },
    102:
    {   
        "roll no":102,
        "name":"sita",
        "age":20,
        "subject":("Python","Java","Mern"),
        "marks":[70,80,90]
    },
    103:
    {
        "roll no":103,
        "name":"rahul",
        "age":20,
        "subject":("Python","Java","Mern"),
        "marks":[58,79,83]

    },
    104:
    {
        "roll no":104,
        "name":"gita",
        "age":18,
        "subject":("Pyhton","Java","Mern"),
        "marks":[88,97,100] 

    }
    
}

print("Student Data : ")
print("Roll",end="   ")
print("Name",end="    ")
print("Total",end="  ")
print()
for k in stud:
    total=sum(stud[k]["marks"])
    print(stud[k]["roll no"]," ",stud[k]["name"] ," ",total)

print()
print("----------------------------------------")
print()

print("Topper Student ")

l1=[]
for k in stud:
    total=sum(stud[k]["marks"])
    l1.append(total)

mx=max(l1)

for k in stud:
    if(sum(stud[k]["marks"])==mx):
        print("Roll No : ",stud[k]["roll no"])
        print("Name : ",stud[k]["name"])


# print("Topper Student ")
# highest=0
# total=0
# topper=""
# for k in stud:
#     total=sum(stud[k]["marks"])

#     if total>highest:
#         highest=total
#         topper=stud[k]["name"]

# print("Topper Name : ",topper)

print()
print("-------------------------------")
print()

py=0
py_topper=""
for value in stud.values():
    if value["marks"][0]>py:
        py=value["marks"][0]
        py_topper=value["name"]

print("Python Topper : ",py_topper)
print("Marks : ",py)

print()
print("-----------------------------------")
print()

print("Age is greater than 18 students : ")
for value in stud.values():
    if value["age"]>18:
        print("Name : ",value["name"])
        print("Age : ",value["age"])


print()
print("------------------------------------------")
print()

print("Mern Marks > 70 and < 90 students : ")
for value in stud.values():
    if value["marks"][2]>70 and value["marks"][2]<90:
        print("Name : ",value["name"])
        print("Marks : ",value["marks"][2])
