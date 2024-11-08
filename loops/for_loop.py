"""
print("meow")
print("meow")
print("meow")
"""

# list ---> it is a datatype which stores the xil values in single variable 
# it is represent in [] square brackets

for i in [0,1,2]:
    print("meow")


for i in range(3):  # range(3-1) 
    print("meow")
    
print("meow" * 3) #meowmeowmeow

print("meow\n" * 3, end="")

# print in column
for _ in range(3):
    print('#')
    
#using function for column
def main():
    print_column(3)
    print_row(4)

def print_column(height):
    # for _ in range(height):
    #    print('#')
    print("#\n"*height,end = "")
    
def print_row(width):
    print("?" * width)
       
main()
