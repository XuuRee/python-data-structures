from __future__ import print_function #kompatibilita s Python 2.7

import sys

#  Implementacni test IB002 2016 - LTree (max 50 bodu)
#
#  Vasi ulohou je implementovat ctyri funkce pro datovou strukturou "LTree".
#  Muzete si samozrejme pridat vlastni pomocne funkce.
#
#  LTree je datova struktura, ktera slouzi k ukladani klicu typu integer.
#  Pro jednoduchost budeme v teto uloze predpokladat, ze klice jsou unikatni,
#  tj. pokud je ve strukture ulozen nejaky klic, tak zadny jiny klic nema
#  stejnou hodnotu, a to ani v jinem strome (v uloze 4).
#
#  LTree je binarni strom, ktery ma v kazdem uzlu ulozeny klic 'key' a navic
#  pomocnou hodnotu 'S'. LTree musi splnovat nasledujici vlastnosti:
#
#  - Klic uzlu musi byt vzdy mensi nez klice jeho synu.
#
#  - Hodnota 'S' je vzdalenost k nejblizsimu "None nasledniku" ve svem podstrome.
#    - List (oba synove jsou 'None') ma hodnotu 'S' rovnu 1.
#    - Uzel s jednim synem (druhy je tedy 'None') ma hodnotu 'S' rovnu 1.
#
#  - Hodnota 'S' leveho syna musi byt vetsi nebo rovna hodnote 'S' praveho syna.
#    - Uzel s jednim synem ma jen leveho syna.
#
#  Prazdny strom je tedy take LTree.
#
#  Jenoduche priklady (vypsane hodnoty jsou klice):
#      jsou LTree           nejsou LTree
#      1        4               4    2
#     / \      /               /      \
#    2   3    7               2        4
#
#  Pro slozitejsi ukazky se muzete podivat do prilozeneho pdf.
#
#  Vasi prvni ulohou je napsat funkci getLeafsKeys, ktera prida klice
#  ze vsech listu zadaneho stromu do pripraveneho seznamu.
#
#  Druhou ulohou je napsat funkci, ktera spocita a doplni hodnoty S do uzlu
#  zadaneho binarniho stromu.
#
#  Treti ulohou je napsat funkci, ktera zkontroluje zda je dany strom
#  korektni LTree.
#
#  Posledni, ctvrtou ulohou je napsat funkci merge podle algoritmu
#  popsanem nize.
#
#  Jednotlive funkce jsou bodovany nasledovne:
#
#  1. uloha (10 bodu): getLeafsKeys
#  2. uloha (10 bodu): computeS
#  3. uloha (10 bodu): isCorrectLTree
#  4. uloha (20 bodu): merge



#  Struktura pro reprezentaci uzlu stromu LTree.
#  'key' je klic uzlu
#  'S' je hodnota S daneho uzlu.
#
#  'left' je levy syn, tedy atribut typu Node, pokud syn existuje, jinak None
#  'right' analogicky jako left
class Node:
    def __init__(self):
        self.key = None
        self.S = None
        self.left = None
        self.right = None


#  Trida pro reprezentaci LTree
#  'root' je koren stromu a je typu Node, nebo None, pokud je strom prazdny.
class LTree:
    def __init__(self):
        self.root = None

#  Ulozi klice listu zadaneho stromu do pripraveneho seznamu 'list'.
#  Poradi klicu v 'list' neni dulezite.
#
#  :param 'tree' strom, typu LTree, klice jehoz listu se maji ulozit do seznamu
#  :param 'list' seznam, do ktereho se maji pridat klice listu stromu 'tree'
#
#  Pro vkladani do list pouzijte funkci append(key), kde 'key' je pridavany klic.
#  Jinak list nemodifikujte!

def get_leafs_keys_recursion(node, result_list):
    if node is None:
        return
    if node.left is None and node.right is None:
        result_list.append(node.key)        # optimalizace: return
    if node.left is None and node.right is not None:
        result_list.append(node.key)        # optimalizace: return
    get_leafs_keys_recursion(node.left, result_list)
    get_leafs_keys_recursion(node.right, result_list)


