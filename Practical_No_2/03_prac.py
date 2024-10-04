# printing a histogram 

def histo(n):
    for i in n:
        print('*' * i)

def main():
    n = int(input("Enter a number : "))
    num = []
    for i in range(n):
        a = int(input("Enter a number in List : "))
        num.append(a)
    histo(num)

main()