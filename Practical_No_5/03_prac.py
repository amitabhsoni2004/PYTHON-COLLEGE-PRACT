# Sum all dictonary values 

def sum_dict_value(dict1):
    sum = 0
    print(f"Values are :",end=" ")
    for key, value in dict1.items():
        print(value , end= " ")
        sum += value
    print(f"\nSum of values : {sum}")



def main():
    dict1 = {
        1 : 20,
        2 : 30,
        3 : 40,
        4 : 60,
    }

    sum_dict_value(dict1)

main()