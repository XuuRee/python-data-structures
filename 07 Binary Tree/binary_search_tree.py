#!/usr/bin/env python3

# Povolene knihovny: copy, math
# Import jakekoli jine knihovny neprojde vyhodnocovaci sluzbou.
# To, ze jsou nejake knihovny povolene, neznamena, ze je nutne je pouzit.


# IB002 Domaci uloha 9.
#
# V teto uloze se budeme zabyvat binarnimi vyhledavacimi stromy.
#
# V prvni casti bude Vasi ulohou sestavit skoro uplny binarni vyhledavaci strom
# obsahujici zadane klice. Vstupni pole klicu bude usporadano od nejmensich po
# nejvetsi. Vas algoritmus musi mit LINEARNI casovou slozitost vzhledem k poctu
# zadanych klicu. Tento pozadavek je splnitelny diky usporadanosti pole na
# vstupu.
#
# V druhe casti bude Vasi ulohou zjistit, jestli zadany binarni vyhledavaci
# strom je skoro uplny. Pozadovana casova slozitost je linearni vuci poctu uzlu
# ve strome.
#
# Ve treti casti bude Vasi ulohou zjistit, jestli zadany binarni vyhledavaci
# strom ma vsechny listy ve stejne hloubce. Pozadovana casova slozitost je opet
# linearni vuci poctu uzlu ve strome.
#
# Skoro uplny strom ma zaplnena vsechna patra, jen posledni nemusi byt uplne
# zaplneno (a rovnez nemusi byt doleva zarovnane).
#
# Pro ilustraci, pro vstup (1,2,3,4,5,6,7,8,9,10) je korektnim vystupem
# algoritmu z prvni casti napriklad jeden z nasledujicich stromu:
#
#             ( 5 )                           ( 7 )
#            /     \                         /     \
#          (2)     (8)                  ( 4 )       ( 9 )
#         /  \     /  \                /     \      /   \
#       (1)  (3) (6)  (9)            (2)     (6)  (8)   (10)
#              \   \    \            / \     /
#              (4) (7)  (10)       (1) (3) (5)


# Do nasledujicich definic trid nijak nezasahujte.
# Pro vykreslovani stromu muzete pouzit dodanou funkci make_graph nize.

class BSTree:
    """Trida BSTree pro reprezentaci binarniho vyhledavacicho stromu.

    Atributy:
        root   koren stromu typu Node, nebo None, pokud je strom prazdny
    """

    def __init__(self):
        self.root = None


class Node:
    """Trida Node pro reprezentaci uzlu binarniho vyhledavaciho stromu.

    Atributy:
        data    hodnota daneho uzlu (zadana pri inicializaci)
        left    odkaz na leveho potomka typu Node, nebo None, pokud neexistuje
        right   odkaz na praveho potomka typu Node, nebo None, pokud neexistuje
    """

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


# Ukol 1.
# Implementuje funkci build_bst, ktera dostane vzestupne serazeny seznam hodnot
# a vytvori z nich skoro uplny binarni vyhledavaci strom (typu BSTree).


def build_bst_rec(array, start, end):
    """ Build almost complete tree. """
    if start > end:
        return None
    mid = (start + end) // 2
    node = Node(array[mid])
    node.left = build_bst_rec(array, start, mid - 1)
    node.right = build_bst_rec(array, mid + 1, end)
    return node


def build_bst(array):
    """
    vstup: 'array' vzestupne serazene pole hodnot
    vystup: strom typu BSTree, ktery je skoro uplny (viz vyse) a obsahuje
            hodnoty z pole array
    casova slozitost: O(n), kde 'n' je delka array
    extrasekvencni prostorova slozitost:
         O(1), nepocitame do ni ovsem vstupni pole ani vystupni strom
    """
    tree = BSTree()
    tree.root = build_bst_rec(array, 0, len(array) - 1)
    return tree


# Ukol 2.
# Implementujte funkci check_almost_complete, ktera dostane binarni vyhledavaci
# strom a otestujte, zda je skoro uplny.


def tree_height_n(node):
    """ Return tree height. """
    if node is None:
        return -1
    left = tree_height_n(node.left)
    right = tree_height_n(node.right)
    return max(left, right) + 1


def check_almost_complete_rec(node, depth, height):
    """ Check if given tree is almost complete tree recursively. """
    if depth >= height - 1:
        return True
    if node.left is None or node.right is None:
        return False
    return check_almost_complete_rec(node.left, depth + 1, height) \
           and \
           check_almost_complete_rec(node.right, depth + 1, height)


