
#create gpa class
class GPA():
#create init and set default gpa to zero
  def __init__(self):
    self.gpa=0
    self.letters = {'A':4.0,'B':3.0,'C':2.0,'D':1.0,'F':0}
    #create function for get_gpa
  def get_gpa(self):
    return self.gpa
  
#create function to set_gpa,
  def set_gpa(self,gpa_in):
#override any valiue outside of 0 -4 to 0 or 4 respectively
    if gpa_in <= 4 and gpa_in >= 0:
      self.gpa = gpa_in
    elif gpa_in < 0:
      self.gpa=0.0
    else:
      self.gpa=4.0
    


#create function get_letter
  def get_letter(self):
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
  def set_letter(self,letter_in):
    self.gpa = self.letters[letter_in]

def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    value = float(input("Enter a new GPA: "))

    student.set_gpa(value)

    print("After setting value:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    letter = input("Enter a new letter: ")

    student.set_letter(letter)

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

if __name__ == "__main__":
    main()