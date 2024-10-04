# Generate a fibonacci series

def fibo(terms):
    n1 = 0
    n2 = 1
    print(f"{n1} {n2} ",end= "")
    for i in range(2, terms):
        n3 = n1 + n2
        print(f"{n3} ",end= "")
        n1 = n2
        n2 = n3

terms = int(input("Ente the number of terms : "))
fibo(terms)