import random

def quicksort(list):
    if len(list) == 1 or len(list) == 0 :
        return list 
    
    half = len(list) // 2
    pivot = list[half]
    left = []
    right = []
    middle = []
    for element in list:
        if pivot > element:
            left.append(element)
        elif pivot < element:
            right.append(element)
        else:
            middle.append(element)
    print(list)
    print(pivot)
    print(left,middle,right)
    print("-------------------")
    sorted = quicksort(left) + middle + quicksort(right) 
    return sorted

n = input("Eleman sayısı gir: ")
list = [random.randint(1,100) for i in range(int(n))]
print(quicksort(list))

