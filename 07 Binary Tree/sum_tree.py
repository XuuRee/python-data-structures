#!/usr/bin/env python3

# Povolene knihovny: copy, math
# Import jakekoli jine knihovny neprojde vyhodnocovaci sluzbou.
# To, ze jsou nejake knihovny povolene, neznamena, ze je nutne je pouzit.


# IB002 Domaci uloha 7.
#
# Souctovy strom je binarni strom, kde kazdy uzel ma nasledujici vlastnost:
# Pokud ma uzel alespon jednoho syna, potom je klic uzlu roven souctu klicu
# vsech jeho synu. Listy stromu tedy mohou obsahovat libovolne hodnoty.
# Za souctovy je povazovan i strom, ktery neobsahuje zadne uzly, a strom,
# ktery obsahuje prave jeden uzel.
#
# Muzete si samozrejme pridat vlastni pomocne funkce.
#
# Priklad:
# souctove stromy      nesouctove stromy
#   53       47            53       47
#  /  \        \          /  \     /
# 21  32       47        21  21   46
#             /  \                  \
#            1    46                 1

# Do nasledujicich definic trid nijak nezasahujte.
#
# Trida pro reprezentaci souctoveho stromu.
# root je koren stromu a je typu Node, nebo None, pokud je strom prazdny.
#
# Pro vykreslovani stromu muzete pouzit funkci make_graph z cv07.

class SumTree:
    def __init__(self):
        self.root = None


# Trida pro reprezentaci uzlu v souctovem strome.
# key je hodnota uzlu, ktera ma byt rovna souctu hodnot vsech synu.

class Node:
    def __init__(self):
        self.key = 0
        self.left = None
        self.right = None


# Ukol 1.
# Vasim prvnim ukolem je napsat funkci, ktera vybuduje uplny souctovy strom ze
# zadaneho pole. Listy stromu budou prave prvky pole v poradi zleva doprava.
# Delka pole bude vzdy mocninou dvojky.
#
# Napriklad:
# Z pole [1,2,3,4] vznikne strom:
#      10
#    /    \
#   3      7
#  / \    / \
# 1   2  3   4


def create_node(key):
    node = Node()
    node.key = key
    return node


def create_nodes_array(array):
    array_nodes = []
    for key in array:
        array_nodes.append(create_node(key))
    return array_nodes


def create_sum_tree(array):
    length = len(array)
    if length == 1:
        return array[0]
    next_level = []
    for i in range(0, length, 2):
        node = create_node(array[i].key + array[i + 1].key)
        node.left, node.right = array[i], array[i + 1]
        next_level.append(node)
    return create_sum_tree(next_level)


def build_sum_tree(array):
    """
    vstup: pole (Pythonovsky seznam) 'array' cisel delky 'n',
           kde 'n' je nejaka mocnina dvojky
    vystup: korektni strom typu SumTree, ktery ma v listech (v poradi zleva
            doprava) hodnoty ze zadaneho pole 'array'
            strom musi byt uplny, tj. vsechna jeho patra musi byt zcela
            zaplnena
    casova slozitost: O(n)
    """
    sum_tree = SumTree()
    sum_tree.root = create_sum_tree(create_nodes_array(array))
    return sum_tree


# Ukol 2.
# Vasim druhym ukolem je napsat funkci is_sum_tree, ktera overi, zda je strom
# souctovy. Pokud ano, vraci True, jinak False.


def check_sum_tree(root):
    if root is None:
        return True
    if root.left is not None or root.right is not None:
        if root.key != (0 if root.left is None else root.left.key) + (0 if root.right is None else root.right.key):
            return False
    return check_sum_tree(root.left) and check_sum_tree(root.right)


def is_sum_tree(tree):
    """
    vstup: 'tree' typu SumTree
           (je zaruceno, ze uzly ve strome jsou typu Node;
            neni zaruceno, ze splnuji souctovou podminku)
    vystup: True, pokud je 'tree' korektni SumTree, tj. vsechny jeho uzly
                  splnuji souctovou podminku
            False, jinak
    casova slozitost: O(n), kde 'n' je pocet prvku 'tree'
    """
    return check_sum_tree(tree.root)


array = [1, 2, 3, 4]
tree = build_sum_tree(array)
print("        ", tree.root.key)
print("     ", tree.root.left.key, "   ", tree.root.right.key)
print("   ", tree.root.left.left.key, " ", tree.root.left.right.key, tree.root.right.left.key, " ", tree.root.right.right.key)
#tree.root.key = 21
print(is_sum_tree(tree))
tree_2 = SumTree()
node = Node()
node.key = 5
tree_2.root = node
print(is_sum_tree(tree_2))

print("----------------------------------")
s_node = Node()
s_node.key = 0
s_s_node = Node()
s_s_node.key = 0
s_node.right = s_s_node
tree_3 = SumTree()
tree_3.root = s_node
print(is_sum_tree(tree_3))
print("-----------------------------------")
node_1 = Node()
node_1.key = 1
node_2 = Node()
node_2.key = 1
node_3 = Node()
node_3.key = 0
node_1.left = node_2
node_2.left = node_3
tree_4 = SumTree()
tree_4.root = node_1
print(is_sum_tree(tree_4))