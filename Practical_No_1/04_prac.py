# To find out reverse of number

def reverse(n):
    rev = 0
    while n > 0:
        remainder = n % 10
        rev = rev * 10 + remainder
        n = n // 10
    return rev

number = int(input("Enter a number : "))
reversed_no = reverse(number)

print(f"The reverse of {number} is {reversed_no}")