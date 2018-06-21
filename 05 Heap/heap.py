#!/usr/bin/env python3
import math

# V nasledujicim textu pouzivame pojem "halda" ve vyznamu "binarni halda".


class MinHeap:
    """Trida MinHeap slouzi k reprezentaci minimove haldy.

    Atributy:
        size    pocet prvku v halde
        array   pole prvku haldy
    """

    def __init__(self):
        self.size = 0
        self.array = []


# Implementujte nasledujici funkce pro ziskani prvku v halde:
# POZOR: Nezapomente, ze indexujeme pole od 0.

def parent_index(i):
    """Vrati index rodice prvku na pozici 'i'.
    Pokud neexistuje, vrati None.
    """
    return (i - 1) // 2 if i > 0 else None


def left_index(i):
    """Vrati index leveho potomka prvku na pozici 'i'."""
    return i * 2 + 1


def right_index(i):
    """Vrati index praveho potomka prvku na pozici 'i'."""
    return i * 2 + 2


def parent(heap, i):
    """Vrati rodice prvku na pozici 'i' v halde 'heap'.
    Pokud neexistuje, vrati None.
    """
    return heap.array[parent_index(i)] if parent_index(i) is not None else None


def left(heap, i):
    """Vrati leveho potomka prvku na pozici 'i' v halde 'heap'.
    Pokud neexistuje, vrati None.
    """
    return heap.array[left_index(i)] if left_index(i) < heap.size else None


def right(heap, i):
    """Vrati praveho potomka prvku na pozici 'i' v halde 'heap'.
    Pokud neexistuje, vrati None.
    """
    return heap.array[right_index(i)] if right_index(i) < heap.size else None


def swap(heap, i, j):
    """Prohodi prvky na pozicich 'i' a 'j' v halde 'heap'."""
    heap.array[i], heap.array[j] = heap.array[j], heap.array[i]


def heapify(heap, i):
    """Opravi haldu 'heap' tak aby splnovala vlastnost minimove haldy.
    Kontrola zacina u prvku na pozici 'i'.
    Haldu opravujeme pouze smerem dolu (k listum).
    """
    smallest = i
    if left_index(i) < heap.size and left(heap, i) < heap.array[smallest]:
        smallest = left_index(i)
    if right_index(i) < heap.size and right(heap, i) < heap.array[smallest]:
        smallest = right_index(i)
    if smallest != i:
        swap(heap, i, smallest)
        heapify(heap, smallest)


