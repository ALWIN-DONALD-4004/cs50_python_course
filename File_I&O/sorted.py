names = []

with open("names.txt","r") as file:
    for line in file:
        names.append(line.rstrip())
        
print("names in assending order ....")
for name in sorted(names):
    print(f"hello, {name}")
    
print()
    
print("names in desending order ....")
for name in sorted(names, reverse=True):
    print(f"hello, {name}")