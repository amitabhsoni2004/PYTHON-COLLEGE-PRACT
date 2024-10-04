# To find out length of given string

def len_string(str):
    # return len(str)
    c = 0
    for i in str:
        c = c + 1
    return c

def main():
    str = input("Enter a string to find length of it : ")
    print(f"The length of given string is : {len_string(str)}")

main()