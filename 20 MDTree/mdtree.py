from __future__ import print_function  # kompatibilita s Python 2.7
from __future__ import division   # kompatibilita s Python 3 (pouze pro testy)
from collections import Counter
import sys

# Implementacni test IB002 2016 - MDTree (max 50 bodu)
#
# Vasi ulohou je implementovat nekolik funkci pro datovou strukturu "MDTree".
# Muzete si samozrejme pridat vlastni pomocne funkce.
#
# MDTree je rozsirenim binarniho vyhledavaciho stromu, kde kazdy vnitrni uzel
# obsahuje presne tri klice, zatimco kazdy list obsahuje jeden az tri klice.
# Klice v uzlech jsou vzestupne usporadany.
# Dale plati vyhledavaci vlastnosti, tj. pro kazdy uzel 'u' plati, ze
# vsechny klice v levem podstrome 'u' jsou mensi nez vsechny klice v 'u'
# a vsechny klice v pravem podstrome 'u' jsou vetsi nez vsechny klice v 'u'.
# Pro jednoduchost predpokladame, ze klice jsou unikatni, tj. ve strome nikdy
# nebudou existovat dva klice stejne hodnoty.
# MDTree nemusi byt vyvazeny strom.
#
# Priklady korektnich a nekorektnich MDTree:
#
#        [6,7,10]                  [6,7]                 [6,7,12]
#       /        \                /     \               /        \
#      /          \              /       \             /          \
# [1,3,4]         [15,18]   [1,3,4]      [15,18]   [1,3,4]         [11,15,18]
#        korektni                 nekorektni             nekorektni
#                         (jen dva klice v koreni)  (porusena vyhledavaci
#                                                               vlastnost)
#
#
# 1. cast (10 bodu): implementujte funkci getInterestingKeys.
# 2. cast (10 bodu): implementujte funkci isValidMDTree.
# 3. cast (15 bodu): implementujte funkci insert.
# 4. cast (15 bodu): implementujte funkci findSuccKey.
#
# Presny popis pozadovaneho chovani funkci je uveden u jejich hlavicek.


class MDTree:
    # Trida pro reprezentaci MDTree.
    #
    # 'root' je ukazatel na koren stromu typu Node (None pokud je strom
    # prazdny).
    #
    # Tridu si muzete libovolne rozsirovat, ale zavedene polozky zachovejte.

    def __init__(self):
        self.root = None


class Node:
    # Trida pro reprezentaci uzlu stromu MDTree.
    #
    # 'keys' je tripolozkove pole pro ukladani klicu.
    # 'size' je aktualni pocet platnych polozek v poli keys.
    # 'parent', 'left' a 'right' jsou ukazatele na rodice, leveho a praveho
    # potomka.
    #
    # Strukturu si muzete libovolne rozsirovat, ale zavedene polozky
    # zachovejte.
    #
    # Nove uzly se vytvareji pomoci 'node = Node()'.
    # Ve vlastnim zajmu nikdy nevolejte 'node.keys.append(key)'.

    def __init__(self):
        self.keys = 3 * [None]
        self.size = 0
        self.parent = None
        self.left = None
        self.right = None


# === POMOCNE FUNKCE ===

# Pomocna funkce, ktera zjisti, jestli dany uzel je listem (tj. nema zadne
# potomky). Vraci False, pokud je jejim vstupem None.


def isLeaf(node):
    return node is not None and node.left is None and node.right is None


# === 1. cast (10 bodu) ===
#
# Funkce getInterestingKeys ulozi do seznamu 'keyList' ze zadaneho stromu
# vsechny klice, ktere se nachazeji v tech uzlech, jejichz oba potomci jsou
# listy. Klice v seznamu musi byt ulozene vzestupne podle velikosti.
# Muzete predpokladat, ze strom je korektni MDTree a ze seznam 'keyList' je
# na zacatku prazdny.
#
# Nezapomente, ze mate k dispozici funkci isLeaf(node).
#
# Pro vkladani do seznamu 'keyList' pouzijte funkce keyList.append (pro
# pridavani po jednom) nebo keyList.extend (pro pridavani vice klicu naraz).
# Jinak 'keyList' nemodifikujte!
#
# Priklad: pro nasledujici strom ma byt vystupem seznam [8,9,10].
#         [4,5,6]
#        /       \
# [1,2,3]         [8,9,10]
#                /       \
#              [7]       [11]
#

