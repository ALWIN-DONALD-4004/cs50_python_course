# or operator ( either one contition are true , print the statement)

x = int(input("enter the x : "))
y = int(input("enter the y : "))

if x > y or x < y:
    print("x and y are not equal")
else:
    print("x and y are equal")
    
    
# and operator ( both contition are true , print the statement)
# grade decission

mark = int(input("enter the mark : "))

if mark>=80 and mark<=100:
    print("Grade A")
elif mark>=50 and mark<80:
    print("Grade B")
else:
    print("fail")
    
# other method to use 'and'

mark1 = int(input("enter the mark : "))
if  80 <= mark1 <=100:
    print("Grade A")
elif 50 <= mark1 <80:
    print("Grade B")
else:
    print("fail")
    
    
# reduce the two ocondtion of code

if mark >=90:
    print("Grade A")
elif mark >=80:
    print("Grade B")
elif mark >=70:
    print("Grade C")
elif mark >=60:
    print("Grade D")
else:
    print("fail")
