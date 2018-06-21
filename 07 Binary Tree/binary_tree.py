#!/usr/bin/env python3
import math


class Node:
    """Trida Node slouzi k reprezentaci uzlu ve strome.

    Atributy:
        key     klic daneho uzlu
        parent  reference na rodice uzlu (None, pokud neexistuje)
        left    reference na leveho potomka (None, pokud neexistuje)
        right   reference na praveho potomka (None, pokud neexistuje)
    """

    def __init__(self):
        self.key = None
        self.parent = None
        self.right = None
        self.left = None


class BinarySearchTree:
    """Trida BinarySearchTree slouzi k reprezentaci binarniho vyhledavaciho
    stromu.

    Atributy:
        root    reference na korenovy uzel typu Node
    """

    def __init__(self):
        self.root = None


def insert(tree, key):
    """Vlozi novy uzel s klicem 'key' do stromu 'tree'."""
    node = Node()
    node.key = key
    parent = None
    current = tree.root

    while current is not None:
        parent = current
        current = current.left if node.key < current.key else current.right

    node.parent = parent

    if parent is None:
        tree.root = node
    elif node.key < parent.key:
        parent.left = node
    else:
        parent.right = node


def search_rec(node, key):
    if node is None or node.key == key:
        return node

    if node.key > key:
        return search_rec(node.left, key)

    return search_rec(node.right, key)


def search(tree, key):
    """Vyhleda uzel s klicem 'key' ve strome 'tree'. Vrati uzel s hledanym
    klicem. Pokud se klic 'key' ve strome nenachazi, vraci None.
    """
    return search_rec(tree.root, key)


def transplant(tree, u, v):
    if u.parent is None:
        tree.root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v

    if v is not None:
        v.parent = u.parent


def minimum(node):
    if node is None:
        return None

    while node.left is not None:
        node = node.left

    return node


def delete(tree, node):
    """Smaze uzel 'node' ze stromu 'tree' a obnovi vlastnost vyhledavaciho
    stromu.
    """
    if node.left is None:
        transplant(tree, node, node.right)
    elif node.right is None:
        transplant(tree, node, node.left)
    else:
        y = minimum(node.right)
        if y.parent != node:
            transplant(tree, y, y.right)
            y.right = node.right
            node.right.parent = y
        transplant(tree, node, y)
        y.left = node.left
        node.left.parent = y


def height_rec(node):
    if node is None:
        return -1

    return 1 + max(height_rec(node.left), height_rec(node.right))


def height(tree):
    """Vraci vysku stromu 'tree'."""
    return height_rec(tree.root)


def is_correct_bst_rec(node, min_val, max_val):
    if node is None:
        return True

    if node.key < min_val or node.key > max_val:
        return False

    return (is_correct_bst_rec(node.left, min_val, node.key) and
            is_correct_bst_rec(node.right, node.key, max_val))


def is_correct_bst(tree):
    """Overi, zdali je strom 'tree' korektni binarni vyhledavaci strom.
    Pokud ano, vraci True, jinak False.
    """
    return is_correct_bst_rec(tree.root, -math.inf, math.inf)


# Dodatek k graphvizu:
# Graphviz je nastroj, ktery vam umozni vizualizaci datovych struktur,
# coz se hodi predevsim pro ladeni. Tento program generuje nekolik
# souboru neco.dot v mainu. Vygenerovane soubory nahrajte do online
# nastroje pro zobrazeni graphvizu:
# http://sandbox.kidstrythisathome.com/erdos/
# nebo http://www.webgraphviz.com/- zvlada i vetsi grafy.
#
# Alternativne si muzete nainstalovat prekladac z jazyka dot do obrazku
# na svuj pocitac.
def make_graphviz(node, f):
    if node is None:
        return

    f.write('"{}" [label="{}"]\n'.format(id(node), node.key))

    for child, lr in (node.left, 'L'), (node.right, 'R'):
        if child is not None:
            f.write('"{}" -> "{}"\n'.format(id(node), id(child)))
            make_graphviz(child, f)
        else:
            nil = lr + str(id(node))
            f.write('{} [label="",color=white]\n{} -> {}\n'
                    .format(nil, id(node), nil))


def make_graph(tree, filename):
    try:
        with open(filename, 'w') as f:
            f.write("digraph Tree {\n")
            f.write("node [color=lightblue2, style=filled];\n")
            if tree is not None and tree.root is not None:
                make_graphviz(tree.root, f)
            f.write("}\n")
        print("Vykresleny strom najdete v souboru", filename)
    except Exception:
        print("Ve vykreslovani nastala chyba")