def get_keys_recursion(node, keyList):
    if node is None:
        return
    get_keys_recursion(node.left, keyList)
    get_keys_recursion(node.right, keyList)
    if node.left is not None and node.right is not None:
        if isLeaf(node.left) and isLeaf(node.right):
            keyList.extend(node.keys)
    

def getInterestingKeys(tree, keyList):
    get_keys_recursion(tree.root, keyList)


# === 2. cast (10 bodu) ===
#
# Funkce isValidMDTree zkontroluje, zda je zadany strom korektni MDTree, tj.
# zda splnuje nasledujici podminky:
# - vnitrni uzly maji vzdy presne tri klice,
# - listy maji jeden az tri klice,
# - klice uvnitr uzlu jsou vzestupne serazeny,
# - strom splnuje vyhledavaci podminku (popsana nahore).
# Funkce vraci True, pokud je dany strom korektni, jinak vraci False.
# Muzete predpokladat, ze ukazatele left, right a parent jsou v uzlech
# nastaveny spravne a ze polozka size v uzlech odpovida poctu klicu
# a jeji hodnota je v rozmezi 0 az 3.
#

def is_valid_mdtree(node, left):
    if node is None:
        return True
    if isLeaf(node):
        if node.size < 1 or node.size > 3:
            return False
        if not right_order(node):
            return False
    else:
        if node.size != 3:
            return False
        if not right_order(node):
            return False
    if left is not None:
        if not subtree_order(node, left): 
            return False
    return is_valid_mdtree(node.left, True) and is_valid_mdtree(node.right, False)


def subtree_order(node, left):
    parent = node.parent
    if left:
        if parent.keys[0] < node.keys[node.size - 1]:
            return False
    else:
        if parent.keys[parent.size - 1] > node.keys[0]:
            return False
    return True


def right_order(node):
    if node.size == 1:
        return True
    if node.size == 2:
        return node.keys[0] < node.keys[1] 
    if node.size == 3:
        return node.keys[0] < node.keys[1] < node.keys[2]


def isValidMDTree(tree):
    return is_valid_mdtree(tree.root, None)


# === 3. cast (15 bodu) ===
#
# Funkce insert vlozi do zadaneho stromu zadany klic. Muzete predpokladat, ze
# zadany strom je korektni MDTree a zadany klic se dosud ve strome nevyskytuje.
#
# Vkladani probiha nasledovne:
# - Nejprve nalezneme uzel, do ktereho vkladany klic patri (aniz by se
#   porusila vyhledavaci vlastnost).
# - Pokud je nalezeny uzel listem a neni plny, klic do nej vlozime; pripadne
#   musime posunout existujici klice v uzlu.
# - Pokud je nalezeny uzel listem a je plny, musime vytvorit novy list.
# - Pokud je nalezeny uzel vnitrni, vlozime do nej klic, ale protoze nyni mame
#   ctyri klice, musime jeden z nich (maximum nebo minimum) vlozit do jednoho
#   z podstromu. Pokud je tento podstrom prazdny, musime v nem vytvorit novy
#   list.
#
# Vsimnete si, ze v nekterych pripadech existuje vic moznosti, jak pokracovat
# (vytvaret novy list vlevo nebo vpravo, vkladat do leveho nebo praveho
# podstromu). Zde volbu nechavame na vas. Podstatne je, aby byl vysledny
# strom korektni MDTree a obsahoval spravne klice. Slozitost teto funkce nesmi
# byt vyssi nez linearni vuci _vysce stromu_.
#
# Nezapomente spravne upravit polozky uzlu, napr. size.
# Pro vytvareni novych uzlu pouzijte Node() (viz vyse).
#

def create_new_node(parent, key):
    node = Node()
    node.keys[0] = key
    node.size = 1
    if parent is not None:
        node.parent = parent
    return node


def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


def sort_node(array, n):
    if array[0] > array[1]:
        swap(array, 0, 1)
    if n == 3:
        if array[1] > array[2]:
            swap(array, 1, 2)


def insert_node_to_list(node, key):
    node.keys[node.size] = key
    node.size += 1
    sort_node(node.keys, node.size)
    if node.size > 3:
        right_key = node.keys.pop()
        create_new_node(node, right_key)


