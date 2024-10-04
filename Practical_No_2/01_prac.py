# Check whether an entered character is a vowel or not

def is_vowel(c):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    if c.lower() in vowels:
        print("It is a vowel.")
    else:
        print("It is not a vowel.")

char = input("Enter a character to check if it is a vowel or not: ")

if len(char) == 1 and char.isalpha():
    is_vowel(char)
else:
    print("Please enter a single alphabetic character.")