def getLeafsKeys(tree, result_list) :
    if tree.root is not None:
        get_leafs_keys_recursion(tree.root, result_list)


#  Spocita a doplni hodnoty S do vsech uzlu stromu tree. Tato funkce by
#  mela pracovat pro libovolny binarni strom, tedy bez ohledu na korektnost LTree.
#
#  :param 'tree' strom, ve kterem se maji spocitat a nasledne do nej vlozit
#  hodnoty S.

def compute_s_recursion(node):
    if node is None:
        return 0
    l = compute_s_recursion(node.left)
    r = compute_s_recursion(node.right)
    result = min(l, r) + 1
    node.S = result
    return result


def computeS(tree):
    compute_s_recursion(tree.root)
    

#  @brief Overi jestli je strom 'tree' korektni LTree
#  :param 'tree' strom, typu LTree, ktery se ma overit
#  :return True pokud tree je korektni LTree, jinak False
#
#  Pro projiti testu je potreba mit funkci computeS.
#  Pred volanim kazdeho testu se vola funkce computeS.


#  - Klic uzlu musi byt vzdy mensi nez klice jeho synu.
#
#  - Hodnota 'S' je vzdalenost k nejblizsimu "None nasledniku" ve svem podstrome.
#    - List (oba synove jsou 'None') ma hodnotu 'S' rovnu 1.
#    - Uzel s jednim synem (druhy je tedy 'None') ma hodnotu 'S' rovnu 1.
#
#  - Hodnota 'S' leveho syna musi byt vetsi nebo rovna hodnote 'S' praveho syna.
#    - Uzel s jednim synem ma jen leveho syna.
#
#  Prazdny strom je tedy take LTree.


def is_correct_lt_tree_recursion(node, parent):
    if node is None:
        return True
    if parent is not None and parent.key >= node.key:
        return False
    if node.left is None and node.right is not None:
        return False
    return is_correct_lt_tree_recursion(node.left, node) and is_correct_lt_tree_recursion(node.right, node)


def is_correct_s_attribute_recursion(node):
    if node is None:
        return True, 0
    bool_one, l = is_correct_s_attribute_recursion(node.left)
    bool_two, r = is_correct_s_attribute_recursion(node.right)
    result = min(l, r) + 1
    if l < r:
        return False, result
    if not bool_one or not bool_two:
        return False, result
    if node.S != result:
        return False, result
    return True, result


def isCorrectLTree(tree):
    if not is_correct_lt_tree_recursion(tree.root, None):
        return False
    bool_result, number = is_correct_s_attribute_recursion(tree.root)
    return bool_result


#  @brief Operace merge spoji stromy 'U' a 'V'.
#
#  :param 'U' strom, typu LTree, ktery se ma spojit s 'V'
#  :param 'V' strom, typu LTree, ktery se ma spojit s 'U'
#  :return koren spojeni 'U' a 'V'
#
#  ################################################
#  Pokud je jeden ze stromu prazdny, funkce vrati koren druheho z nich.
#
#  Oznacme si koren 'U' jako 'u' a koren 'V' jako 'v'.
#  Pro jednoduchost predpokladejme, ze klic korene 'u' je mensi nez
#  klic v koreni 'v', Opacny pripad reste symetricky. Rovnost muzete diky
#  unikatnosti klicu ignorovat, nenastava.
#
#  Pokud 'u' nema praveho syna, tak se 'v' stane pravym synem 'u'.
#  Pokud 'u' ma praveho syna 'w', musime jej nahradit spojenim 'w' a 'v'.
#
#  Jestli po spojeni 'w' a 'v' by mel pravy syn 'u' vetsi S nez jeho levy syn,
#  musime tyto syny prohodit.
#
#  Priklad viz prilozene pdf.
#
#  ################################################
#  Na vstupu jsou dva korektni LTree 'U' a 'V'.
#
#  Vystupem je koren korektniho LTree. Korektni implementace algoritmu popsana vyse
#  vede k jednoznacnemu reseni, tedy resenim je pouze jeden konkretni strom.

