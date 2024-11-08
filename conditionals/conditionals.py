"""
>    greater than
>=   greater than or equal to
<    less than
<=   less than or equal to
==   equal to
!=   not equal to
"""

x = int(input("Enter x: "))
y = int(input("Enter y: "))

# if statement
if x < y:
    print("x is less than y")

if x > y:
    print("x is grater than y")
    
if x == y:
    print("x is equal to y")
    
    
# if else statement
if x == y:
    print("x is equal to y")
else :
    print("x is not equal to y")


# if elif else statement    
if x < y:
    print("x is less than y")
elif x > y:
    print("x is grater than y")   
else:
    print("x is equal to y")

