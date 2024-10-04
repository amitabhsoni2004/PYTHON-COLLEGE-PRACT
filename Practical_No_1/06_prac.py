# To determine whether a given number is armstrong or not

def is_armstrong(number):
    original_number = number
    armstrong_sum = 0
    num_digits = len(str(number))
    
    while number > 0:
        digit = number % 10
        armstrong_sum += digit ** num_digits
        number //= 10
    
    return original_number == armstrong_sum


def main():
    num = int(input("Enter a number: "))
    if is_armstrong(num):
        print("It is an Armstrong number")
    else:
        print("It is not an Armstrong number")

main()