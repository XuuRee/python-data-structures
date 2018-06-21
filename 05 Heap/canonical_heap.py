#!/usr/bin/env python3


# IB002 Domaci uloha 6.
#
# V nasledujicim textu pouzivame pojem "halda" ve vyznamu "binarni halda".
#
# Minimova halda je v kanonickem tvaru, pokud pro kazdy jeji prvek se dvema
# potomky plati, ze jeho levy potomek je mensi nez ten pravy nebo se oba
# rovnaji.
#
# Je v kanonickem tvaru | Neni v kanonickem tvaru
#                       |
#       (1)             |           (1)
#      /   \            |          /   \
#    (2)   (3)          |        (3)   (2)


# Trida representujici minimovou haldu. Pro praci s ni muzete s vyhodou pouzit
# funkce, ktere jste implementovali v zakladnim domacim ukolu.

class MinHeap:
    def __init__(self):
        self.size = 0
        self.array = []


# Ukol 1.
# Vasim prvnim ukolem je implementovat funkci is_canonical_min_heap(heap),
# ktera overi, zda je zadana halda 'heap' korektni minimovou haldou
# v kanonickem tvaru. Pokud ano, vrati True, v opacnem pripade vrati False.
#
# Prazdna nebo jednoprvkova halda je v kanonickem tvaru implicitne. Mejte na
# pameti, ze halda v kanonickem tvaru musi splnovat take pozadavky kladene na
# minimovou haldu.

def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


def is_min_heap(heap, i):
    left, right = 2 * i + 1, 2 * i + 2
    if right < len(heap):
        if heap[left] < heap[i] or heap[right] < heap[i]:
            return False
        return is_min_heap(heap, left) and is_min_heap(heap, right)
    elif left < len(heap):
        if heap[left] < heap[i]:
            return False
        return is_min_heap(heap, left)
    else:
        return True


def is_canonical_min_heap(heap):
    """
    vstup: 'heap' typu MinHeap
           (je zaruceno, ze heap.size je velikost pole heap.array;
            neni zaruceno, ze prvky heap.array splnuji haldovou podminku
            nebo podminku kanonickeho tvaru)
    vystup: True, pokud je 'heap' minimova halda v kanonickem tvaru
            False, jinak
    casova slozitost: O(n), kde 'n' je pocet prvku 'heap'
    """
    if heap is None:
        return False
    if heap.size == 1 or heap.size == 0:
        return True
    if not is_min_heap(heap.array, 0):
        return False
    i = 1
    left = heap.array[1]
    while i < heap.size:
        if i % 2 == 1:
            left = heap.array[i]
            i += 1
            continue
        if left > heap.array[i]:
            return False
        i += 1
    return True


# Ukol 2.
# Druhym ukolem je implementovat funkci canonise_min_heap(heap), ktera zadanou
# minimovou haldu 'heap' prevede na kanonicky tvar. Funkce bude menit primo
# haldu zadanou v argumentu, proto nebude vracet zadnou navratovou hodnotu.
#
# Napoveda:
# Pro algoritmus s linearni casovou slozitosti je potreba postupovat takto:
# - Rekurzivne resime od korene k listum haldy;
# - pro kazdy uzel haldy:
#   + zkontrolujeme, jestli potomci splnuji vlastnost kanonickeho tvaru;
#     pokud ne:
#     * prohodime hodnoty leveho a praveho potomka;
#     * tim se muze pokazit vlastnost haldy v pravem podstrome, proto
#       probublame problematickou hodnotu z korene praveho podstromu
#       tak hluboko, aby uz neporusovala vlastnost haldy (pri tomto bublani
#       opravujeme pouze vlastnost haldy, kanonicky tvar neresime)
#   + mame tedy korektni minimovou haldu, ktera navic splnuje kanonicky
#     tvar od tohoto uzlu smerem nahoru;
#   + pokracujeme v rekurzi vlevo a vpravo.


def choose_smaller_number(heap, first, second):
    if heap.array[first] < heap.array[second]:
        return first
    return second


def check_subtree(heap, parent):
    left, right = 2 * parent + 1, 2 * parent + 2
    if left >= heap.size and right >= heap.size:
        return
    if left < heap.size and right >= heap.size:
        if heap.array[parent] > heap.array[left]:
            swap(heap.array, parent, left)
            return
    if left < heap.size and right < heap.size:
        position = choose_smaller_number(heap, left, right)
        if heap.array[parent] > heap.array[position]:
            swap(heap.array, position, parent)
            check_subtree(heap, position)


