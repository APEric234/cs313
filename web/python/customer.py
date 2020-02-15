
class Customer:

  def __init__(self):
    self.id=""
    self.name=""
    self.orders=[]
  
  def get_order_count(self):
    return len(self.orders)

  def get_total(self):
    sum=0
    for x in self.orders:
      sum=sum+x.get_total()
    return sum
  #must be of Product type
  def add_order(self,order):
    self.orders.append(order)
  def display_summary(self):
    print(f"Summary for customer '{self.id}':")
    print(f"Name: {self.name}")
    print(f"Orders: {self.get_order_count()}")
    print(f"Total: ${'{0:.2f}'.format(self.get_total())}")
  def display_receipts(self):
    print(f"Detailed receipts for customer '{self.id}':")
    print(f"Name: {self.name}")
    
    for x in self.orders:
      print(f"")
      x.display_receipt()
    