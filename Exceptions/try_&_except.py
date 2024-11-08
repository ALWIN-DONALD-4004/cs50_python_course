"""try:
    x = int(input("enter the number x :"))
    print(f"x is {x}")
#value error if enter cat
except ValueError:
    print("x is not an integer")"""

"""
try:
    x = int(input("enter the number x :"))

except ValueError:
    print("x is not an integer")
else:    #IT THROWS NAME ERROR   , goto nanme errorrr
    print(f"x is {x}") 
    
"""
"""
# when the user input correct arg the the loop break
while True:
    try:
        x = int(input("enter x : "))
    except ValueError:
        print("x is not an integer :")
    else:
        break

print(f"x is {x}")
"""

"""
# when the user input correct arg the the loop break
while True:
    try:
        x = int(input("enter x : "))
        break
    except ValueError:
        print("x is not an integer :")

print(f"x is {x}")
"""
"""
# using function
def get_int():
    while True:
        try:
             #x = int(input("enter x : "))
             return int(input("enter x : "))  
         
        except ValueError:
             print("x is not an integer :")
       # else:
           # return x
"""
"""
# pass
def get_int1():
    while True:
        try:
             #x = int(input("enter x : "))
             return int(input("enter x : "))  
         
        except ValueError:
             pass
         
         
def main():
    #x = get_int()
    y = get_int1()
    
    print(f"x is {y}")

main()
"""
# caller
def main():
    #x = get_int()
    y = get_int1("what's x ? ")
    print(f"x is {y}")
    
    
def get_int1(promt):
    while True:
        try:
             return int(input(promt))  
         
        except ValueError:
             pass
    
main()

    