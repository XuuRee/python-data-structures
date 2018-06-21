#!/usr/bin/env python3


class Node:
    """Trida Node slouzi pro reprezentaci objektu v obousmerne
    spojovanem seznamu.

    Atributy:
        value   reprezentuje ulozenou hodnotu/objekt
        next    reference na nasledujici prvek v seznamu
        prev    reference na predchazejici prvek v seznamu
    """

    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None


class LinkedList:
    """Trida LinkedList reprezentuje spojovany seznam.

    Atributy:
        first   reference na prvni prvek seznamu
        last    reference na posledni prvek seznamu
    """

    def __init__(self):
        self.first = None
        self.last = None


def insert(linked_list, value):
    """Metoda insert() vlozi na konec seznamu linked_list (za prvek last)
    novy uzel s hodnotou value. Vraci nove vlozeny objekt.
    """
    n = Node()
    n.value = value
    n.prev = linked_list.last

    if linked_list.first is None:
        linked_list.first = n
    else:
        linked_list.last.next = n

    linked_list.last = n
    return n


def print_list(linked_list):
    """Metoda print_list() vypise seznam linked_list."""
    n = linked_list.first
    while n is not None:
        print(str(n.value) + ", ", end="")
        n = n.next
    print()


def search(linked_list, value):
    """Metoda search() vraci referenci na prvni vyskyt uzlu s hodnotou
    value v seznamu linked_list. Pokud se hodnota v seznamu nenachazi,
    vraci None.
    """
    n = linked_list.first
    while n is not None and n.value != value:
        n = n.next
    return n


def delete(linked_list, node):
    """Metoda delete() smaze uzel node v seznamu linked_list."""
    if node is None:
        return

    if node.prev is None:
        linked_list.first = node.next
    else:
        node.prev.next = node.next

    if node.next is None:
        linked_list.last = node.prev
    else:
        node.next.prev = node.prev


# Testy implementace
def test_insert_empty():
    print("Test 1. Vkladani do prazdneho seznamu: ", end="")

    l1 = LinkedList()
    insert(l1, 1)

    if l1.first is None or l1.last is None:
        print("FAIL")
        return

    if (l1.first.value == 1 and l1.last.value == 1 and
            l1.first.next is None and l1.first.prev is None):
        print("OK")
    else:
        print("FAIL")


def test_insert_nonempty():
    print("Test 2. Vkladani do neprazdneho seznamu: ", end="")

    l2 = LinkedList()
    n = Node()
    n.value = 1
    n.next = None
    l2.first = n
    l2.last = n

    insert(l2, 2)

    if l2.last is None:
        print("FAIL")
        return

    if (l2.last.value == 2 and l2.last.prev is not None and
            l2.last.prev == l2.first and l2.first.value == 1):
        print("OK")
    else:
        print("FAIL")


def test_search_exist():
    print("Test 3. Hledani existujiciho prvku v seznamu: ", end="")

    l3 = LinkedList()
    n1 = Node()
    n2 = Node()
    n1.value = 1
    n1.next = n2
    n1.prev = None
    n2.value = 2
    n2.next = None
    n2.prev = n1
    l3.first = n1
    l3.last = n2

    i = search(l3, 2)

    if i == n2:
        print("OK")
    else:
        print("FAIL")


def test_search_not_exist():
    print("Test 4. Hledani neexistujiciho prvku v seznamu: ", end="")

    l4 = LinkedList()
    n1 = Node()
    n2 = Node()
    n1.value = 1
    n1.next = n2
    n1.prev = None
    n2.value = 2
    n2.next = None
    n2.prev = n1
    l4.first = n1
    l4.last = n2

    i = search(l4, 3)

    if i is None:
        print("OK")
    else:
        print("FAIL")


def test_delete_first():
    print("Test 5. Odstraneni prvniho prvku v seznamu: ", end="")

    l5 = LinkedList()
    n1 = Node()
    n2 = Node()
    n1.value = 1
    n1.next = n2
    n1.prev = None
    n2.value = 2
    n2.next = None
    n2.prev = n1
    l5.first = n1
    l5.last = n2

    delete(l5, n1)

    if l5.first == n2 and n2.prev is None:
        print("OK")
    else:
        print("FAIL")


def test_delete_mid():
    print("Test 6. Odstraneni prostredniho prvku v seznamu: ", end="")

    l6 = LinkedList()
    n1 = Node()
    n2 = Node()
    n3 = Node()
    n1.value = 1
    n1.next = n2
    n1.prev = None
    n2.value = 2
    n2.next = n3
    n2.prev = n1
    n3.value = 3
    n3.next = None
    n3.prev = n2
    l6.first = n1
    l6.last = n3

    delete(l6, n2)

    if l6.last != n3 or l6.last.prev != n1 or l6.first.next != n3:
        print("FAIL")
    else:
        print("OK")


def test_delete_last():
    print("Test 7. Odstraneni posledniho prvku v seznamu: ", end="")

    l7 = LinkedList()
    n1 = Node()
    n2 = Node()
    n3 = Node()
    n1.value = 1
    n1.next = n2
    n1.prev = None
    n2.value = 2
    n2.next = n3
    n2.prev = n1
    n3.value = 3
    n3.next = None
    n3.prev = n2
    l7.first = n1
    l7.last = n3

    delete(l7, n3)

    if l7.last != n2 or l7.last.prev != n1 or l7.first.next != n2:
        print("FAIL")
    else:
        print("OK")


def test_delete_solo():
    print("Test 8. Odstraneni jedineho prvku v seznamu: ", end="")

    l8 = LinkedList()
    n1 = Node()
    n1.value = 1
    n1.next = None
    n1.prev = None
    l8.first = n1
    l8.last = n1

    delete(l8, n1)

    if l8.last is not None or l8.first is not None:
        print("FAIL")
    else:
        print("OK")


def test_insert_return():
    print("Test 9. Vraceni vlozeneho prvku: ", end="")

    l9 = LinkedList()
    n = insert(l9, 1)

    if n is None or n.value != 1:
        print("FAIL")
    else:
        print("OK")


if __name__ == '__main__':
    test_insert_empty()
    test_insert_nonempty()
    test_search_exist()
    test_search_not_exist()
    test_delete_first()
    test_delete_mid()
    test_delete_last()
    test_delete_solo()
    test_insert_return()
