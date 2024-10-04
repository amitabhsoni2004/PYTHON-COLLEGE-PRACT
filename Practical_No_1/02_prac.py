# Program to determine Even or Odd of given number..

def EvenOrOdd(n):
    if n == 0:
        print("Number is Zero(0)")
    elif (n % 2) == 0 : 
        print(f"{n} is Even")
    else:
        print(f"{n} is Odd")

number = int(input("Enter a number : "))
EvenOrOdd(number)