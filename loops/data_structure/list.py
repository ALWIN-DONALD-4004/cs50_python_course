students = ["alwin","athi","ari","chan"]

#to print elements in list by its index value
print(students[0])
print(students[1])
print(students[2])
print(students[3])

#using for loop
"""i = 0
for student in students:
    print(students[i])
    i+=1"""

for student in students:
    print(student) 
    
for  i in range(len(students)):    # length == len
       print(students[i])
       print(i,students[i])
       

# slice operator(start : end)

name = ["alwin","fred","athi","ari","chan"]
print(name[1:]) # 1: from 1 to last