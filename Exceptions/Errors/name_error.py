try:
    x = int(input("enter the number x :"))

except ValueError:
    print("x is not an integer")
    
print(f"x is {x}")


# it cause error

"""
    print(f"x is {x}")
NameError: name 'x' is not defined
"""