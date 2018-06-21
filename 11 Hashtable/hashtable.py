#!/usr/bin/env python3


class Node:
    """Trida Node slouzi pro reprezentaci objektu v obousmerne
    spojovanem seznamu.

    Atributy:
        pair    reprezentuje ulozenou dvojici (klic, data)
        next    reference na nasledujici prvek v seznamu
        prev    reference na predchazejici prvek v seznamu
    """

    def __init__(self):
        self.pair = None
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


class HashPair:
    """Trida reprezentujici dvojici klice 'key' a hodnoty 'data'."""

    def __init__(self, key, data):
        self.key = key
        self.data = data


SIZE = 10   # velikost hasovaci tabulky


class HashTable:
    """Trida HashTable reprezentujici hasovaci tabulku.

    Atributy:
        table   pole zretezenych seznamu
                zretezene seznamy obsahuji dvojice HashPair,
                ktere jsou indexovany podle indexu pole
    """

    def __init__(self):
        self.table = [LinkedList() for x in range(SIZE)]


def insert_linked_list(linked_list, pair):
    """Metoda insert_linked_list vlozi na konec (za prvek last) seznamu
    novy uzel s hodnotou pair.
    """
    node = Node()
    node.pair = pair
    node.prev = linked_list.last
    if linked_list.first is None:
        linked_list.first = node
    else:
        linked_list.last.next = node
    linked_list.last = node


def search_linked_list(linked_list, key):
    """Metoda search_linked_list vraci referenci na prvni vyskyt uzlu
    s klicem 'key'. Pokud se hodnota v seznamu nenachazi, vraci None.
    """
    node = linked_list.first
    while node is not None and node.pair.key is not key:
        node = node.next
    return node


def delete_linked_list(linked_list, node):
    """Metoda delete_linked_list smaze uzel node ze seznamu."""
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


def hash(key):
    """Funkce vypocita hodnotu hasovaci funkce pro klic 'key'
    na zaklade velikosti tabulky.
    Hashovaci funkce f(n) = n mod 'SIZE'
    """
    return key % SIZE


def insert_hashtable(hashtable, key, data):
    """Vytvori dvojici 'HashPair' z hodnot 'key' a 'data'. Pote vlozi
    vytvorenu dvojici do tabulky.
    """
    pair = HashPair(key, data)  # vkladana dvojice do tabulky
    insert_linked_list(hashtable.table[hash(key)], pair)


def get_hashtable(hashtable, key):
    """Najde dvojici s klicem 'key' a vrati klici prirazenou
    hodnotu 'data'. Pokud se klic v tabulce nenachazi, vraci None.
    """
    node = search_linked_list(hashtable.table[hash(key)], key)
    if node is None:
        return None

    return node.pair.data


def remove_hashtable(hashtable, key):
    """Odstrani prvni vyskyt dvojice s klicem 'key'."""
    linked_list = hashtable.table[hash(key)]
    node = search_linked_list(linked_list, key)
    if node is not None:
        delete_linked_list(linked_list, node)


def keys_hashtable(hashtable):
    """Vrati seznam vsech klicu v tabulce."""
    keys = []
    for linked_list in hashtable.table:
        node = linked_list.first
        while node is not None:
            keys.append(node.pair.key)
            node = node.next
    return keys


def values_hashtable(hashtable):
    """Vrati seznam vsech hodnot v tabulce."""
    values = []
    for linked_list in hashtable.table:
        node = linked_list.first
        while node is not None:
            values.append(node.pair.data)
            node = node.next
    return values


# Testy implementace

def test_hash():
    print("Test 1. hasovaci funkce (hash): ")

    for key in 10, 5323, 65321:
        if hash(key) != key % SIZE:
            print("NOK - nekorektni hasovani.")
            print("Vase hodnota {} != {}".format(hash(key), key % SIZE))
            return

    print("OK")


