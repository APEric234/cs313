

class robot:
  x_cordinate = 10
  y_cordinate = 10 
  fuel_amount = 100
  def check_fuel(self,amount):
    if self.fuel_amount>= amount:
      self.fuel_amount = self.fuel_amount - amount
      return True
    print("Insufficient fuel to perform action")
    return False
  def status(self):
    print(f"({self.x_cordinate}, {self.y_cordinate}) - Fuel: {self.fuel_amount}")
  def move(self,text):
    fuel_cost = 5
    if self.check_fuel(fuel_cost):
      if(text == "left"):
        self.x_cordinate=self.x_cordinate-1
      elif(text == "right"):
        self.x_cordinate=self.x_cordinate+1
      elif(text == "up"):
        self.y_cordinate=self.y_cordinate-1
      elif(text == "down"):
        self.y_cordinate=self.y_cordinate+1
  def fire(self):
    fuel_cost=15
    if self.check_fuel(fuel_cost):
      
      print("Pew! Pew!")
    
  #prompt is here
  def command(self):
    valid_commands = {
      "left":'move',
      "right":'move',
      "up":'move',
      "down":'move',
      "fire":"fire",
      "status":"status",
      "quit":0

    }
    input2 = input("Enter command: ")
    command_value=valid_commands.get(input2,"not valid")
    while not (command_value in valid_commands.values()):
      input2 = input("Enter command: ")
      command_value=valid_commands.get(input2,"not valid")
    if input2 == "quit":
      print("Goodbye.")
    else:
      method = getattr(self,command_value)
      if command_value=="move":
        method(input2)
    
      else:
        method()
    return command_value

def main():
  a = robot()
  b=a.command()
  while not (b==0):
    b=a.command()
if __name__ == "__main__":
    main()