def build_heap(array):
    """Vytvori korektni minimovou haldu z pole 'array'.
    Pro zjednoduseni smite modifikovat existujici pole 'array'.
    """
    heap = MinHeap()
    heap.size = len(array)
    heap.array = array
    for i in reversed(range(heap.size // 2)):
        heapify(heap, i)
    return heap


def decrease_key(heap, i, value):
    """Snizi hodnotu prvku haldy 'heap' na pozici 'i' na hodnotu 'value'
    a opravi vlastnost haldy 'heap'.
    """
    if heap.array[i] < value:
        return  # Nova hodnota je vetsi nez puvodni!
    heap.array[i] = value
    while (parent(heap, i) is not None and
            i >= 0 and
            parent(heap, i) > heap.array[i]):
        swap(heap, i, parent_index(i))
        i = parent_index(i)


def insert(heap, value):
    """Vlozi hodnotu 'value' do haldy 'heap'."""
    heap.size += 1
    heap.array.append(math.inf)
    decrease_key(heap, heap.size - 1, value)


def extract_min(heap):
    """Odstrani minimalni prvek haldy 'heap'. Vraci hodnotu odstraneneho
    prvku. Pokud je halda prazdna, vraci None.
    """
    if (heap.size == 0):    # empty heap
        return None
    minimum = heap.array[0]
    heap.array[0] = heap.array[heap.size - 1]
    heap.size -= 1
    heap.array.pop()
    heapify(heap, 0)
    return minimum


def heap_sort(array):
    """Seradi pole 'array' pomoci haldy od nejvetsiho prvku po nejmensi.
    Vraci serazene pole.
    """
    heap = build_heap(array)
    for i in reversed(range(heap.size)):
        swap(heap, 0, i)
        heap.size -= 1
        heapify(heap, 0)
    return array


# Graphviz funkce.
# Vytvori haldu jako graf ve formatu ".dot"."""
#
# Dodatek k graphvizu:
# Graphviz je nastroj, ktery vam umozni vizualizaci datovych struktur,
# coz se hodi predevsim pro ladeni. Tento program generuje nekolik
# souboru neco.dot v mainu. Vygenerovane soubory nahrajte do online
# nastroje pro zobrazeni graphvizu:
# http://sandbox.kidstrythisathome.com/erdos/
# nebo http://www.webgraphviz.com/ - zvlada i vetsi grafy.
#
# Alternativne si muzete nainstalovat prekladac z jazyka dot do obrazku
# na svuj pocitac.
def make_graphviz(heap, i, f):
    f.write('"{}"\n'.format(heap.array[i]))
    if (left_index(i) < heap.size):
        f.write('"{}" -> "{}"\n'.format(heap.array[i], left(heap, i)))
        make_graphviz(heap, left_index(i), f)
    if (right_index(i) < heap.size):
        f.write('"{}" -> "{}"\n'.format(heap.array[i], right(heap, i)))
        make_graphviz(heap, right_index(i), f)


def make_graph(heap, filename):
    with open(filename, 'w') as f:
        f.write("digraph Heap {\n")
        f.write("node [color=lightblue2, style=filled];\n")
        if heap.size > 0:
            make_graphviz(heap, 0, f)
        f.write("}\n")


def test_indices():
    print("Test 1. indexovani parent, left, right: "),
    if (parent_index(2) != 0 or
            parent_index(1) != 0 or
            parent_index(0) is not None):
        print("NOK - chybny parent_index")
        return False
    if left_index(0) != 1 or left_index(3) != 7:
        print("NOK - chybny left_index")
        return False
    if right_index(0) != 2 or right_index(3) != 8:
        print("NOK - chybny right_index")
        return False

    heap = MinHeap()
    heap.array = [1, 2, 3]
    heap.size = len(heap.array)
    try:
        if (parent(heap, 0) is not None or
                parent(heap, 1) != 1 or
                parent(heap, 2) != 1):
            print("NOK - chyba ve funkci parent")
            return False
        if left(heap, 0) != 2 or left(heap, 1) is not None:
            print("NOK - chyba ve funkci left")
            return False
        if right(heap, 0) != 3 or right(heap, 1) is not None:
            print("NOK - chyba ve funkci right")
            return False
    except IndexError:
        print("NOK - pristup mimo pole")
        return False
    print("OK")
    return True


def test_build_heap():
    print("Test 2. build_heap: "),
    array = [4, 3, 1]
    heap = build_heap(array)
    if (heap.array == [1, 3, 4] or heap.array == [1, 4, 3]) and heap.size == 3:
        print("OK")
        return
    else:
        print("NOK - chyba ve funkci build_heap")
    try:
        make_graph(heap, "build.dot")
        print("Vykreslenou haldu najdete v souboru build.dot")
    except Exception:
        print("Chyba ve vykreslovani,",
              "je potreba mit spravne nastavenou heap.size")


def helper_test_insert_heap(heap):
    insert(heap, 2)
    if heap.array != [2] or heap.size != 1:
        print("NOK - chyba ve funkci insert na prazdne halde")
        return False

    insert(heap, 3)
    insert(heap, 4)
    if heap.array != [2, 3, 4] or heap.size != 3:
        print("NOK - chyba ve funkci insert na neprazdne halde")
        return False

    insert(heap, 5)
    if heap.array != [2, 3, 4, 5] or heap.size != 4:
        print("NOK - chyba ve funkci insert na neprazdne halde")
        return False

    insert(heap, 1)
    if heap.array != [1, 2, 4, 5, 3] or heap.size != 5:
        print("NOK - chyba ve funkci insert na neprazdne halde")
        return False

    print("OK")
    return True


def test_insert_heap():
    print("Test 3. insert_heap: "),
    heap = MinHeap()
    heap.array = []
    heap.size = 0

    if helper_test_insert_heap(heap):
        return

    try:
        make_graph(heap, "insert.dot")
        print("Vykreslenou haldu najdete v souboru insert.dot")
    except Exception:
        print("Chyba ve vykreslovani, ", end="")
        print("je potreba mit spravne nastavenou heap.size")


def test_decrease_key():
    print("Test 4. decrease_key: "),
    heap = MinHeap()
    heap.array = [2, 3, 4]
    heap.size = 3
    decrease_key(heap, 2, 1)

    if heap.array != [1, 3, 2] or heap.size != 3:
        print("NOK - chyba ve funkci decrease_key")
    else:
        decrease_key(heap, 0, 4)
        if heap.array != [1, 3, 2] or heap.size != 3:
            print("NOK - chyba ve funkci decrease_key")
        else:
            print("OK")
            return
    try:
        make_graph(heap, "decrease.dot")
        print("Vykreslenou haldu najdete v souboru decrease.dot")
    except Exception:
        print("Chyba ve vykreslovani, ", end="")
        print("je potreba mit spravne nastavenou heap.size")


def helper_test_extract_min(heap):
    tmp = extract_min(heap)

    if heap.array != [3, 5, 4] or tmp != 2:
        print("NOK - chyba ve funkci extract_min")
        return False

    tmp = extract_min(heap)
    if heap.array != [4, 5] or tmp != 3:
        print("NOK - chyba ve funkci extract_min")
        return False

    tmp = extract_min(heap)
    if heap.array != [5] or tmp != 4:
        print("NOK - chyba ve funkci extract_min")
        return False

    tmp = extract_min(heap)
    if heap.array != [] or tmp != 5:
        print("NOK - chyba ve funkci extract_min")
        return False

    try:
        if extract_min(heap) is None:
            print("OK")
            return True
    except Exception:
        print("NOK - chyba ve funkci extract_min na prazne halde")
        return False


def test_extract_min():
    print("Test 5. extract_min: "),
    heap = MinHeap()
    heap.array = [2, 3, 4, 5]
    heap.size = 4

    if helper_test_extract_min(heap):
        return

    try:
        make_graph(heap, "extract.dot")
        print("Vykreslenou haldu najdete v souboru extract.dot")
    except Exception:
        print("Chyba ve vykreslovani, ", end="")
        print("je potreba mit spravne nastavenou heap.size")


def test_heap_sort():
    array = [8, 4, 9, 3, 2, 7, 5, 0, 6, 1]
    print("Test 6. heap_sort: "),
    if heap_sort(array) != [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]:
        print("NOK - chyba ve funkci heap_sort, vraci neserazene pole")
    else:
        print("OK")


if __name__ == '__main__':
    if test_indices():
        test_build_heap()
        test_decrease_key()
        test_insert_heap()
        test_extract_min()
        test_heap_sort()