def test_insert():
    print("Test 2. vkladani do tabulky (insert):")
    t = HashTable()
    key = SIZE - 1
    value = 'A'
    insert_hashtable(t, key, value)
    if t.table[key % SIZE].first is None:
        print("NOK - nekorektni vkladani do tabulky")
        print("V tabulce je po vlozeni None")
        return
    if t.table[key % SIZE].first.pair.data != value:
        print("NOK - nekorektni vkladani do tabulky")
        print("Na pozici hash({}) se na prvni pozici ".format(key), end="")
        print("v seznamu nenachazi hodnota '{}'".format(value))
        print("Ve vasi tabulce se na pozici hash({}) ".format(key), end="")
        print("nachazi '{}'".format(t.table[key % SIZE].first.pair.data))
        return
    key = SIZE * 2
    value = 'B'
    insert_hashtable(t, key, value)
    if t.table[key % SIZE].first is None:
        print("NOK - nekorektni vkladani do tabulky")
        print("V tabulce je po vlozeni None")
        return
    if t.table[key % SIZE].first.pair.data != value:
        print("NOK - nekorektni vkladani do tabulky")
        print("Na pozici hash({}) se na prvni pozici ".format(key), end="")
        print("v seznamu nenachazi hodnota '{}'".format(value))
        print("Ve vasi tabulce se na pozici hash({}) ".format(key), end="")
        print("nachazi '{}'".format(t.table[key % SIZE].first.pair.data))
        return
    key = 2 * SIZE - 1
    value = 'C'
    insert_hashtable(t, key, value)
    if t.table[key % SIZE].first is None:
        print("NOK - nekorektni vkladani do tabulky")
        print("V tabulce je po vlozeni None")
        return
    if t.table[key % SIZE].first.next is None:
        print("NOK - nekorektni vkladani do tabulky")
        print("V tabulce je po vlozeni None")
        return
    if t.table[key % SIZE].first.next.pair.data != value:
        print("NOK - nekorektni vkladani do tabulky")
        print("Na pozici hash({}) se na prvni pozici ".format(key), end="")
        print("v seznamu nenachazi hodnota '{}'".format(value))
        print("Ve vasi tabulce se na pozici hash({}) ".format(key), end="")
        print("nachazi '{}'".format(t.table[key % SIZE].first.next.pair.data))
        return
    key = 0
    value = 'D'
    insert_hashtable(t, key, value)
    if t.table[key % SIZE].last is None:
        print("NOK - nekorektni vkladani do tabulky")
        print("V tabulce je po vlozeni None")
        return
    if t.table[key % SIZE].last.pair.data != value:
        print("NOK - nekorektni vkladani do tabulky")
        print("Na pozici hash({}) se na prvni pozici ".format(key), end="")
        print("v seznamu nenachazi hodnota '{}'".format(value))
        print("Ve vasi tabulce se na pozici hash({}) ".format(key), end="")
        print("nachazi '{}'".format(t.table[key % SIZE].last.pair.data))
        return
    print("OK")


def init_table():
    t = HashTable()
    p1 = HashPair(0, 'A')
    p2 = HashPair(SIZE, 'B')
    p3 = HashPair(1, 'C')
    p4 = HashPair(2 * SIZE, 'D')
    p5 = HashPair(2 * SIZE - 2, 'E')

    insert_linked_list(t.table[0], p1)
    insert_linked_list(t.table[0], p2)
    insert_linked_list(t.table[0], p4)
    insert_linked_list(t.table[1], p3)
    insert_linked_list(t.table[SIZE - 2], p5)
    return t


def check_get(res, correct):
    if res != correct:
        print("NOK - nekorektni hledani v tabulce")
        print("Tabulka vraci {} != {}".format(res, correct))

    return res == correct


