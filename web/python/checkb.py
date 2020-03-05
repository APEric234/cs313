
class NegativeNumberError(Exception):
  def __init__(self, message):
        self.message = message
def get_inverse():
    loop =True
    while loop:
      number=int(input("Enter a number: "))
      if number < 0:
        raise NegativeNumberError("negative")
      elif number==0:
        raise ZeroDivisionError()
      number=int(number)

      return 1/number
        

        
def main():
    try:
      i=get_inverse()
      
      print(f"The result is: {i}")

    except NegativeNumberError:
      print("Error: The value cannot be negative")
      return -1
    except ValueError:
      print("Error: The value must be a number")
      return -1
    except ZeroDivisionError:
      print("Error: The value cannot be zero")
      return -1


if __name__ == "__main__":
    main()
