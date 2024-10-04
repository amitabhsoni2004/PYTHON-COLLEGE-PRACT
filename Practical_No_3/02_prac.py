# print element which is less than five in list

def less_five(l):
    for i in l:
        if i < 5:
            print(i, end=" ")

def main():
    l = [1, 2, 5, 98, 5, 7, 5, 78, 56, 4, 3 ,65, 47, 5, 5, 78]

    print("Less that five elements in an array are :" , end=" ")
    # l.sort()
    less_five(l)
    
main()