def merge(U, V) :
    #TODO
    return None


# ######################################################################
# ##             Nasleduje kod testu, NEMODIFIKUJTE JEJ               ##
# ######################################################################

"""
Dodatek k graphvizu:
Graphviz je nastroj, ktery vam umozni vizualizaci datovych struktur,
coz se hodi predevsim pro ladeni.
Tento program generuje nekolik souboru neco.dot v mainu
Vygenerovane soubory nahrajte do online nastroje pro zobrazeni graphvizu:
http://sandbox.kidstrythisathome.com/erdos/
nebo http://graphviz-dev.appspot.com/  - zvlada i vetsi grafy

Alternativne si muzete nainstalovat prekladac z jazyka dot do obrazku na svuj pocitac.
"""
def makeGraphviz(node, f):
    if (node == None): return
    if (node.S is not None):
        f.write("%i [label = \"%i\\nS=%i\"]\n" % (node.key, node.key, node.S))
    if (node.left is not None):
        f.write("%i -> %i\n" % (node.key, node.left.key))
        makeGraphviz(node.left, f)
    else:
        f.write("L{} [label=\"\",color=white]\n{} -> L{}\n".format(id(node), node.key, id(node)))
    if (node.right is not None):
        f.write("%i -> %i\n" % (node.key, node.right.key))
        makeGraphviz(node.right, f)
    else:
        f.write("R{} [label=\"\",color=white]\n{} -> R{}\n".format(id(node), node.key, id(node)))

def makeGraph(tree, fileName):
    f = open(fileName, 'w')
    f.write("digraph Tree {\n")
    f.write("node [color=lightblue2, style=filled];\n")
    if (tree is not None) and (tree.root is not None):
        makeGraphviz(tree.root, f)
    f.write("}\n")
    f.close()

def makeSubtree(s, node) :
	leftValue = s.pop(0)
	if leftValue is not None :
		left = Node()
		left.key = leftValue
		node.left = left
		makeSubtree(s, left)
	rightValue = s.pop(0)
	if rightValue is not None :
		right = Node()
		right.key = rightValue
		node.right = right
		makeSubtree(s, right)

def makeTree(s) :
	key = s.pop(0)
	if key is None :
		return None
	root = Node()
	root.key = key
	makeSubtree(s, root)
	return root

def printNodeKeys(node, keys) :
	if node is None :
		keys.append(None)
		return
	keys.append(node.key)
	printNodeKeys(node.left, keys)
	printNodeKeys(node.right, keys)

def printTreeKeys(tree) :
    keys = []
    printNodeKeys(tree.root, keys)
    return keys

def printNodeS(node, SVals) :
	if node is None :
		SVals.append(None)
		return
	SVals.append(node.S)
	printNodeS(node.left, SVals)
	printNodeS(node.right, SVals)

def printTreeS(tree) :
    SVals = []
    printNodeS(tree.root, SVals)
    return SVals

def testgetLeafsKeys() :
    TEST_COUNT = 5

    treeCodes = [
        [10, 20, None, None, None],
        [10, None, None],
        [None],
        [2, 4, 9, None, None, 5, None, None, 6, 8, None, None, 7, None, None],
        [2, 4, None, None, 6, None, None]
    ]

    expectedResults = [
        [20],
        [10],
        [],
        [5, 7, 8, 9],
        [4, 6]
    ]

    checkTrees = [
        [10, 20, None, None, None],
        [10, None, None],
        [None],
        [2, 4, 9, None, None, 5, None, None, 6, 8, None, None, 7, None, None],
        [2, 4, None, None, 6, None, None]
    ]

    failure = 0

    print("Test 1. getLeafsKeys: ")
    tree = LTree()

    for i in range(TEST_COUNT):
        tree.root = makeTree(treeCodes[i])
        list = []
        getLeafsKeys(tree, list)
        list.sort()

        if (list != expectedResults[i]) or (printTreeKeys(tree) != checkTrees[i]):
            failure = i + 1
            break

    if failure != 0 :
        print("NOK%d - chyba ve funkci getLeafsKeys"%(failure))
        if (printTreeKeys(tree) != checkTrees[i]) :
            print("Zadany strom se nema menit!")
        print("Ocekavane reseni: ", expectedResults[i])
        print("Vase reseni: ", list)
    else :
        print("OK")

