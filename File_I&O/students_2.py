import csv

name = input("enter u r name ? ")
home = input("enter u r place ?")

with open("students_2.csv", "a" ) as file:
    writer = csv.DictWriter(file, fieldnames=["name" , "home"])
    writer.writerow({"name": name, "home": home})
                     
                     