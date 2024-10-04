# program to sort a dictionary by key.

def sort_dict(example_dict):
    return dict(sorted(example_dict.items()))
    # return dict(sorted(example_dict.items(), key=lambda item: item[1])) # for sorting by value

def main():
    example_dict = {
        2 : 'Apple',
        4 : 'Banana',
        1 : 'Pear',
        3 : 'Orange'
    }

    sorted_dict = sort_dict(example_dict)
    print(sorted_dict)
    
main()