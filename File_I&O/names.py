7

# name = input("what's your name:")
# print(f"hello,{name}")


# names = []

# for _ in range(3):
#     names.append(input("what's your name : "))
    
# for name in sorted(names):
#     print(f"hello, {name}")
    
    
#name = input("what's your name ? ")

'''
#file = open("names.txt", "w")  # w ---> write every time ,i run it rewrites the whole text file

file = open("names.txt","a") # a---> append output as  alwinarichan

file.write(f"{name}\n")

file.close()
'''

#instred of usin close we can use 'with' ---- > context
'''
with open("names.txt","a") as file:
'''


# to read file

with open("names.txt","r") as file:
    for line in file:
        print("hello",line.rstrip())
        
        