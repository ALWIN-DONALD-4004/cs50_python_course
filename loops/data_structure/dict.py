# dict has key & values
# it can be represented in {}

students = {
    "alwin": "villu",
    "chan" : "villu",
    "ari" : "pondy",
    "athi" : "pondy"
}

# to print keys
for i in students:
    print(i)

print("\n")

# to print values
for i in students:
    print(students[i])
    
print("\n")
    
# to print keys & values
for i in students:
    print(i,students[i],sep = " --- ")
    


students_ece = [
    {"name":"alwin","place":"villu","reg" : "4004"},
    {"name":"chan","place":"villu","reg" : "4015"},
    {"name":"ari","place":"pondy","reg" : "4005"},
    {"name":"athi","place":"pondy","reg" : None}
]

for student in students_ece:
    print(student["name"],student["place"],student["reg"],sep=" ---> ")