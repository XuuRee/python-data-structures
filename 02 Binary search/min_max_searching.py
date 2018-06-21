#!/usr/bin/env python3
import random


# Vasim ukolem bude naimplementovat rekurzivni a iterativni verze algoritmu pro
# binarni vyhledavani a vyhledavani minima a maxima v poli. Dale pak bude
# Vasim ukolem prepsat zadanou rekurzivni funkci na iterativni verzi, pricemz
# budete muset pouzit zasobnik.
#
# U funkci na hledani dvojice minima a maxima nesmite pouzit vestavene funkce
# min a max (muzete je pouzivat na dvojice, ale ne na cele pole).
#
# U vsech funkci predpokladejte, ze pole array neni prazdne a ze left a right
# jsou korektni indexy do pole.


def binary_search_recursive(array, left, right, key):
    """
    Funkce rekurzivne ve vzestupne usporadanem poli 'array' vyhleda klic
    'key'. Hleda se pouze v rozsahu od indexu 'left' do indexu 'right'.
    Funkce vraci index nalezeneho prvku, pokud prvek v posloupnosti
    neni, vraci -1.
    """
    if left == right:
        return left if array[left] == key else -1

    mid = (left + right) // 2

    if key < array[mid]:
        return binary_search_recursive(array, left, mid - 1, key)

    if key > array[mid]:
        return binary_search_recursive(array, mid + 1, right, key)

    return mid


def binary_search_iterative(array, left, right, key):
    """Iterativni verze predesle funkce.
    Iterativni podobu napiste podle intuice.
    """
    while left < right:
        mid = (left + right) // 2
        if key < array[mid]:
            right = mid - 1
        elif key > array[mid]:
            left = mid + 1
        else:
            return mid

    return left if array[left] == key else -1


def min_max_two(first, second):
    """Pomocna funkce, vrati dvojici:
           (mensi ze zadanych prvku, vetsi ze zadanych prvku).
    K tomu potrebuje pouze jedno porovnani."""
    return (first, second) if first < second else (second, first)


def min_max_search_recursive(array, left, right):
    """Funkce vyhleda hodnoty minima a maxima v poli 'array' pomoci
    rozdeluj a panuj algoritmu.
    V poli se hleda v rozsahu od indexu 'left' do indexu 'right'.
    """
    if left == right:
        return array[left], array[left]  # zadne porovnani

    if left + 1 == right:
        return min_max_two(array[left], array[right])  # jedno porovnani

    mid = (left + right) // 2
    l_min, l_max = min_max_search_recursive(array, left, mid)
    r_min, r_max = min_max_search_recursive(array, mid + 1, right)

    return min(l_min, r_min), max(l_max, r_max)  # dve porovnani

    # kdyz si to dobre spocitate, zjistite, ze min_max_search_recursive
    # pouziva pro zpracovani pole s n prvky o neco vice nez 3n/2 porovnani
    # k zamysleni: tento kod se da upravit tak, aby vzdy pouzil nejvyse
    # ceil(3n / 2 - 2) porovnani (ceil = horni cela cast)


def min_max_search_iterative(array, left, right):
    """Iterativni verze predesle funkce. Iterativni podobu napiste podle
    intuice.
    Pokud chcete, muzete zkusit prepis do iterativni podoby pomoci
    zasobniku. Je to dobry trenink.
    Navodem by vam mohlo byt:
    http://www.codeproject.com/Articles/418776/How-to-replace-recursive-functions-using-stack-and
    """
    # klasicke reseni "najdu nezavisle minimum a maximum" pouziva (2n - 2)
    # porovnani; toto reseni pouzije vzdy ceil(3n / 2 - 2) porovnani

    if left == right:
        return array[left], array[left]  # zadne porovnani

    c_min, c_max = min_max_two(array[left], array[left + 1])  # 1 porovnani

    for i in range(left + 2, right, 2):  # iterace po dvojicich prvku
        new_min, new_max = min_max_two(array[i], array[i + 1])  # 1 porovnani
        c_min = min(c_min, new_min)  # 1 porovnani
        c_max = max(c_max, new_max)  # 1 porovnani

    if (right - left + 1) % 2 == 1:
        # lichy prvek
        c_min = min(c_min, array[right])  # 1 porovnani
        c_max = max(c_max, array[right])  # 1 porovnani

    return c_min, c_max


def fractal_recursive(n):
    """Tato funkce vypisuje radu cisel, ktera pripomina fraktal.
    Vasim ukolem je prepsat ji bez pomoci rekurze, viz nize.
    Vstupem je prirozene (tj. nezaporne cele) cislo n."""
    if n == 0:
        print(n, end=" ")
        return

    print(n, end=" ")
    fractal_recursive(n - 1)
    print(n, end=" ")
    fractal_recursive(n - 1)
    print(n, end=" ")