def helper_test_insert(tree):
    insert(tree, 3)

    if tree.root is None or tree.root.key != 3:
        print("NOK - chybne vkladani do prazdneho stromu")
        return False

    insert(tree, 1)

    if tree.root.key != 3 or tree.root.left.key != 1:
        print("NOK - chybne vkladani do leveho podstromu")
        return False

    insert(tree, 5)

    if tree.root.key != 3 or tree.root.right.key != 5:
        print("NOK - chybne vkladani do praveho podstromu")
        return False

    insert(tree, 2)

    if tree.root.left.right.key != 2:
        print("NOK - chybne vkladani do leveho podstromu")
        return False

    insert(tree, 4)

    if tree.root.right.left.key != 4:
        print("NOK - chybne vkladani do praveho podstromu")
        return False

    print("OK")
    return True


def test_insert():
    print("Test 1. insert: ", end='')

    tree = BinarySearchTree()

    if not helper_test_insert(tree):
        make_graph(tree, "insert.dot")


def init_test_tree():
    tree = BinarySearchTree()

    nodes = [Node() for _ in range(7)]
    for i in range(7):
        nodes[i].key = i

    tree.root = nodes[3]

    tree.root.left = nodes[1]
    nodes[1].parent = tree.root
    nodes[1].left = nodes[0]
    nodes[0].parent = nodes[1]
    nodes[1].right = nodes[2]
    nodes[2].parent = nodes[1]

    tree.root.right = nodes[5]
    nodes[5].parent = tree.root
    nodes[5].left = nodes[4]
    nodes[4].parent = nodes[5]
    nodes[5].right = nodes[6]
    nodes[6].parent = nodes[5]

    return tree


def helper_test_delete(tree):
    delete(tree, tree.root.left.left)

    if tree.root.left.key != 1 or tree.root.left.left is not None:
        print("NOK - chybne mazani listu")
        return False

    delete(tree, tree.root)

    if (tree.root is None or tree.root.key != 4 or tree.root.left.key != 1 or
            tree.root.left.left is not None):
        print("NOK - chybne mazani korenu")
        return False

    delete(tree, tree.root.left)

    if tree.root.left.key != 2:
        print("NOK - chybne mazani uzlu v levem podstrome")
        return False

    print("OK")
    return True


def test_delete():
    print("Test 2. delete: ", end='')
    tree = init_test_tree()

    if not helper_test_delete(tree):
        make_graph(tree, "delete.dot")


def helper_test_search(tree):
    node = search(tree, 3)

    if node is None or node.key != 3:
        print("NOK - chybne hledani korene s hodnotou 3")
        return False

    node = search(tree, 2)

    if node is None or node.key != 2:
        print("NOK - chybne hledani listu s hodnotou 2")
        return False

    node = search(tree, 7)

    if node is not None:
        print("NOK - hledani prvku, ktery se ve strome nevyskytuje")
        return False

    print("OK")
    return True


def test_search():
    print("Test 3. search: ", end='')
    tree = init_test_tree()

    if not helper_test_search(tree):
        make_graph(tree, "search.dot")


def helper_test_height(tree):
    h = height(tree)

    if h != 2:
        print("NOK - vyska 2 != vase vyska {}".format(h))
        return False

    n = Node()
    n.key = 7
    tree.root.right.right.right = n
    n.parent = tree.root.left.right

    h = height(tree)

    if h != 3:
        print("NOK - vyska 3 != vase vyska {}".format(h))
        return False

    print("OK")
    return True


def test_height():
    print("Test 4. height: ", end='')
    tree = init_test_tree()

    if not helper_test_height(tree):
        make_graph(tree, "height.dot")


def helper_test_is_correct_bst(tree):
    if not is_correct_bst(tree):
        print("NOK - strom je korektni binarni vyhledavaci strom")
        return False

    tree.root.key = 0
    tree.root.left.left = None

    if is_correct_bst(tree):
        print("NOK - strom neni korektni binarni vyhledavaci strom")
        return False

    tree.root.key = 3
    tree.root.left.right.key = 4
    tree.root.right.left.key = 2

    if is_correct_bst(tree):
        print("NOK - strom neni korektni binarni vyhledavaci strom")
        return False

    print("OK")
    return True


def test_is_correct_bst():
    print("Test 5. is_correct_bst: ", end='')
    tree = init_test_tree()

    if not helper_test_is_correct_bst(tree):
        make_graph(tree, "correct.dot")


if __name__ == '__main__':
    test_insert()
    test_delete()
    test_search()
    test_height()
    test_is_correct_bst()
