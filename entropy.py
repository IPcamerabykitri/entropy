import math
from collections import Counter

def calculate_entropy(symbol_list):
    entropy = 0
    total_symbol_count = float(len(symbol_list))
    values_symbol = Counter(symbol_list).values() # counts the elements' frequency

    for symbol_count in values_symbol:
        percentage = symbol_count/total_symbol_count
        reverse_percentage = total_symbol_count/symbol_count
        entropy += percentage * math.log(reverse_percentage,2)

    return entropy

'''if __name__ == "__main__":
    test_list = []
    for i in range (0,1000) :
        if i == 2:
            for j in range(0,100):
                test_list.append(i)
        if i == 3:
            for j in range(0,10):
                test_list.append(i)
        if i == 4:
            for j in range(0,25):
                test_list.append(i)
        if i == 5:
            for j in range(0,100):
                test_list.append(i)
        else :
            test_list.append(i)
    print(test_list)
    print(calculate_entropy(test_list))'''