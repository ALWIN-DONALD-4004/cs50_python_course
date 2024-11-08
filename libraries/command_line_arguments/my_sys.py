
#sys.argv

#argv ---> argument vector

import sys

'''
print("hello, my name is", sys.argv[1])
'''
#if the user does not type the arg then it throws the Index Error, 
#how to over come it

# to handle the error

'''
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("to give the arguments")
'''
'''
if len(sys.argv) < 2:
    print("too few arguments")

elif len(sys.argv) > 2:
    print("too many arguments")
    
else:
    print("hello, my name is ",sys.argv[1])
'''
    
# if we print full name as in cli "alwin donald"
'''
if len(sys.argv) < 2:
    print("too few arguments")

elif len(sys.argv) > 2: 
    print("too many arguments")
    
print("hello, my name is ",sys.argv[1])
'''

# if we run the above code with wrong input , the system throws the Index error
'''
if len(sys.argv) < 2:
    sys.exit("too few arguments")

elif len(sys.argv) > 2: 
    sys.exit("too many arguments")
    
print("hello, my name is ",sys.argv[1])
'''

# to reduce the code , and remove elif

if len(sis.argv) < 2 :
    sys.exit("too few arguments")

for arg in sys.argv[1:]:  # using slice operator
    print("hello,my name is ",arg)
    

