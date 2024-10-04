# Deleting 0th and 4th element in list and print it


def delete_elem(l):
    if len(l) > 4:
        del l[4]

    if len(l) > 0:
        del l[0]

    
    print(f"Updated List : {l}")


def main():
    l = [10,20,30,40,50,60]

    print(f"Before updated list : {l}")

    delete_elem(l)

main()