

class Phone:
  def __init__(self):
    area_code=0
    prefix=0
    suffix=0
  def prompt_number(self):
    
    self.area_code=input("Area Code: ")
    self.prefix=input("Prefix: ")
    self.suffix=input("Suffix: ")
  def display(self):
    print("Phone info:")
    print(f"({self.area_code}){self.prefix}-{self.suffix}")
class SmartPhone(Phone):
  def __init__(self):
    super().__init__()
    email="a@a.com"
  def prompt(self):
    super().prompt_number()
    self.email=input("Email: ")

  def display(self):
    super().display()
    print(f"{self.email}")
def main():
  a = Phone()
  print("Phone:")
  a.prompt_number()
  print("")
  a.display()
  print("")
  print("Smart phone:")
  b = SmartPhone()
  b.prompt()
  print("")
  b.display()
if __name__ == "__main__":
    main()