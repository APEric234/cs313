"""
File: sorting.py
Original Author: Br. Burton, designed to be completed by others.

Sorts a list of numbers.
"""
def sort_helper(numbers,start,sorted_list):
    if len(numbers) == len(sorted_list):
      for i in range(len(sorted_list)):
        numbers[i]=sorted_list[i]
    else:
      insert_position=-1
      start_new=start+1
      new_value=numbers[start]
      if new_value < sorted_list[0]:
        insert_position=0
      for i in range(1,len(sorted_list)):

        if  insert_position == -1:
          if  new_value<sorted_list[i]:
            insert_position=i
      if insert_position == -1:
        sorted_list.insert(len(sorted_list),new_value)
      else:
        sorted_list.insert(insert_position,new_value)

      sort_helper(numbers,start_new,sorted_list)



def sort(numbers):
    """
    Fill in this method to sort the list of numbers
    """
    list_in=[numbers[0]]
    sort_helper(numbers,1,list_in)
def prompt_for_numbers():
    """
    Prompts the user for a list of numbers and returns it.
    :return: The list of numbers.
    """

    numbers = []
    print("Enter a series of numbers, with -1 to quit")

    num = 0

    while num != -1:
        num = int(input())

        if num != -1:
            numbers.append(num)

    return numbers

def display(numbers):
    """
    Displays the numbers in the list
    """
    print("The list is:")
    for num in numbers:
        print(num)

def main():
    """
    Tests the sorting process
    """
    numbers = prompt_for_numbers()
    sort(numbers)
    display(numbers)

if __name__ == "__main__":
    main()