def check_almost_complete(tree):
    """
    vstup: 'tree' binarni vyhledavaci strom typu BSTree
    vystup: True, pokud je 'tree' skoro uplny
            False, jinak
    casova slozitost: O(n), kde 'n' je pocet uzlu stromu
    extrasekvencni prostorova slozitost: O(1) (nepocitame vstup)
    """
    if tree.root is None:
        return True
    height = tree_height_n(tree.root)
    return check_almost_complete_rec(tree.root, 0, height)


# Ukol 3.
# Implementujte funkci check_all_leaves_same_depth, ktera overi, zda jsou
# vsechny listy zadaneho binarniho vyhledavaciho stromu ve stejne hloubce.


class Storage:

    def __init__(self):
        self.level = None


def check_all_leaves_same_depth_rec(node, depth, storage):
    if node is None:
        return True
    if node.left is None and node.right is None:
        if storage.level is None:
            storage.level = depth
            return True
        return depth == storage.level
    return check_all_leaves_same_depth_rec(node.left, depth + 1, storage) \
           and \
           check_all_leaves_same_depth_rec(node.right, depth + 1, storage)


def check_all_leaves_same_depth(tree):
    """
    vstup: 'tree' binarni vyhledavaci strom typu BSTree
    vystup: True, pokud jsou vsechny listy 'tree' ve stejne hloubce
            False, jinak
    casova slozitost: O(n), kde 'n' je pocet uzlu stromu
    extrasekvencni prostorova slozitost: O(1) (nepocitame vstup)
    """
    return check_all_leaves_same_depth_rec(tree.root, 0, Storage())


# Pomocna funkce make_graph vygeneruje .dot soubor na zaklade stromu predaneho
# v argumentu. Cilem funkce je jen zobrazit aktualni stav daneho uzlu a jeho
# potomku, nijak nekontroluje jestli se jedna o BVS.
#
# Na vygenerovany soubor si bud najdete nastroj, nebo pouzijte odkazy:
# http://sandbox.kidstrythisathome.com/erdos/ nebo http://www.webgraphviz.com/
#
# Staci zkopirovat obsah souboru do formulare webove stranky.

def make_graph(tree, filename="bst.dot"):
    def dot_node(fd, node):
        if node is None:
            return

        fd.write('{} [label="{}"]\n'.format(id(node), node.data))

        for child, lr in (node.left, 'L'), (node.right, 'R'):
            dot_node(fd, child)
            dot_node_relations(fd, node, child, lr)

    def dot_node_relations(fd, parent, node, direction):
        if node is None:
            nil = direction + str(id(parent))
            fd.write('{} [label="",color=white]\n{} -> {}\n'
                     .format(nil, id(parent), nil))
        else:
            fd.write('{} -> {}\n'.format(id(parent), id(node)))

    with open(filename, "w") as fd:
        fd.write("digraph {\n")
        fd.write("node [color=lightblue2,style=filled]\n")
        dot_node(fd, tree.root)
        fd.write("}\n")


##################################################################
# TESTS
##################################################################


bs_tree_0 = build_bst([0])

bs_tree_1 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

bs_tree_2 = build_bst([1, 1, 1, 1, 1, 2, 3, 3, 4, 5, 5, 5, 5, 6])

bs_tree_3 = BSTree()

node_0 = Node(0)
node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)

node_1.left = node_0
node_1.right = node_2
node_2.right = node_3
node_3.right = node_4

bs_tree_3.root = node_1

bs_tree_4 = BSTree()

node_1_1 = Node(1)
node_1_2 = Node(2)
node_1_3 = Node(3)

node_1_1.right = node_1_2
node_1_2.right = node_1_3

bs_tree_4.root = node_1_1

print(tree_height_n(bs_tree_0.root))
print(tree_height_n(bs_tree_1.root))
print(tree_height_n(bs_tree_2.root))
print(tree_height_n(bs_tree_3.root))
print(tree_height_n(bs_tree_4.root))

print("Check if binary tree is almost complete tree")

print(check_almost_complete(bs_tree_0))     # true
print(check_almost_complete(bs_tree_1))     # true
print(check_almost_complete(bs_tree_2))     # true
print(check_almost_complete(bs_tree_3))     # false
print(check_almost_complete(bs_tree_4))     # false

print("Check if all leaves of binary tree have same depth")

print(check_all_leaves_same_depth(bs_tree_0))   # true
print(check_all_leaves_same_depth(bs_tree_1))   # false
print(check_all_leaves_same_depth(bs_tree_2))   # true
print(check_all_leaves_same_depth(bs_tree_3))   # false
print(check_all_leaves_same_depth(bs_tree_4))   # true