def fractal_iterative(n):
    """Iterativni verze predesle funkce. K implementaci pouzijte zasobnik.
    Jako zasobnik poslouzi Pythonovsky seznam:
    - push se provede seznam.append(prvek)
    - pop se provede seznam.pop() a vrati odebrany prvek
    - jako test neprazdnosti staci pouze seznam (tj. if seznam, while seznam)
    """
    stack = [(n, 0)]

    while stack:
        n, count = stack.pop()
        print(n, end=" ")
        if n != 0 and count < 2:
            stack.append((n, count + 1))
            stack.append((n - 1, 0))


# Nize nasleduji testy.
def test_binary_search_recursive():
    print("Test 1. rekurzivni vyhledavani, prvek v poli neni:")
    array1 = [i for i in range(100)]
    ret = binary_search_recursive(array1, 0, 99, 100)
    if ret == -1:
        print("OK")
    else:
        print("NOK, v [0..99] se 100 nevyskytuje,")
        print("vracite {} != -1".format(ret))

    print("Test 2. rekurzivni vyhledavani, prvek v poli je na konci:")
    array2 = [i for i in range(100)]
    ret = binary_search_recursive(array2, 0, 99, 99)
    if ret == 99:
        print("OK")
    else:
        print("NOK, v [0..99] je 99 na pozici 99")
        print("vracite {} != 99".format(ret))

    print("Test 3. rekurzivni vyhledavani, prvek v poli je na zacatku:")
    array3 = [i for i in range(100)]
    ret = binary_search_recursive(array3, 0, 99, 0)
    if ret == 0:
        print("OK")
    else:
        print("NOK, v [0..99] je 0 na pozici 0")
        print("vracite {} != 0".format(ret))

    print("Test 4. rekurzivni vyhledavani, prvek v poli je kdekoliv:")
    array4 = [i for i in range(100)]
    ret = binary_search_recursive(array4, 0, 99, 33)
    if ret == 33:
        print("OK")
    else:
        print("NOK, v [0..99] je 33 na pozici 33")
        print("vracite {} != 33".format(ret))

    print("Test 5. rekurzivni vyhledavani, nahodne prvky:")
    array5 = []
    for i in range(100):
        array5.append(random.randint(1, 1000000000))
    array5.sort()
    ret = binary_search_recursive(array5, 0, 99, array5[68])
    if ret == 68:
        print("OK")
    else:
        print("NOK, v posloupnosti se hledal klic 68. prvku")
        print("vracite {} != 68".format(ret))


def test_binary_search_iterative():
    print("\nTest 6. iterativni vyhledavani, prvek v poli neni:")
    array1 = [i for i in range(100)]
    ret = binary_search_iterative(array1, 0, 99, 100)
    if ret == -1:
        print("OK")
    else:
        print("NOK, v [0..99] se 100 nevyskytuje,")
        print("vracite {} != -1".format(ret))

    print("Test 7. iterativni vyhledavani, prvek v poli je na konci:")
    array2 = [i for i in range(100)]
    ret = binary_search_iterative(array2, 0, 99, 99)
    if ret == 99:
        print("OK")
    else:
        print("NOK, v [0..99] je 99 na pozici 99")
        print("vracite {} != 99".format(ret))

    print("Test 8. iterativni vyhledavani, prvek v poli je na zacatku:")
    array3 = [i for i in range(100)]
    ret = binary_search_iterative(array3, 0, 99, 0)
    if ret == 0:
        print("OK")
    else:
        print("NOK, v [0..99] je 0 na pozici 0")
        print("vracite {} != 0".format(ret))

    print("Test 9. iterativni vyhledavani, prvek v poli je kdekoliv:")
    array4 = [i for i in range(100)]
    ret = binary_search_iterative(array4, 0, 99, 33)
    if ret == 33:
        print("OK")
    else:
        print("NOK, v [0..99] je 33 na pozici 33")
        print("vracite {} != 33".format(ret))

    print("Test 10. iterativni vyhledavani, nahodne prvky:")
    array5 = []
    for i in range(100):
        array5.append(random.randint(1, 1000000000))
    array5.sort()
    ret = binary_search_iterative(array5, 0, 99, array5[68])
    if ret == 68:
        print("OK")
    else:
        print("NOK, v posloupnosti se hledal klic 68. prvku")
        print("vracite {} != 68".format(ret))


