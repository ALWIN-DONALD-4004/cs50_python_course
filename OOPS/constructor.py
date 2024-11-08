class Student:
    
   def __init__(self,name,place=None):
       if not name:
           raise ValueError("missing name")
       if place not in ["vill","pondy"]:
           raise ValueError("invalid palce")
           
       self.name = name
       self.place = place       
        
   def __str__(self):
       return f"{self.name} from {self.place}"
        

def main():
    student = get_student()
    # print(f"{student.name} from {student.place}")
    print(student)
    
def get_student():  
    
#   '''
#   student = Student()
#   student.name = input("name:") #attributes -- > instance variable
#   student.place = input("place")'''
  
     name = input("name : ")
     place = input("place : ")
     student = Student(name,place)
     return student

if __name__ == "__main__":
    main() 