def node_in_range(node, parent, key):
    if node.size == 1:
        return True
    return key > node.keys[0] and key < node.keys[node.size - 1] 


def insert_recursive(node, parent, key):
    if node is None:
        if key < parent.keys[0]:
            parent.left = create_new_node(parent, key)
        else:
            parent.right = create_new_node(parent, key)
        return
    if node_in_range(node, parent, key):
        if isLeaf(node) and node.size < 3:
            insert_node_to_list(node, key)
            return
        else:
            node.keys.append(key)
            node.keys.sort()
            right_key = node.keys.pop()
            insert_recursive(node.right, node, right_key)
            return
    if key > node.keys[node.size - 1]:
        insert_recursive(node.right, node, key)
    else:
        insert_recursive(node.left, node, key)


def insert(tree, key):
    if tree.root is None:
        tree.root = create_new_node(None, key)
    else:
        insert_recursive(tree.root, None, key)


# === 4. cast (15 bodu) ===
#
# Funkce findSuccKey nalezne v danem MDTree naslednika klice 'key'. Naslednik
# je takovy klic stromu, ze je vetsi nez 'key' a ze vsech takovych je nejmensi.
# Pozor na to, ze samotny klic 'key' se ve strome muze, ale nemusi vyskytovat.
#
# Pokud v danem strome neni zadny naslednik zvoleneho klice, vrati funkce
# None.
#
# Pro dosazeni plneho poctu bodu nesmi byt slozitost teto funkce horsi nez
# linearni vuci _vysce stromu_.
#
# Muzete predpokladat, ze zadany strom je korektni MDTree.
#
# Priklad: naslednikem klice 7 v nasledujicim strome je 9,
#          naslednikem klice 1 v nasledujicim strome je 2,
#          naslednikem klice 5 v nasledujicim strome je 6.
#
#            [9, 10, 11]
#           /           \
#    [3,4,5]            [12]
#   /       \
# [2]       [6]
#
# Napoveda: Staci projit pouze jedinou vetev stromu.
# S vyhodou lze vyuzit funkce findRec, jejiz hlavicku mate k dispozici.

import sys


def findSuccKey(tree, key):
    if tree.root is None:
        return None
    candidate = sys.maxsize
    node = tree.root
    while node is not None:
        for i in range(node.size):
            if node.keys[i] > key and node.keys[i] < candidate:
                candidate = node.keys[i]
        if key >= node.keys[node.size - 1]:
            node = node.right
        else:
            node = node.left
    if candidate == sys.maxsize:
        return None
    return candidate


#
# Nasleduje kod testu, NEMODIFIKUJTE JEJ               ##
#

"""
Dodatek k graphvizu:
Graphviz je nastroj, ktery vam umozni vizualizaci datovych struktur,
coz se hodi predevsim pro ladeni.
Tento program generuje nekolik souboru neco.dot v mainu
Vygenerovane soubory nahrajte do online nastroje pro zobrazeni graphvizu:
http://sandbox.kidstrythisathome.com/erdos/
nebo http://graphviz-dev.appspot.com/ - zvlada i vetsi grafy

Alternativne si muzete nainstalovat prekladac z jazyka dot do obrazku na svuj
pocitac.
"""


def drawNode(node, f):
    if node is None:
        return
    f.write("\tnode%d [label=\"" % id(node))
    for i in range(node.size):
        f.write("%s%d" % ("|" if i else "", node.keys[i]))
    f.write("\"];\n")
    if node.left is not None:
        drawNode(node.left, f)
        f.write("\tnode%d:sw -> node%d;\n" % (id(node), id(node.left)))
    if node.right is not None:
        drawNode(node.right, f)
        f.write("\tnode%d:se -> node%d;\n" % (id(node), id(node.right)))


def drawMDTree(tree, fileName):
    f = open(fileName + ".dot", 'w')
    f.write("digraph MDTree {\n")
    f.write("\tnode [shape=record, height=0.3, width=0.3, fontsize=16];\n")
    if (tree is not None) and (tree.root is not None):
        drawNode(tree.root, f)
    f.write("}\n")
    f.close()


def real_size(keys):
    rsize = 0
    for key in keys:
        if key is not None:
            rsize += 1
    return rsize


