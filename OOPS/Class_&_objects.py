class Student:
    
   def __init__(self,name,place):
       self.name = name
       self.place = place       
        

def main():
    student = get_student()
    print(f"{student.name} from {student.place}")
    
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