def testComputeS() :
    TEST_COUNT = 3

    treeCodes = [
        [None],
        [1, 3, 4, 5, None, None, 9, None, None, 6, 7, 8, None, None, None, None, 2, None, None],
        [1, 3, 4, 5, None, None, 9, None, None, 6, 7, None, None, 8, None, None, 2, None, None]
    ]

    expectedResults = [
        [None],
        [2, 2, 2, 1, None, None, 1, None, None, 1, 1, 1, None, None, None, None, 1, None, None],
        [2, 3, 2, 1, None, None, 1, None, None, 2, 1, None, None, 1, None, None, 1, None, None]
    ]

    checkTrees = [
        [None],
        [1, 3, 4, 5, None, None, 9, None, None, 6, 7, 8, None, None, None, None, 2, None, None],
        [1, 3, 4, 5, None, None, 9, None, None, 6, 7, None, None, 8, None, None, 2, None, None]
    ]

    failMessages = [
        "OK",
        "NOK1 - prazdny strom",
        "NOK2 - strom s delsi vetvi",
        "NOK3 - husty strom"
    ]

    print("Test 2. computeS: ")
    tree = LTree()

    failure = 0

    for i in range(TEST_COUNT):
        tree.root = makeTree(treeCodes[i])
        computeS(tree)

        if (printTreeS(tree) != expectedResults[i]) or \
                (printTreeKeys(tree) != checkTrees[i]):
            failure = i + 1
            break

    if failure != 0 :
        print(failMessages[failure])
        makeGraph(tree, "computeNOK%dvas.dot"%(failure));
        tree.root = makeTree(checkTrees[failure-1]);
        makeGraph(tree, "computeNOK%dvzor.dot"%(failure));
        print("Byly vygenerovany soubory s prislusnymi stromy\n");
    else :
        print("OK")

def testCorrect() :
    TEST_COUNT = 8

    treeCodes = [
        [1, 3, None, None, 2, 6, None, None, None],
        [1, 3, 4, 5, None, None, 9, None, None, 6, 7, 8, None, None, None, None, 2, None, None],
        [1, 3, None, None, 2, 5, None, None, 6, None, None],
        [2, 3, None, None, 6, 4, None, 1, None, None, None],
        [1, None, 2, None, None],
        [1, None, None],
        [1, None, None],
        [1, 3, 4, None, None, 5, None, None, 2, 6, None, None, None]
    ]

    expectedResults = [True, True, False, False, False, True, False, False]

    checkTrees = [
        [1, 3, None, None, 2, 6, None, None, None],
        [1, 3, 4, 5, None, None, 9, None, None, 6, 7, 8, None, None, None, None, 2, None, None],
        [1, 3, None, None, 2, 5, None, None, 6, None, None],
        [2, 3, None, None, 6, 4, None, 1, None, None, None],
        [1, None, 2, None, None],
        [1, None, None],
        [1, None, None],
        [1, 3, 4, None, None, 5, None, None, 2, 6, None, None, None]
    ]

    failMessages = [
        "OK",
        "NOK1 - korektni strom - maly strom",
        "NOK2 - korektni strom - vetsi strom",
        "NOK3 - nekorektni strom - hodnota S praveho syna vetsi nez leveho",
        "NOK4 - nekorektni strom - pomomci maji mensi hodnotu key",
        "NOK5 - nekorektni strom - ma praveho syna, ale nema leveho - hodnota S",
        "NOK6 - korektni strom - jen koren",
        "NOK7 - nekorektni strom - strom se spatne spocitanymi hodnotami S",
        "NOK8 - nekorektni strom - strom se spatne spocitanymi hodnotami S"
    ]

    print("Test 3. isCorrectLTree: ")
    tree = LTree()

    failure = 0

    for i in range(TEST_COUNT):
        tree.root = makeTree(treeCodes[i])
        computeS(tree)

        if (i+1 == 7) : tree.root.S = 3
        if (i+1 == 8) :
            tree.root.S = 3
            tree.root.right.S = 2

        if (isCorrectLTree(tree) != expectedResults[i]) or \
                (printTreeKeys(tree) != checkTrees[i]) :
            failure = i + 1
            break

    if failure != 0 :
        print(failMessages[failure])
        makeGraph(tree, "correctNOK%dvas.dot"%(failure));
        tree.root = makeTree(checkTrees[failure-1]);
        makeGraph(tree, "correctNOK%dvzor.dot"%(failure));
        print("Byly vygenerovany soubory s prislusnymi stromy\n");
    else :
        print("OK")

