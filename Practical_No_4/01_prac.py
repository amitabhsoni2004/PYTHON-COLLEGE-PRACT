# To insert an element in List


def insertion(l , index , num):
    if index < 0:
        print("Index can not be negative in List...Try again..")
        main()
    elif index > len(l):
        l.append(num)
    else:
        l.insert(index, num)

    return l

def main():
    l = [1 , 2 , 3 , 4 , 5]

    index = int(input("Enter a index where you want to Enter the element : "))
    num = int(input("Enter a element to be inserted in List : "))
    up_lst = insertion(l , index , num)
    print(f"Updated List : {up_lst}")
main()