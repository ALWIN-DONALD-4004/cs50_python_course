# docs.python.org/3/library/stdtypes.html#string-methods

name = input("what's your name? ")

# remove whitespace from str
name = name.strip()  
print(f"hello , {name}")

#Capaitalize the str
name = name.capitalize() #Alwin donald
print(f"hello , {name}")

#title the str
name = name.title()  # Alwin Donald
print(f"hello , {name}")


# to combine all the function using '.' 
name = name.strip().title()
print(f"hello , {name}")

#to set all functions in the input variable name1
name1 = input("Enter your name:").strip().title()
print(f"hello, {name1}")


# split method
# Split user's name into first name and the last name
first,last = name1.split(" ")
print(f"hello , {first}")
print(f"hello , {last}")

name2 = frist + last # here the '+' operator preforms the concatenation processes because the variables are string.
print(f"hello , {name2}")