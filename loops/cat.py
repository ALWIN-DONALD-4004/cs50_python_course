#using break and continue
'''
while True:
    n = int(input("what's x?"))
    if n<0:
        continue
    else:
        break

for _ in range(n):
    print("meow")
  '''  

'''
#using break
while True:
    m = int(input("what's x?"))
    if n > 0:
        break

for _ in range(m):
    print("meow") 
    '''
     
#using function 
def main():
    number = getnumber()
    meow(number)
    
def getnumber():
    while True:
        num = int(input("enter how many times : "))
        if(num>0):
            #return num
            break
    return num
    
def meow(n):
    for _ in range(n):
        print("meow")
        

main()
    