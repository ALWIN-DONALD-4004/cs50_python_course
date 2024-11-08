# 'def' keyword is used to declear the function


#function without parameter
"""def hello():
    print("hello")


name = input("what's your name?")
hello()
print(name)"""


#function with parameter
"""def hello1(to):
    print("hello, " , to)

name1 = input("what's your name?").strip().title()
hello1(name1)

#function with or without arguments
def hello2(to="world"):
    print("hello, " , to)
    
hello2()
name2 = input("what's your name?").strip().title()
hello2(name2)"""


# In the above program the hello function is declare above the call functionname.

"""hello3()

def hello3(to="world"):
    print("hello, " , to)"""
    
# in ihis above code it throws hello3 not defined because the function hello3 is below the callfunction ,
# it can be over come by the main function.

"""def main():
    name3 = input("enter your name: ")
    hello4(name3)
    
def hello4(to):
    print("hello," , to)
    
main()"""



# return keyword

def main():
    x = int(input("enter x:"))
    print(f"{x} square is",square(x))
    
def square(n):
    return n*n # pow(n,2)
    
main()

    