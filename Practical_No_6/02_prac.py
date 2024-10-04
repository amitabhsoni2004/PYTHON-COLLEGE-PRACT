# append a text into file and display text

def append_data(data , file):
    try:
        with open(file , 'a+') as f:
            f.write('\n'+ data)
        print("Appended successfully")
    except IOError:
        print("Error hai")

def read_data(file):
    try:
        with open(file , 'r') as f:
            content = f.read()
        print(content)  
    except IOError:
        print("Error aaya")
    
def main():
    data = input("Enter data : ")
    file_path = 'Practical_No_6/01_02_03_a.txt'

    append_data(data , file_path)

    read_data(file_path)

main()