def canonise_min_heap(heap):
    """
    vstup: 'heap' korektni minimova halda typu MinHeap
    vystup: funkce nic nevraci, vstupni halda 'heap' je prevedena
            do kanonickeho tvaru (pritom obsahuje stejne prvky jako na zacatku)
    casova slozitost: O(n), kde 'n' je pocet prvku 'heap'
    """
    if is_min_heap(heap.array, 0):
        for i in range(heap.size // 2):
            left, right = 2 * i + 1, 2 * i + 2
            if left < heap.size and right < heap.size:
                if heap.array[left] > heap.array[right]:
                    swap(heap.array, left, right)
                    check_subtree(heap, right)


heap = MinHeap()

heap.array = [1, 3, 2]
heap.size = 3
if is_canonical_min_heap(heap):
    print(heap.array, " = IS canonical heap")
else:
    print(heap.array, " = IS NOT canonical heap")
    canonise_min_heap(heap)
    print(heap.array, " = REPAIRED")
    if is_canonical_min_heap(heap):
        print(" = TEST OK")
    else:
        print(" = TEST NOK")
print("-----------------------------------------")


heap.array = [-1, 0, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, -1]
heap.size = 14
if is_canonical_min_heap(heap):
    print(heap.array, " = IS canonical heap")
else:
    print(heap.array, " = IS NOT canonical heap")
    canonise_min_heap(heap)
    print(heap.array, " = REPAIRED")
    if is_canonical_min_heap(heap):
        print(" = TEST OK")
    else:
        print(" = TEST NOK")
print("-----------------------------------------")


heap.array = [-2, 0, -2, 0, 0, -1, -2]
heap.size = 7
if is_canonical_min_heap(heap):
    print(heap.array, " = IS canonical heap")
else:
    print(heap.array, " = IS NOT canonical heap")
    canonise_min_heap(heap)
    print(heap.array, " = REPAIRED")
    if is_canonical_min_heap(heap):
        print(" = TEST OK")
    else:
        print(" = TEST NOK")
print("-----------------------------------------")


heap.array = [-1, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, -1]
heap.size = 12
if is_canonical_min_heap(heap):
    print(heap.array, " = IS canonical heap")
else:
    print(heap.array, " = IS NOT canonical heap")
    canonise_min_heap(heap)
    print(heap.array, " = REPAIRED")
    if is_canonical_min_heap(heap):
        print(" = TEST OK")
    else:
        print(" = TEST NOK")
print("-----------------------------------------")


heap.array = [1, 3, 2, 4, 5, 9, 7, 6, 8]
heap.size = 9
if is_canonical_min_heap(heap):
    print(heap.array, " = IS canonical heap")
else:
    print(heap.array, " = IS NOT canonical heap")
    canonise_min_heap(heap)
    print(heap.array, " = REPAIRED")
    if is_canonical_min_heap(heap):
        print(" = TEST OK")
    else:
        print(" = TEST NOK")
print("-----------------------------------------")


heap.array = [0, 1, 0, 1, 1, 0]
heap.size = 6
if is_canonical_min_heap(heap):
    print(heap.array, " = IS canonical heap")
else:
    print(heap.array, " = IS NOT canonical heap")
    canonise_min_heap(heap)
    print(heap.array, " = REPAIRED")
    if is_canonical_min_heap(heap):
        print(" = TEST OK")
    else:
        print(" = TEST NOK")
print("-----------------------------------------")


heap.array = [0, 1, 0, 1, 1, 0, 0]
heap.size = 7
if is_canonical_min_heap(heap):
    print(heap.array, " = IS canonical heap")
else:
    print(heap.array, " = IS NOT canonical heap")
    canonise_min_heap(heap)
    print(heap.array, " = REPAIRED")
    if is_canonical_min_heap(heap):
        print(" = TEST OK")
    else:
        print(" = TEST NOK")
print("-----------------------------------------")


heap.array = [0, 1, 0, 1, 1, 0, 1]
heap.size = 7
if is_canonical_min_heap(heap):
    print(heap.array, " = IS canonical heap")
else:
    print(heap.array, " = IS NOT canonical heap")
    canonise_min_heap(heap)
    print(heap.array, " = REPAIRED")
    if is_canonical_min_heap(heap):
        print(" = TEST OK")
    else:
        print(" = TEST NOK")
print("-----------------------------------------")