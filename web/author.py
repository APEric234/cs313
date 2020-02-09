

class Person:
  name = "anonymous"
  birth_year = "unknown"
  def display(self):
    print(f"{self.name} (b. {self.birth_year})")
class book:
  title = "untitled"
  author = Person()
  publisher = "unpublished"
  def display(self):
    print(f"{self.title}")
    print("Publisher:")
    print(f"{self.publisher}")
    print("Author:")
    self.author.display()
def main():
  a = book()
  a.display()
  print("Please enter the following:")
  name= input("Name: ")
  year=input("Year: ")
  title= input("Title: ")
  publisher= input("Publihser: ")
  print("")
  a.title = title
  a.author.name = name
  a.author.birth_year = year
  a.publisher = publisher
  a.display()
if __name__ == "__main__":
    main()