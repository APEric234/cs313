class Book:

  def __init__(self):
    self.title=""
    self.author=""
    self.publication_year=0

  def prompt_book_info(self):
    self.title=input("Title: ")
    self.author=input("Author: ")
    self.publication_year=int(input("Publication Year: "))
  def display_book_info(self):
    print(f"{self.title} ({self.publication_year}) by {self.author}")
  
class TextBook(Book):
  def __init__(self):
    super(TextBook, self).__init__()
    self.subject = ""
  def prompt_subject(self):
    self.subject=input("Subject: ")
  def display_subject(self):
    print(f"Subject: {self.subject}")
class PictureBook(Book):
  def __init__(self):
    super(PictureBook, self).__init__()
    self.illustrator = ""
  def prompt_illustrator(self):
    self.illustrator=input("Illustrator: ")
  def display_illustrator(self):
    print(f"Illustrated by {self.illustrator}")
def main():
  b = Book()
  b.prompt_book_info()
  print()
  b.display_book_info()
  print()
  c=TextBook()
  c.prompt_book_info()
  c.prompt_subject()
  print()
  c.display_book_info()
  c.display_subject()
  print()
  d = PictureBook()
  d.prompt_book_info()
  d.prompt_illustrator()
  print()
  d.display_book_info()
  d.display_illustrator()
if __name__ == "__main__":
    main()