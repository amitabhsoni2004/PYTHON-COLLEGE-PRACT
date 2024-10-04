# write a program to check enter number is palindrome or not

def palindrome(n):
    original = n
    rev = 0
    while n > 0:
        remain = n % 10
        rev = rev * 10 + remain
        n //= 10
    return rev == original


def main():
    num = int(input("Enter a number : "))
    if palindrome(num):
        print("It is Palindrome")
    else:
        print("It is not a Palindrome")


main()