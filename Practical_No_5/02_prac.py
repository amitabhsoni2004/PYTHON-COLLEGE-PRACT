# To concat two dictionary which create new dictionary

def concat_dict(dict1 , dict2):
    dict3 = {**dict1 , **dict2}
    return dict3

def main():
    dict1 = {
        1 : 'Amitabh',
        2 : 'Ajay',
        3 : 'Ankit',
    }

    dict2 = {
        5 : 'Soni',
        8 : 'Gupta',
        9 : 'Mourya',
    }


    dict3 = concat_dict(dict1, dict2)
    print(f"Merged dict : {dict3}")
main()