"""
+ 
-
*
/
%
"""

# program for even or odd
'''
x = int(input("enter the value x :"))

if(x%2 == 0):
    print(f"{x} is an even number")
else:
    print(f"{x} is odd number")
    '''
   
    
#program of odd or even using function
def main():
    y = int(input("enter the value y :"))
    if is_even(y):
        print(f"{x} is Even")
    else:
        print(f"{x} is odd")
    
def is_even(n):
    if n%2 == 0:
        return True  # using bool
    else:
        return False
    
"""
def is_even(n):
    return True if n%2 == 0 else False
"""

"""
def is_even(n):
    return (n%2 == 0)  # n%2 == 0
"""

main()

