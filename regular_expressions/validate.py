import re

email = input("what is your email : ").strip()

# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("invalid")
'''
username, domine = email.split("@")

if username and domain.endwith(".com"):#("." in domine)
    print("valid")
else:
    print("Invalid")
'''
  
# 're' keyword used for regular expression
# re.search(pattern, string , false = 0)

if re.search(r".+@.+\.com",email):
    print("valid")
else:
    print("Invalid")

