

def loop_int():
    loop =True
    while loop:
        try:
            number=input("Enter a number: ")
            number=int(number)
            print(f"The result is: {number}")
            loop=False
        except:
            pass
        
def main():
    
    loop_int()
if __name__ == "__main__":
    main()