def testMerge() :
    TEST_COUNT = 8

    tree1Codes = [
        [None],
        [None],
        [2, None, None],
        [2, None, None],
        [4, 7, None, None, None],
        [1, 2, None, None, 3, None, None],
        [1, 2, 8, None, None, 9, None, None, 4, 6, None, None, 7, None, None],
        [1, 2, 8, None, None, 9, None, None, 4, 12, None, None, None]
    ]

    tree2Codes = [
        [None],
        [2, None, None],
        [None],
        [3, None, None],
        [3, None, None],
        [4, 5, None, None, 6, None, None],
        [3, None, None],
        [3, 5, 10, None, None, 11, None, None, 6, 7, None, None, None]
    ]

    expectedTrees = [
        [None],
        [2, None, None],
        [2, None, None],
        [2, 3, None, None, None],
        [3, 4, 7, None, None, None, None],
        [1, 2, None, None, 3, 4, 5, None, None, 6, None, None, None],
        [1, 2, 8, None, None, 9, None, None, 3, 4, 6, None, None, 7, None, None, None],
        [1, 3, 5, 10, None, None, 11, None, None, 4, 12, None, None, 6, 7, None, None, None, 2, 8, None, None, 9, None, None]
    ]

    expectedSTrees = [
        [None],
        [1, None, None],
        [1, None, None],
        [1, 1, None, None, None],
        [1, 1, 1, None, None, None, None],
        [2, 1, None, None, 1, 2, 1, None, None, 1, None, None, None],
        [2, 2, 1, None, None, 1, None, None, 1, 2, 1, None, None, 1, None, None, None],
        [3, 3, 2, 1, None, None, 1, None, None, 2, 1, None, None, 1, 1, None, None, None, 2, 1, None, None, 1, None, None]
    ]

    failMessages = [
        "OK",
        "NOK1 - oba stromy U i V prazdne",
        "NOK2 - strom U je prazdny",
        "NOK3 - strom V je prazdny",
        "NOK4 - oba stromy obsahuji jen jeden uzel u < v",
        "NOK5 - u nema praveho syna, v je nejmensi a nema syny",
        "NOK6 - male stromy U a V",
        "NOK7 - u^ ma syna a V ma jeden uzel",
        "NOK8 - vetsi stromy"
    ]

    print("Test 4. merge: ")
    tree1 = LTree()
    tree2 = LTree()
    res = LTree()

    failure = 0

    for i in range(TEST_COUNT):
        tree1.root = makeTree(tree1Codes[i])
        tree2.root = makeTree(tree2Codes[i])
        computeS(tree1)
        computeS(tree2)

        res.root = merge(tree1, tree2)

        if ((printTreeKeys(res)) != expectedTrees[i]) or \
                (printTreeS(res) != expectedSTrees[i]) :
            failure = i + 1
            break

    if failure != 0 :
        print(failMessages[failure])
        makeGraph(res, "mergeNOK%dvas.dot"%(failure));
        tree = LTree()
        tree.root = makeTree(expectedTrees[failure-1]);
        makeGraph(tree, "mergeNOK%dvzor.dot"%(failure));
        print("Byly vygenerovany soubory s prislusnymi stromy\n");
    else :
        print("OK")

def main() :
    testgetLeafsKeys()
    testComputeS()
    testCorrect()
    testMerge()

if __name__ == '__main__':
    main()