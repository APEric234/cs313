

class Shape:
  def __init__(self):
    self.name="Shape"
  def get_area(self):
    pass
  def display(self):
    print(f"{self.name} - {"{0:.2f}".format(self.get_area())}")

class Circle(Shape):
  def __init__(self):
    super().__init__()
    self.name="Circle"
    self.radius=0
  def get_area(self):
    return 3.14*self.radius*self.radius


class Rectangle (Shape):
  def __init__(self):
    super().__init__()
    self.name="Rectangle"
    self.length=0
    self.width=0
  def get_area(self):
    return self.length*self.width