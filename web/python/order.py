
class Order:

  def __init__(self):
    self.id=""
    self.products=[]
  
  def get_subtotal(self):
    sum=0
    for x in self.products:
      sum=sum+x.get_total_price()
    return sum
  def get_tax(self):
    return self.get_subtotal()*.065
  def get_total(self):
    return self.get_subtotal()+self.get_tax()
  #must be of Product type
  def add_product(self,product):
    self.products.append(product)
  def display_receipt(self):
    print(f"Order: {self.id}")
    for x in self.products:
      x.display()
    print(f"Subtotal: ${'{0:.2f}'.format(self.get_subtotal())}")
    print(f"Tax: ${'{0:.2f}'.format(self.get_tax())}")
    print(f"Total: ${'{0:.2f}'.format(self.get_total())}")
    