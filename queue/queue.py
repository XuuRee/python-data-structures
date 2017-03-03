#!/usr/bin/python3

class Item:
    """Trida Item slouzi pro reprezentaci objektu ve fronte.

    Atributy:
        value   reprezentuje ulozenou hodnotu/objekt
        left    reference na predchazejici prvek ve fronte
    """
    def __init__(self):
        self.value = None
        self.left = None


class Queue:
    """Trida Queue reprezentuje frontu.

    Atributy:
        atribut first je reference na prvni prvek
        atribut last je reference na posledni prvek
    """
    def __init__(self):
        self.first = None
        self.last = None


def enqueue(queue, value):
    """Metoda enqueue vlozi do fronty (queue) novy prvek s hodnotou
    (value).
    """

    element = Item()
    
    element.value = value
    element.left = None

    if(queue.last == None):
        queue.first = element
    else:
        queue.last.left = element

    queue.last = element


def dequeue(queue):
    """Metoda dequeue odebere prvni prvek z fronty (queue).
    Vraci hodnotu (value) odebraneho prvku, pokud je fronta prazdna,
    vraci None
    """

    if(isEmpty(queue)):
        return None
    
    value = queue.first.value
    tmp = queue.first

    if(queue.first == queue.last):
        queue.first = None
        queue.last = None
    else:
        queue.first = queue.first.left

    return value


def isEmpty(queue):
    """isEmpty() vraci True v pripade prazdne fronty, jinak False."""

    if(queue.first == None):
        return True
    else:
        return False


# Tests
def test_enqueue_empty():
    print("Test 1. Insert to the empty queue: ", end="")

    q = Queue()
    enqueue(q, 1)

    if q.first is None or q.last is None:
        print("FAIL")
        return

    if (q.first.value is 1 and q.first.left is None and
            q.last.value is 1 and q.last.left is None):
        print("OK")
    else:
        print("FAIL")


def test_enqueue_nonempty():
    print("Test 2. Insert to the nonempty queue: "),

    q = Queue()
    i = Item()
    i.left = None
    i.value = 1
    q.first = i
    q.last = i

    enqueue(q, 2)

    if q.first is None or q.last is None:
        print("FAIL")
        return
    if q.last.value is 2 and q.first is i and q.first.left.value is 2:
        print("OK")
    else:
        print("FAIL")


def test_dequeue_empty():
    print("Test 3. Remove from empty queue: "),

    q = Queue()
    v = dequeue(q)

    if v is not None or q.first is not None or q.last is not None:
        print("FAIL")
    else:
        print("OK")


def test_dequeue_nonempty():
    print("Test 4. Remove from nonempty queue: "),

    q = Queue()
    i = Item()
    i.value = 1
    i.left = None
    q.first = i
    q.last = i

    v = dequeue(q)

    if v is not 1 or q.first is not None or q.last is not None:
        print("FAIL")
    else:
        print("OK")


def test_isEmpty_empty():
    print("Test 5. isEmpty on empty queue: "),

    q = Queue()

    if isEmpty(q):
        print("OK")
    else:
        print("FAIL")


def test_isEmpty_nonempty():
    print("Test 6. isEmpty on nonempty queue: "),

    q = Queue()
    i = Item()
    i.left = None
    i.value = 1
    q.first = i
    q.last = i

    if isEmpty(q):
        print("FAIL")
    else:
        print("OK")


if __name__ == '__main__':
    test_enqueue_empty()
    test_enqueue_nonempty()
    test_dequeue_empty()
    test_dequeue_nonempty()
    test_isEmpty_empty()
    test_isEmpty_nonempty()
