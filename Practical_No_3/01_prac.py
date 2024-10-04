# To check given string is pangram or not

def pangram(input_str):
    pan_string = "abcdefghijklmnopqrstuvwxyz"

    for i in pan_string:
        if i not in input_str.lower():
            return "Not a pangram"
    return "It is a pangram"


def main():
    input_str = input("Enter the string : ")

    p = pangram(input_str)
    print(p)

main()