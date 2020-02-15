from collections import deque

class Student:
  def __init__(self):
    name = "anonymous"
    course = "unknown"
  def display(self):
    print(f"Now helping {self.name} with {self.course}")
  def prompt(self):
    self.name=input("Enter Name: ")
    self.course=input("Enter course: ")
class HelpSystem:
  waiting_list = deque()
  #returns true when a student is in deque
  def is_student_waiting(self):
    if len(self.waiting_list) > 0:
      return True
    return False
  #input required to be a student
  def add_to_waiting_list(self,s):
    self.waiting_list.append(s)
  def help_next_student(self):
    if self.is_student_waiting():
      return self.waiting_list.popleft()
    
def main():
  a = True
  help = HelpSystem()
  while a:
    print("")
    print("Options: ")
    print("1. Add a new student")
    print("2. Help next student")
    print("3. Quit")
    in_user = int(input("Enter selection: "))
    print("")
    if in_user==3:
      a=False
      print("Goodbye")
      continue
    if in_user==2:
      if help.is_student_waiting():
        student = help.help_next_student()
        student.display()
      else:
        print("No one to help.")
    elif in_user==1:
      student= Student()
      student.prompt()
      help.add_to_waiting_list(student)
    else:
      print("Errror"
      )
  
if __name__ == "__main__":
    main()