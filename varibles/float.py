# #decimals values are called float

# x = float(input("Enter x :"))# x=1.2 
# y = float(input("Enter y :"))# y =3.4
# print(x+y) #4.6

# """ docs.python.org/3/library/stdtypes.html#round
#  round(number[,ndigits]) """

# # round function is used to round the float value to the nearest integer.
# z = round(x+y) # x=1.2 y =3.4
# print(z) # 5 



# #if we can print the integers as  1,000 or 10,000 .... this format is known as periods.
# amount = int(input("enter the amount : "))
# print(f"{amount:,}")

n1 = 22
n2 = 7
op = n1/n2
print(op) #3.142857142857143

op1 = round(n1/n2,2)
print(op1) #3.14

print(f"{op:.2f}") #3.14
print(f"{op:.3f}") #3.143