def test_min_max_search_recursive():
    print("\nTest 11. rekurzivni vyhledavani minima a maxima v poli [1]:")
    array1 = [1]
    ret = min_max_search_recursive(array1, 0, 0)
    if ret == (1, 1):
        print("OK")
    else:
        print("NOK, v poli [1] je min 1 a max 1,")
        print("vracite {} != (1, 1)".format(ret))

    print("Test 12. rekurzivni vyhledavani minima a maxima v poli [2, 1]:")
    array2 = [2, 1]
    ret = min_max_search_recursive(array2, 0, 1)
    if ret == (1, 2):
        print("OK")
    else:
        print("NOK, v poli [2, 1] je min 1 a max 2,")
        print("vracite {} != (1, 2)".format(ret))

    print("Test 13. rekurzivni vyhledavani minima a maxima v poli [0..99]:")
    array3 = [i for i in range(100)]
    ret = min_max_search_recursive(array3, 0, 99)
    if ret == (0, 99):
        print("OK")
    else:
        print("NOK, v poli [0..99] je min 0 a max 99,")
        print("vracite {} != (0, 99)".format(ret))

    print("Test 14. rekurzivni vyhledavani minima a maxima v poli",
          "nahodnych cisel:")
    array4 = [random.randint(1, 1000) for i in range(100)]
    array4[21] = 0
    array4[45] = 1001
    ret = min_max_search_recursive(array4, 0, 99)
    if ret == (0, 1001):
        print("OK")
    else:
        print("NOK, v poli je min 0 a max 1001,")
        print("vracite {} != (0, 1001)".format(ret))

    print("Test 15. rekurzivni vyhledavani minima a maxima v poli",
          "nahodnych cisel (opakujici se minimum a maximum):")
    array5 = [random.randint(1, 1000) for i in range(100)]
    array5[21] = 0
    array5[61] = 0
    array5[42] = 1001
    array5[45] = 1001
    ret = min_max_search_recursive(array5, 0, 99)
    if ret == (0, 1001):
        print("OK")
    else:
        print("NOK, v poli je min 0 a max 1001,")
        print("vracite {} != (0, 1001)".format(ret))


def test_min_max_search_iterative():
    print("\nTest 16. iterativni vyhledavani minima a maxima v poli [1]:")
    array1 = [1]
    ret = min_max_search_iterative(array1, 0, 0)
    if ret == (1, 1):
        print("OK")
    else:
        print("NOK, v poli [1] je min 1 a max 1,")
        print("vracite {} != (1, 1)".format(ret))

    print("Test 17. iterativni vyhledavani minima a maxima v poli [2, 1]:")
    array2 = [2, 1]
    ret = min_max_search_iterative(array2, 0, 1)
    if ret == (1, 2):
        print("OK")
    else:
        print("NOK, v poli [2, 1] je min 1 a max 2,")
        print("vracite {} != (1, 2)".format(ret))

    print("Test 18. iterativni vyhledavani minima a maxima v poli [0..99]:")
    array3 = [i for i in range(100)]
    ret = min_max_search_iterative(array3, 0, 99)
    if ret == (0, 99):
        print("OK")
    else:
        print("NOK, v poli [0..99] je min 0 a max 99,")
        print("vracite {} != (0, 99)".format(ret))

    print("Test 19. iterativni vyhledavani minima a maxima",
          "v poli nahodnych cisel:")
    array4 = [random.randint(1, 1000) for i in range(100)]
    array4[21] = 0
    array4[45] = 1001
    ret = min_max_search_iterative(array4, 0, 99)
    if ret == (0, 1001):
        print("OK")
    else:
        print("NOK, v poli je min 0 a max 1001,")
        print("vracite {} != (0, 1001)".format(ret))

    print("Test 20. iterativni vyhledavani minima a maxima v poli",
          "nahodnych cisel (opakujici se minimum a maximum):")
    array5 = [random.randint(1, 1000) for i in range(100)]
    array5[21] = 0
    array5[61] = 0
    array5[42] = 1001
    array5[45] = 1001
    ret = min_max_search_iterative(array5, 0, 99)
    if ret == (0, 1001):
        print("OK")
    else:
        print("NOK, v poli je min 0 a max 1001,")
        print("vracite {} != (0, 1001)".format(ret))


def test_fractal():
    print("\nTest 21. iterativni verze funkce fractal:")
    print("Porovnejte shodu nasledujicich radku:")
    for n in range(5):
        print("\nfractal_recursive({}):".format(n), end=" ")
        fractal_recursive(n)
        print("\nfractal_iterative({}):".format(n), end=" ")
        fractal_iterative(n)
        print()


if __name__ == '__main__':
    test_binary_search_recursive()
    test_binary_search_iterative()
    test_min_max_search_recursive()
    test_min_max_search_iterative()
    test_fractal()
