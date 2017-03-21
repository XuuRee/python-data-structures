#!/usr/bin/python3

# IB002 Extra domaci ukol 3.
#
# Vasi ulohou bude s vyuzitim principu binarniho vyhledavani implementovat
# dve metody, find_first_occurrence a find_first_greater. V obou pripadech
# musi casova slozitost vaseho algoritmu byt nejhure logaritmicka, tedy byt
# v O(log n). (Pozor, iterovani v poli ma linearni slozitost.)
#
# Ukol 1.
# Implementujte metodu find_first_occurrence, ktera vrati index prvniho
# vyskytu prvku key v serazenem poli numbers. Pokud se prvek v poli
# nevyskytuje, vrati -1.
#
# Priklady vstupu a vystupu:
# find_first_occurrence(2, [1, 2, 2, 2, 4]) -->  1
# find_first_occurrence(3, [1, 2, 4, 5])    --> -1

def find_first_occurrence(key, numbers):
    low = 0
    high = len(numbers)

    while low < high:
        mid = (low + high) // 2
        if numbers[mid] < key:
            low = mid + 1
        elif numbers[mid] > key:
            high = mid
        elif mid > 0 and numbers[mid-1] == key:
            high = mid
        else:
            return mid

    return -1


# Ukol 2.
# Implementujte metodu find_first_greater modifikaci predchozi metody
# find_first_occurrence tak, ze find_first_greater vrati index prvniho prvku
# v poli vetsiho nez key. Neni-li v poli zadny takovy, vrati -1.
#
# Priklady vstupu a vystupu:
# find_first_greater(2, [1, 2, 4, 5]) -->  2
# find_first_greater(3, [1, 2, 4, 5]) -->  2
# find_first_greater(3, [1, 2, 3])    --> -1


def find_first_greater(key, numbers):
    low = 0
    high = len(numbers)
    
    while low < high:
        mid = (low + high) // 2
        if key < numbers[mid]:
            high = mid
        else:
            low = mid + 1

    if(low >= len(numbers)):
        return -1
    
    return low

