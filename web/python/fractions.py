from fractions import Fraction
class fraction:
  numerator=0
  denominator = 0
  def _init_(self):
    self.numerator=0
    self.denominator=1
  #prompt is here
  def prompt(self):
    self.numerator = int(input("Enter the numerator: "))
    self.denominator = int(input("Enter the denominator: "))

  def multiply_by(self,fractionb):
    self.numerator=self.numerator*fractionb.numerator

  def reduce(self):
    reduced_fraction = Fraction(self.numerator,self.denominator)
    self.numerator = reduced_fraction.numerator
    self.denominator = reduced_fraction.denominato

  def display_fraction(self):

    print(f"{self.numerator}/{self.denominator}")
  
  def display_decimal(self):
    print(f"{float(self.numerator)/float(self.denominator)}")
def main():
  a = fraction()
  a.prompt()
  a.reduce()
  a.display_fraction()
if __name__ == "__main__":
    main()