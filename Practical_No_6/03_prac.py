# program to read last 'n' lines of the file

def print_last_n(file , n):
    with open(file , 'r') as f:
        content = f.readlines()
    return content[-n:]

def main():
    file_path = 'Practical_No_6/01_02_03_a.txt'
    n = int(input("Enter n : "))

    last_n = print_last_n(file_path , n)

    for last in last_n:
        print(last)

main()