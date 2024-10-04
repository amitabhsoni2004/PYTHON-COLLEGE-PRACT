# program to copy one list element to another list

def copy_list(l1):
    l2 = []
    for i in l1:
        l2.append(i)

    print(f"Copied list : {l2}")

def create_list(size):
    l1 = []
    for i in range(size):
        a = int(input(f"Enter a element no {i + 1} : "))
        l1.append(a)

    print(f"Original List : {l1}")
    copy_list(l1)

def main():
    size = int(input("Enter a size of List : "))
    create_list(size)


main()