import random

def quicksort(list):
    if len(list) <= 1:
        return list 
    
    half = len(list) // 2
    pivot = list[half]
    left = [element for element in list if element < pivot]
    middle = [element for element in list if element == pivot]
    right = [element for element in list if element > pivot]
    print(list)
    print(pivot)
    print(left,middle,right)
    print("-------------------")
    sorted = quicksort(left) + middle + quicksort(right) 
    return sorted

n = input("Eleman sayısı gir: ")
list = [random.randint(1,100) for i in range(int(n))]
print(quicksort(list))


