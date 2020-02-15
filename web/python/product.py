

class Product:

  def __init__(self,id_in,name_in,price_in,quantity_in):
    self.id=id_in
    self.name=name_in
    self.price=price_in
    self.quantity = quantity_in
  def get_total_price(self):
    return self.price*float(self.quantity)
  def display(self):
    print(f"{self.name} ({self.quantity}) - ${'{0:.2f}'.format(self.get_total_price())}")