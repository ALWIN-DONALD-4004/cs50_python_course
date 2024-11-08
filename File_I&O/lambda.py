import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    #name, house = line.rstrip().split(",")
    for name, home in reader:
        students.append({"name": name,"home":home})
'''        
def get_name(student):
    return student["name"]'''
    
    # key = get_name
        
for student in sorted(students, key = lambda student:student["name"]):
    print(f"{student['name']} is in {student['home']}")