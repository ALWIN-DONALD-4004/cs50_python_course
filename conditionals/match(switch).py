name = input("ENTER YOUR NAME :")

match name:
    case "alwin":
        print("vill")
    case "chandrabalan":
        print("vill")
    case "dinakaran":
        print("vill")
    case "gokul":
        print("cud")
    case _:
        print("where ?")
        
match name:
    case "alwin" | "chandrabalan" |"dinakaran":
        print("vill")
    case "gokul":
        print("cud")
    case _:
        print("where ?")