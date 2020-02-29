
#create gpa class
class GPA():
#create init and set default gpa to zero
  def __init__(self):
    self.__gpa=0
    self.letters = {'A':4.0,'B':3.0,'C':2.0,'D':1.0,'F':0}
    #create function for get_gpa
  property
  def __get_gpa(self):
    return self.__gpa
  
#create function to set_gpa,
  
  def __set_gpa(self,gpa_in):
#override any valiue outside of 0 -4 to 0 or 4 respectively
    if gpa_in <= 4 and gpa_in >= 0:
      self.__gpa = gpa_in
    elif gpa_in < 0:
      self.__gpa=0.0
    else:
      self.__gpa=4.0
    


#create function get_letter
  def __get_letter(self):
    letter_grade=list(self.letters.keys())
    if self.gpa==4.0:
      return letter_grade[0]
    elif self.gpa >= 3.0:
      return letter_grade[1]
    elif self.gpa >=2.0:
      return letter_grade[2]
    elif self.gpa >=1.0:
      return letter_grade[3]
    else:
      return letter_grade[4]
      
#create function set_letter
  def __set_letter(self,letter_in):
    self.gpa = self.letters[letter_in]
  
  letter = property(__get_letter,__set_letter)
  gpa = property(__get_gpa,__set_gpa)
def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    value = float(input("Enter a new GPA: "))

    student.gpa = value
    print("After setting value:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    letter = input("Enter a new letter: ")

    student.letter = letter

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

if __name__ == "__main__":
    main()