def test_get():
    print("Test 3. hledani v tabulce (get):")
    t = init_table()

    res = get_hashtable(t, 0)
    if not check_get(res, 'A'):
        return

    res = get_hashtable(t, SIZE)
    if not check_get(res, 'B'):
        return

    res = get_hashtable(t, 1)
    if not check_get(res, 'C'):
        return

    res = get_hashtable(t, 2 * SIZE)
    if not check_get(res, 'D'):
        return

    res = get_hashtable(t, 2 * SIZE - 2)
    if not check_get(res, 'E'):
        return

    res = get_hashtable(t, 3 * SIZE - 2)
    if not check_get(res, None):
        return

    res = get_hashtable(t, SIZE - 3)
    if not check_get(res, None):
        return

    print("OK")


def test_remove():
    print("Test 4. odstranovani z tabulky (remove):")
    t = init_table()
    key = 1
    remove_hashtable(t, key)
    if t.table[key % SIZE].first is not None:
        print("NOK - nekorektni odebirani prvku s klicem {}".format(key))
        return
    key = 2 * SIZE - 2
    remove_hashtable(t, key)
    if t.table[key % SIZE].first is not None:
        print("NOK - nekorektni odebirani prvku s klicem {}".format(key))
        return
    key = 0
    remove_hashtable(t, key)
    if (t.table[key % SIZE].first is None or
            t.table[key % SIZE].first.pair.data != 'B'):
        print("NOK - nekorektni odebirani prvku s klicem {}".format(key))
        return
    key = 2 * SIZE
    remove_hashtable(t, key)
    if (t.table[key % SIZE].first is None or
            t.table[key % SIZE].first.pair.data != 'B'):
        print("NOK - nekorektni odebirani prvku s klicem {}".format(key))
        return
    key = SIZE
    remove_hashtable(t, key)
    if t.table[key % SIZE].first is not None:
        print("NOK - nekorektni odebirani prvku s klicem {}".format(key))
        return
    print("OK")


def test_keys():
    print("Test 5. seznam klicu (keys):")
    t = HashTable()
    res = []
    k = keys_hashtable(t)
    if k != res:
        print("NOK - nekorektni vypis klicu {}".format(res))
        print("Vas vystup: {}".format(k))
        return

    t = init_table()
    k = keys_hashtable(t)
    res = [0, SIZE, 2 * SIZE, 1, 2 * SIZE - 2]
    if k != res:
        print("NOK - nekorektni vypis klicu {}".format(res))
        print("Vas vystup: {}".format(k))
        return

    p = HashPair(SIZE // 2, 'G')
    insert_linked_list(t.table[SIZE // 2], p)
    k = keys_hashtable(t)
    res = [0, SIZE, 2 * SIZE, 1, SIZE // 2, 2 * SIZE - 2]
    if k != res:
        print("NOK - nekorektni vypis klicu {}".format(res))
        print("Vas vystup: {}".format(k))
        return

    print("OK")


def test_values():
    print("Test 6. seznam hodnot (value):")
    t = HashTable()
    res = []
    k = values_hashtable(t)
    if k != res:
        print("NOK - nekorektni vypis hodnot {}".format(res))
        print("Vas vystup: {}".format(k))
        return

    t = init_table()
    k = values_hashtable(t)
    res = ['A', 'B', 'D', 'C', 'E']
    if k != res:
        print("NOK - nekorektni vypis hodnot {}".format(res))
        print("Vas vystup: {}".format(k))
        return

    p = HashPair(SIZE // 2, 'G')
    insert_linked_list(t.table[SIZE // 2], p)
    res = ['A', 'B', 'D', 'C', 'G', 'E']
    k = values_hashtable(t)
    if k != res:
        print("NOK - nekorektni vypis hodnot {}".format(res))
        print("Vas vystup: {}".format(k))
        return

    print("OK")


if __name__ == '__main__':
    test_hash()
    print()
    test_insert()
    print()
    test_get()
    print()
    test_remove()
    print()
    test_keys()
    print()
    test_values()
    print()