def makeTree(treeList):
    tree = MDTree()
    nodes = []
    for i, keys in enumerate(treeList):
        if keys is None:
            if i == 0:
                tree.root = None
            nodes.append(None)
            continue
        else:
            node = Node()
            nodes.append(node)
            if i == 0:
                tree.root = node
            else:
                par = ((i + 1) // 2) - 1
                if i % 2 == 0:
                    nodes[par].right = node
                else:
                    nodes[par].left = node
                node.parent = nodes[par]
            node.keys = list(keys)
            for key in node.keys:
                if key is not None:
                    node.size += 1
    return tree


def getAllKeys(tree):
    l = []
    getAllKeysRec(tree.root, l)
    return l


def getAllKeysRec(node, l):
    if node is None:
        return

    for i in range(0, node.size):
        l.append(node.keys[i])

    getAllKeysRec(node.left, l)
    getAllKeysRec(node.right, l)


def testGetInterestingKeys():
    tests = [([None], [], "prazdny_strom"),
             ([[10, 12, 14]], [], "pouze_koren"),
             ([[10, 12, 14], [6, None, None], None], [], "pouze_jeden_list"),
             ([[10, 12, 14], [6, None, None], [20, None, None]],
             [10, 12, 14], "dva_listy"),
             ([[2, 4, 6], None, [30, 40, 50], None, None, [10, 12, 14], None,
               None, None, None, None, [
               6, None, None], [20, 22, None], None, None],
              [10, 12, 14], "hloubka_4"),
             ([[2, 4, 6], None, [30, 40, 50], None, None, [10, 12, 14],
               [60, 70, 80],
               None, None, None, None, [20, 22, None], None, None],
              [], "hloubka_4_no_interesting"),
             ([[2, 4, 6], None, [30, 40, 50], None, None, [10, 12, 14],
               [60, 70, 80],
               None, None, None, None, None, [55, None, None], None],
              [], "hloubka_4_no_interesting2"),
             ([[19, 21, 22], [10, 11, 12], [30, 32, 34],
               [4, 5, 6], [15, 16, 17], [25, 26, 27], [40, 41, 42],
                 [2, None, None], [8, None, None], [
                     13, None, None], [18, None, None],
               [24, None, None], [28, None, None], [36, 37, 38], [45, 46, 47],
               None, None, None, None, None, None, None, None,
               None, None, None, None,
               [35, None, None], [39, None, None], [44, None, None],
               [49, None, None]],
              [4, 5, 6, 15, 16, 17, 25, 26, 27, 36, 37, 38, 45, 46, 47],
              "velky_strom")
             # ([strom], [kluce], name),
             ]

    for treeRepr, interestingKeys, name in tests:
        tree = makeTree(treeRepr)
        answerKeys = []
        getInterestingKeys(tree, answerKeys)
        if answerKeys != interestingKeys:
            fname = "getInteresting_" + name
            drawMDTree(tree, fname)
            return (False,
                    "Vase odpoved: " + str(answerKeys),
                    "Ocekavane klice: " + str(interestingKeys),
                    fname + ".dot")
    return (True,)


def testIsValidMDTree():
    tests = [([None], True, "prazdny_strom"),
             ([[2, None, None]], True, "jeden_klic"),
             ([[3, 2, 4]], False, "spatne_poradi_klicu"),
             ([[2, 4, 3]], False, "spatne_poradi_klicu"),
             ([[10, 12, 14], [6, None, None], None], True, "jeden_list"),
             ([[10, 12, 14], [6, None, None], [20, 22, 23]],
             True, "maly_strom"),
             ([[10, 8, 12], [6, None, None], [16, 18, 20]], False,
              "spatne_poradi_klicu_v_koreni"),
             ([[8, 10, 12], [6, None, None], [18, 16, None]], False,
              "spatne_poradi_klicu_v_listu"),
             ([[8, 10, 12], [None, None, None], [16, 18, 20]], False,
              "spatny_pocet_klicu_v_listu"),
             ([[8, 10, None], [6, None, None], [16, 18, 20]], False,
              "spatny_pocet_klicu_v_koreni"),
             ([[19, 21, 22], [10, 11, 12], [30, 32, 34],
               [4, 5, 6], [15, 16, 17], [25, 26, 27], [40, 41, 42],
                 [2, None, None], [8, None, None], [
                     13, None, None], [18, None, None],
               [24, None, None], [28, None, None], [36, 37, 38], [45, 46, 47],
               None, None, None, None, None, None, None, None,
               None, None, None, None,
               [35, None, None], [39, None, None], [44, None, None],
               [49, None, None]],
              True, "velky_strom"),
             ([[19, 21, 22], [10, 11, 12], [30, 32, 34],
               [4, 5, 6], [15, 16, 17], [25, 26, 27], [40, 41, 42],
                 [2, None, None], [8, None, None], [
                     13, None, None], [18, None, None],
               [24, None, None], [28, None, None], [36, 37, 38], [45, 46, 47],
               None, None, None, None, None, None, None, None,
               None, None, None, None,
               [35, None, None], [39, None, None], [49, None, None],
               [44, None, None]],
              False, "porusena_vyhledavaci_vlastnost"),
             ([[19, 21, 22], [10, 11, 12], [30, 32, 34],
               [4, 5, 6], [15, 16, 17], [25, 26, 27], [40, 41, 42],
                 [2, None, None], [8, None, None], [
                     13, None, None], [18, None, None],
               [24, None, None], [28, None, None], [36, 37, 40], [45, 46, 47],
               None, None, None, None, None, None, None, None,
               None, None, None, None,
               [35, None, None], [39, None, None], [44, None, None],
               [49, None, None]],
              False, "porusena_vyhledavaci_vlastnost"),
             ([[19, 21, 22], [10, 11, 12], [30, 32, 34],
               [4, 5, 6], [15, 16, 17], [25, 26, 27], [40, 41, 42],
                 [2, None, None], [8, None, None], [
                     13, None, None], [18, None, None],
               [24, None, None], [28, None, None], [
               36, 37, None], [45, 46, 47],
               None, None, None, None, None, None, None, None,
               None, None, None, None,
               [35, None, None], [39, None, None], [44, None, None],
               [49, None, None]],
              False, "spatny_pocet_klicu_v_uzlu")
             # ([strom], isvalid, name),
             ]

    for treeRepr, isValid, name in tests:
        tree = makeTree(treeRepr)
        answer = isValidMDTree(tree)
        if answer != isValid:
            fname = "isValid_" + name
            drawMDTree(tree, "isValid_" + name)
            return (False,
                    "Vase odpoved: " + str(answer),
                    "Ocekavana odpoved: " + str(isValid),
                    fname + ".dot")

    return (True,)


def testInsert():
    a = [[10, 12, 14], [6, None, None], [20, None, None]]
    a1 = [[10, 12, 14], [6, None, None], [20, 22, None]]
    a2 = [[10, 12, 14], [4, 6, None], [20, None, None]]
    a3 = [[10, 11, 12], [6, None, None], [14, 20, None]]
    b = [[10, 12, 14], [6, None, None], [20, 22, 23]]
    b1 = [[10, 12, 14], [6, None, None],
          [20, 22, 23], None, None, None, [25, None, None]]
    b2 = [[10, 12, 14], [6, None, None],
          [20, 21, 22], None, None, None, [23, None, None]]
    b3 = [[10, 12, 14], [6, None, None],
          [20, 22, 23], None, None, [18, None, None], None]
    big = [[19, 21, 22], [10, 11, 12], [30, 32, 34],
           [4, 5, 6], [15, 16, 17], [25, 26, 27], [40, 41, 42],
           [2, None, None], [8, None, None], [
               13, None, None], [18, None, None],
           [24, None, None], [28, None, None], [36, 37, 38], [45, 46, 47],
           None, None, None, None, None, None, None, None,
           None, None, None, None,
           [35, None, None], [39, None, None], [44, None, None],
           [49, None, None]]
    big1 = [[19, 21, 22], [10, 11, 12], [30, 32, 34],
            [4, 5, 6], [15, 16, 17], [25, 26, 27], [40, 41, 42],
            [2, None, None], [8, None, None], [
                13, None, None], [18, None, None],
            [23, 24, None], [28, None, None], [36, 37, 38], [45, 46, 47],
            None, None, None, None, None, None, None, None,
            None, None, None, None,
            [35, None, None], [39, None, None], [44, None, None],
            [49, None, None]]
    big2 = [[19, 20, 21], [10, 11, 12], [22, 30, 32],
            [4, 5, 6], [15, 16, 17], [25, 26, 27], [34, 40, 41],
            [2, None, None], [8, None, None], [
                13, None, None], [18, None, None],
            [24, None, None], [28, None, None], [36, 37, 38], [42, 45, 46],
            None, None, None, None, None, None, None, None,
            None, None, None, None,
            [35, None, None], [39, None, None], [44, None, None],
            [47, 49, None]]
    empty = [None]
    empty1 = [[5, None, None]]
    tests = [(a, a1, 22, "volny_list"),
             (a, a2, 4, "volny_list_posunuti_poradi"),
             (a, a3, 11, "koren"),
             (b, b1, 25, "novy_list"),
             (b, b2, 21, "plny_list"),
             (b, b3, 18, "novy_list_vlevo"),
             (big, big1, 23, "velky_do_listu"),
             (big, big2, 20, "velky_do_korene"),
             (empty, empty1, 5, "prazdny_strom"),
             # ([strom], [nejakykorektnystrom], key, name)
             ]

    for treeRepr, retTreeRepr, key, name in tests:
        answerTree, compTree = makeTree(treeRepr), makeTree(retTreeRepr)
        insert(answerTree, key)
        answBag, compBag = getAllKeys(answerTree), getAllKeys(compTree)

        if Counter(answBag) != Counter(compBag) or \
           not isValidMDTree(answerTree):
            originalname = "insert_original_" + name
            drawMDTree(makeTree(treeRepr), originalname)
            afterinsertname = "insert_after_insert_" + name
            drawMDTree(answerTree, afterinsertname)
            correctname = "insert_correct_example_" + name
            drawMDTree(compTree, correctname)
            return (False,
                    "Vas strom byl vypsan do souboru " + afterinsertname +
                    ".dot",
                    "Priklad korektniho stromu byl vypsan do souboru " +
                    correctname + ".dot",
                    originalname + ".dot")

    return (True,)


def testFindSuccKey():
    a = [[10, 12, 14], None, [30, 32, 34], None, None, [20, 22, 24], None]
    big = [[19, 21, 22], [10, 11, 12], [30, 32, 34],
           [4, 5, 6], [15, 16, 17], [25, 26, 27], [40, 41, 42],
           [2, None, None], [8, None, None], [
               13, None, None], [18, None, None],
           [24, None, None], [28, None, None], [36, 37, 38], [45, 46, 47],
           None, None, None, None, None, None, None, None,
           None, None, None, None,
           [35, None, None], [39, None, None], [44, None, None],
           [49, None, None]]
    tests = [
        ([None], 9, None, "prazdny_strom"),
        (a, 18, 20, "v_listu"),
        (a, 26, 30, "vnitrni_uzel"),
        (a, 38, None, "nepritomen"),
        (big, 43, 44, "big_v_listu"),
        (big, 49, None, "big_nepritomen"),
        (big, 2, 4, "big_klic_v_listu"),
        (big, 12, 13, "big_klic_v_uzlu"),
        (big, 30, 32, "big_klic_ve_stejnem_uzlu"),
        (big, 33, 34, "big_poradi_v_uzlu"),
        (big, 29, 30, "big_vnitrni_uzel"),
        (big, 18, 19, "big_koren")
        # ([strom], key, succKey, name),
    ]

    for treeRepr, key, succKey, name in tests:
        tree = makeTree(treeRepr)
        answerKey = findSuccKey(tree, key)
        if answerKey != succKey:
            succname = "find_succ_tree_" + name
            drawMDTree(tree, "find_succ_tree_" + name)
            return (False,
                    "Nalezeny klic: " + str(answerKey),
                    "Ocekavany klic: " + str(succKey),
                    succname + ".dot")

    return (True,)


def main():
    testList = [
        (testGetInterestingKeys, "Test vypisu zajimavych klicu:"),
        (testIsValidMDTree, "Test kontroly validity stromu:"),
        (testInsert,
         "Test vkladani klice (pro spravnou funkcionalitu potrebuje korektni "
         "implementaci isValidMDTree):"),
        (testFindSuccKey, "Test hledani naslednika:")
    ]

    for test, name in testList:
        print(name)
        result = test()
        if result[0]:
            print("OK")
        else:
            print(result[1])
            print(result[2])
            print("NOK, testovy strom byl vypsan do souboru " + result[3])
        print()


if __name__ == '__main__':
    main()
