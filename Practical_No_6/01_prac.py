# Read all content from a txt file

def main():
    try:
        with open('Practical_No_6/01_02_03_a.txt', 'r') as f:
            content = f.read()
        print(content)

    except FileNotFoundError:
        print("File was found in Folder")


main()