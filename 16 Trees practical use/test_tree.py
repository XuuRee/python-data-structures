#!/usr/bin/python
from __future__ import print_function

# Zadani ukolu:
#
# Mejme neorientovany graf reprezentovany pomoci seznamu nasledniku (viz
# strukturu LLGraph nize).
#
# 1. cast (10 bodu): implementujte funkce listFind, isEdge, isCorrect
# 2. cast (15 bodu): implementujte funkce insert a delete
# 3. cast (10 bodu): implementujte funkci generateTransitionMatrix
# 4. cast (15 bodu): implementujte funkci detectCycle
#
# Presny popis chovani uvedenych funkci je nize u jejich hlavicek.
#
# Doporucujeme vam pouzivat pomocne funkce, ktere mate k dispozici.
# Pro praci se seznamy to jsou funkce listFree, listInsert, listDelete,
# listIsEmpty a listPrint; pro praci s grafy je to funkce graphIsValidVertex.
#
# Testy se v pripade chyby odkazuji na grafy ocislovane od 0. Obrazky techto
# grafu najdete v souboru 03_testovaci_grafy.pdf ve slozce se zadanim.
# Cervenou barvou jsou v nekorektnich grafech zvyrazneny duvody nekorektnosti
# (jednosmerne hrany, neplatne vrcholy).
#
# Testy insert a delete generuji soubory ve formatu GraphViz (jen pri prvnim
# neuspesnem testu daneho typu). Vygenerovane soubory muzete zobrazit pomoci
# online nastroju:
# - http://sandbox.kidstrythisathome.com/erdos/
# - http://www.webgraphviz.com/
# nebo muzete pouzit prekladac z jazyka dot na svem pocitaci.
# Vygenerovane grafy nemaji cervene zvyrazneni a kresli vsechny hrany vzdy
# jako orientovane.
#
# Pro zjedoduseni se omezime na grafy maximalni velikosti MAX_GRAPH_SIZE.
MAX_GRAPH_SIZE = 100


# --- deklarace struktur ---

# Prvek oboustranne zretezeneho seznamu, nese hodnotu typu int.
class Node:
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None


# Oboustranne zretezeny seznam
class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None


# Graf je reprezentovan seznamy nasledniku. Vrcholy grafu jsou vzdy prirozena
# cisla 0, 1, ..., size - 1. Muzete predpokladat, ze graf nikdy nebude mit
# vice nez MAX_GRAPH_SIZE vrcholu.
class LLGraph:
    def __init__(self):
        self.neighbours = [LinkedList() for i in range(MAX_GRAPH_SIZE)]
        self.size = 0


# --- operace se seznamy ---

# Vyprazdneni seznamu
def listFree(linkedList):
    linkedList.first = None
    linkedList.last = None


# Vlozeni hodnoty na konec seznamu
def listInsert(linkedList, value):
    node = Node()
    node.value = value
    node.prev = linkedList.last
    if linkedList.first is None:
        linkedList.first = node
    else:
        linkedList.last.next = node
    linkedList.last = node


# Odstraneni zadaneho prvku ze seznamu
def listDelete(linkedList, node):
    if node.prev is None:
        linkedList.first = node.next
    else:
        node.prev.next = node.next

    if node.next is None:
        linkedList.last = node.prev
    else:
        node.next.prev = node.prev


# Test na prazdnost seznamu
def listIsEmpty(linkedList):
    return linkedList.first is None


# Vypsani seznamu (pro kontrolni vypisy)
def listPrint(linkedList):
    node = linkedList.first
    while node is not None:
        print(node.value, end=' ')
        node = node.next


# --- operace s grafy ---

# Test, zda je zadany vrchol validni
def graphIsValidVertex(graph, vertex):
    if vertex is None:
        return False
    return vertex >= 0 and vertex < graph.size


# --- 1. cast ---

# Zjisti, zda zadany zretezeny seznam obsahuje prvek se zadanou hodnotou.
# Pokud ano, vrati ukazatel na prvni takovy prvek.
# Pokud ne, vrati None.
def listFind(linkedList, value):
    pass  # TODO implementovat


# Zjisti, jestli mezi zadanymi vrcholy existuje hrana. Muzete predpokladat, ze
# graf je korektni a ze zadane vrcholy jsou validni.
# Vraci True, pokud hrana existuje, jinak vraci False.
def isEdge(graph, u, v):
    pass  # TODO implementovat


# Zjisti, jestli je graf korektni, tj. jestli jsou ve vsech seznamech
# nasledniku jen validni vrcholy a jestli je graf neorientovany (tj. hrany jdou
# vzdy obema smery).
# Vraci True, pokud je graf korektni, jinak vraci False.
def isCorrect(graph):
    pass  # TODO implementovat


# --- 2. cast ---

# Vlozi do grafu novy vrchol a prida hrany z tohoto vrcholu do vsech vrcholu
# uvedenych v connectTo. Muzete predpokladat, ze graf je korektni a ze
# connectTo je seznam hodnot vrcholu, ktere jsou validnimi vrcholy grafu.
def insert(graph, connectTo):
    pass  # TODO implementovat


# Vymaze vsechny hrany zadaneho vrcholu. Muzete predpokladat, ze graf je
# korektni a ze zadany vrchol je validni.
def delete(graph, vertex):
    pass  # TODO implementovat


# --- 3. cast ---

# Pro zadany graf vytvori matici sousednosti. Matici sousednosti vytvorte
# rovnou zapisem do argumentu matrix, tedy napr. matrix[1][2] = True. Muzete
# predpokladat, ze graf je korektni. Muzete dale predpokladat, ze matice je
# dostatecne velkych rozmeru. Nemuzete nic predpokladat o obsahu matice.
# Vysledna matice by mela obsahovat hodnoty True/False.
def generateTransitionMatrix(graph, matrix):
    pass  # TODO implementovat


# --- 4. cast ---

# Pro zadany graf rozhodnete, zda obsahuje cyklus.
# Implementace NESMI vyuzivat k vypoctu matici sousednosti.
# Funkce detectCycle vrati True/False podle toho,
# zda zadany graf obsahuje cyklus.
# Muzete predpokladat, ze graf na vstupu je korektni.
def detectCycle(graph):
    pass  # TODO implementovat


# Hlavni funkce volana automaticky po spusteni programu.
# Pokud chcete krome dodanych testu spustit vlastni testovaci kod, dopiste ho
# sem. Odevzdavejte reseni s puvodni verzi teto funkce.
def main():
    if testPart1():
        testPart2()
    else:
        print("Upozorneni: Testy insert a delete je mozno provest pouze"
              "s funkcni implementaci listFind, isCorrect a isEdge.")
        print("--- Testy ukolu 2: NEPROVEDENY ---")
    testPart3()
    testPart4()


# ###################################################################### #
# ##             Nasleduje kod testu, NEMODIFIKUJTE JEJ               ## #
# ###################################################################### #

class TestGraph:
    def __init__(self, graphSize=0):
        self.graph = LLGraph()
        self.graph.size = graphSize
        self.cycle = False
        self.matrix = [[False for i in range(MAX_GRAPH_SIZE)]
                       for j in range(MAX_GRAPH_SIZE)]


def addEdgeToTestGraph(testGraph, fromVertex, toVertex):
    listInsert(testGraph.graph.neighbours[fromVertex], toVertex)
    if 0 <= toVertex < MAX_GRAPH_SIZE:
        testGraph.matrix[fromVertex][toVertex] = True


# --- testovaci grafy ---
def getTestGraph(caseNumber):
    testGraph = None
    # prazdny graf
    if caseNumber == 0:
        testGraph = TestGraph(0)
    # jeden vrchol
    elif caseNumber == 1:
        testGraph = TestGraph(1)
    # zadna hrana
    elif caseNumber == 2:
        testGraph = TestGraph(2)
    # jedna hrana
    elif caseNumber == 3:
        testGraph = TestGraph(2)
        addEdgeToTestGraph(testGraph, 0, 1)
        addEdgeToTestGraph(testGraph, 1, 0)
    # jednoduchy cyklus
    elif caseNumber == 4:
        testGraph = TestGraph(3)
        testGraph.cycle = True
        addEdgeToTestGraph(testGraph, 0, 1)
        addEdgeToTestGraph(testGraph, 0, 2)
        addEdgeToTestGraph(testGraph, 1, 0)
        addEdgeToTestGraph(testGraph, 1, 2)
        addEdgeToTestGraph(testGraph, 2, 1)
        addEdgeToTestGraph(testGraph, 2, 0)
    # bez cyklu
    elif caseNumber == 5:
        testGraph = TestGraph(3)
        addEdgeToTestGraph(testGraph, 0, 1)
        addEdgeToTestGraph(testGraph, 1, 0)
        addEdgeToTestGraph(testGraph, 1, 2)
        addEdgeToTestGraph(testGraph, 2, 1)
    # nesouvisly s cyklem
    elif caseNumber == 6:
        testGraph = TestGraph(8)
        testGraph.cycle = True
        addEdgeToTestGraph(testGraph, 0, 1)
        addEdgeToTestGraph(testGraph, 1, 0)
        addEdgeToTestGraph(testGraph, 1, 2)
        addEdgeToTestGraph(testGraph, 2, 1)
        addEdgeToTestGraph(testGraph, 2, 3)
        addEdgeToTestGraph(testGraph, 3, 2)
        addEdgeToTestGraph(testGraph, 4, 5)
        addEdgeToTestGraph(testGraph, 4, 6)
        addEdgeToTestGraph(testGraph, 5, 4)
        addEdgeToTestGraph(testGraph, 5, 6)
        addEdgeToTestGraph(testGraph, 6, 5)
        addEdgeToTestGraph(testGraph, 6, 4)
    # nesouvisly bez cyklu
    elif caseNumber == 7:
        testGraph = TestGraph(9)
        addEdgeToTestGraph(testGraph, 0, 1)
        addEdgeToTestGraph(testGraph, 1, 0)
        addEdgeToTestGraph(testGraph, 1, 2)
        addEdgeToTestGraph(testGraph, 2, 1)
        addEdgeToTestGraph(testGraph, 2, 3)
        addEdgeToTestGraph(testGraph, 3, 2)
        addEdgeToTestGraph(testGraph, 4, 5)
        addEdgeToTestGraph(testGraph, 5, 4)
        addEdgeToTestGraph(testGraph, 5, 6)
        addEdgeToTestGraph(testGraph, 5, 7)
        addEdgeToTestGraph(testGraph, 6, 5)
        addEdgeToTestGraph(testGraph, 7, 5)
    # KS
    elif caseNumber == 8:
        testGraph = TestGraph(5)
        testGraph.cycle = True
        addEdgeToTestGraph(testGraph, 0, 1)
        addEdgeToTestGraph(testGraph, 0, 2)
        addEdgeToTestGraph(testGraph, 0, 3)
        addEdgeToTestGraph(testGraph, 0, 4)
        addEdgeToTestGraph(testGraph, 1, 0)
        addEdgeToTestGraph(testGraph, 1, 2)
        addEdgeToTestGraph(testGraph, 1, 3)
        addEdgeToTestGraph(testGraph, 1, 4)
        addEdgeToTestGraph(testGraph, 2, 0)
        addEdgeToTestGraph(testGraph, 2, 1)
        addEdgeToTestGraph(testGraph, 2, 3)
        addEdgeToTestGraph(testGraph, 2, 4)
        addEdgeToTestGraph(testGraph, 3, 0)
        addEdgeToTestGraph(testGraph, 3, 1)
        addEdgeToTestGraph(testGraph, 3, 2)
        addEdgeToTestGraph(testGraph, 3, 4)
        addEdgeToTestGraph(testGraph, 4, 0)
        addEdgeToTestGraph(testGraph, 4, 1)
        addEdgeToTestGraph(testGraph, 4, 2)
        addEdgeToTestGraph(testGraph, 4, 3)
    # K3,3
    elif caseNumber == 9:
        testGraph = TestGraph(6)
        testGraph.cycle = True
        addEdgeToTestGraph(testGraph, 0, 3)
        addEdgeToTestGraph(testGraph, 0, 4)
        addEdgeToTestGraph(testGraph, 0, 5)
        addEdgeToTestGraph(testGraph, 1, 3)
        addEdgeToTestGraph(testGraph, 1, 4)
        addEdgeToTestGraph(testGraph, 1, 5)
        addEdgeToTestGraph(testGraph, 2, 3)
        addEdgeToTestGraph(testGraph, 2, 4)
        addEdgeToTestGraph(testGraph, 2, 5)
        addEdgeToTestGraph(testGraph, 3, 0)
        addEdgeToTestGraph(testGraph, 3, 1)
        addEdgeToTestGraph(testGraph, 3, 2)
        addEdgeToTestGraph(testGraph, 4, 0)
        addEdgeToTestGraph(testGraph, 4, 1)
        addEdgeToTestGraph(testGraph, 4, 2)
        addEdgeToTestGraph(testGraph, 5, 0)
        addEdgeToTestGraph(testGraph, 5, 1)
        addEdgeToTestGraph(testGraph, 5, 2)
    # jedna orientovana hrana (nekorektni)
    elif caseNumber == 10:
        testGraph = TestGraph(2)
        addEdgeToTestGraph(testGraph, 0, 1)
    # nekorektni
    elif caseNumber == 11:
        testGraph = TestGraph(1)
        addEdgeToTestGraph(testGraph, 0, 1)
    # nekorektni
    elif caseNumber == 12:
        testGraph = TestGraph(2)
        addEdgeToTestGraph(testGraph, 0, 1)
        addEdgeToTestGraph(testGraph, 1, 0)
        addEdgeToTestGraph(testGraph, 1, -101)
    # nekorektni
    elif caseNumber == 13:
        testGraph = TestGraph(5)
        addEdgeToTestGraph(testGraph, 2, 356)
        addEdgeToTestGraph(testGraph, 2, 17)
        addEdgeToTestGraph(testGraph, 2, 42)
    # nekorektni (jedna hrana chybi)
    elif caseNumber == 14:
        testGraph = TestGraph(5)
        addEdgeToTestGraph(testGraph, 0, 1)
        addEdgeToTestGraph(testGraph, 1, 0)
        addEdgeToTestGraph(testGraph, 1, 2)
        addEdgeToTestGraph(testGraph, 2, 1)
        addEdgeToTestGraph(testGraph, 2, 3)
        addEdgeToTestGraph(testGraph, 3, 2)
        addEdgeToTestGraph(testGraph, 4, 1)
    # nekorektni (K3,3 s jednou jednosmernou hranou)
    elif caseNumber == 15:
        testGraph = TestGraph(6)
        addEdgeToTestGraph(testGraph, 0, 3)
        addEdgeToTestGraph(testGraph, 0, 4)
        addEdgeToTestGraph(testGraph, 0, 5)
        addEdgeToTestGraph(testGraph, 1, 3)
        addEdgeToTestGraph(testGraph, 1, 4)
        addEdgeToTestGraph(testGraph, 1, 5)
        addEdgeToTestGraph(testGraph, 2, 3)
        addEdgeToTestGraph(testGraph, 2, 4)
        addEdgeToTestGraph(testGraph, 2, 5)
        addEdgeToTestGraph(testGraph, 3, 0)
        addEdgeToTestGraph(testGraph, 3, 1)
        addEdgeToTestGraph(testGraph, 3, 2)
        addEdgeToTestGraph(testGraph, 4, 0)
        addEdgeToTestGraph(testGraph, 4, 2)
        addEdgeToTestGraph(testGraph, 5, 0)
        addEdgeToTestGraph(testGraph, 5, 1)
        addEdgeToTestGraph(testGraph, 5, 2)
    # nekorektni se 100 vrcholy
    elif caseNumber == 16:
        testGraph = TestGraph(100)
        addEdgeToTestGraph(testGraph, 99, 100)
    return testGraph

TEST_CASES = 17
CORRECT_CASES = 10

# --- testy casti 1 ---


def reportList(sayNOK, array):
    if sayNOK:
        print("NOK")
    print("\tseznam %s: " % array, end='')


def testListFind():
    result = True
    arrays = [
        [],
        [127],
        [1, 2, 3, 4, 5],
        [7, 42, 17, 9, 20],
        [5, 0, 8, 256]
    ]
    others = [6, 10, 11, 12, 16, 300, 1000, -1]
    print("Test listFind: ", end='')
    for array in arrays:
        ok = True
        linkedList = LinkedList()
        for value in array:
            listInsert(linkedList, value)
        for value in array:
            if not ok:
                break
            node = listFind(linkedList, value)
            if node is None:
                reportList(result, array)
                print("%d nenalezeno" % value)
                ok = False
            elif node.value != value:
                reportList(result, array)
                print("misto %d nalezen prvek s hodnotou %s" %
                      (value, str(node.value)))
                ok = False
        for other in others:
            if not ok:
                break
            node = listFind(linkedList, other)
            if node is not None:
                reportList(result, array)
                print("hledani %d naslo prvek s hodnotou %s" %
                      (other, str(node.value)))
                ok = False
        result = result and ok
    if result:
        print("OK")
    return result


def testAgainstMatrix(testGraph):
    for i in range(testGraph.graph.size):
        for j in range(testGraph.graph.size):
            if isEdge(testGraph.graph, i, j) != testGraph.matrix[i][j]:
                return False, i, j
    return True, -1, -1


def reportGraph(sayNOK, graphNo):
    if sayNOK:
        print("NOK")
    print("\tgraf cislo %d" % graphNo, end='')


def testIsEdge():
    result = True
    print("Test isEdge: ", end='')
    for i in range(CORRECT_CASES):
        testGraph = getTestGraph(i)
        ok, u, v = testAgainstMatrix(testGraph)
        if not ok:
            reportGraph(result, i)
            print(": spatna odpoved pro hranu %d -- %d " % (u, v))
        result = result and ok
    if result:
        print("OK")
    return result


def testIsCorrect():
    result = True
    print("Test isCorrect: ", end='')
    for i in range(TEST_CASES):
        testGraph = getTestGraph(i)
        correct = (i < CORRECT_CASES)
        answer = isCorrect(testGraph.graph)
        if answer != correct:
            reportGraph(result, i)
            print(", spatna odpoved: %s, melo byt %s" % (answer, correct))
        result = result and (answer == correct)
    if result:
        print("OK")
    return result


def testPart1():
    b = testListFind()
    b = testIsEdge() and b
    b = testIsCorrect() and b
    print("--- Testy casti 1: %s ---" % ("uspesne" if b else "NEUSPESNE"))
    return b


# --- testy casti 2 ---

def drawDot(testGraph, testIns):
    filename = "graf_insert.dot" if testIns else "graf_delete.dot"
    with open(filename, "w") as dot:
        dot.write("digraph {\n")
        for i in range(testGraph.graph.size):
            dot.write("\t\"%d\";\n" % i)
            node = testGraph.graph.neighbours[i].first
            while node is not None:
                dot.write("\t\"%d\" -> \"%d\";\n" % (i, node.value))
                node = node.next
        dot.write("}\n")
    print("\t\tVas graf byl vygenerovan do souboru '%s'." % filename)


def testCorrectness(testGraph, sayNOK, graphNo, msg, testIns):
    if not isCorrect(testGraph.graph):
        reportGraph(sayNOK, graphNo)
        print(", %s: nekorektni graf" % msg)
        if sayNOK:
            drawDot(testGraph, testIns)
        return False
    else:
        ok, u, v = testAgainstMatrix(testGraph)
        if not ok:
            reportGraph(sayNOK, graphNo)
            print(", %s: chybna hrana %d -- %d" % (msg, u, v))
            if sayNOK:
                drawDot(testGraph, testIns)
        return ok


def testInsert():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    neighbours = [0, 2, 3, 6, 1, 7, MAX_GRAPH_SIZE]
    result = True
    print("Test insert: ", end='')
    for i in range(CORRECT_CASES):
        testGraph = getTestGraph(i)
        insert(testGraph.graph, [])
        res = testCorrectness(testGraph, result, i,
                              "vlozeni vrcholu bez sousedu", True)
        result = result and res

        insert(testGraph.graph, numbers[:testGraph.graph.size])
        n = testGraph.graph.size - 1
        for v in range(n):
            testGraph.matrix[n][v] = True
            testGraph.matrix[v][n] = True
        res = testCorrectness(testGraph, result, i,
                              "vlozeni vrcholu se vsemi sousedy", True)
        result = result and res

        nsize = 0
        msg = "vlozeni vrcholu se sousedy"
        while neighbours[nsize] < testGraph.graph.size:
            msg += " %d" % neighbours[nsize]
            nsize += 1

        insert(testGraph.graph, neighbours[:nsize])
        n = testGraph.graph.size - 1
        for v in range(nsize):
            testGraph.matrix[n][neighbours[v]] = True
            testGraph.matrix[neighbours[v]][n] = True
        res = testCorrectness(testGraph, result, i, msg, True)
        result = result and res

    if result:
        print("OK")
    return result


def testOneDelete(testGraph, v, sayNOK, graphNo):
    delete(testGraph.graph, v)
    for u in range(testGraph.graph.size):
        testGraph.matrix[u][v] = False
        testGraph.matrix[v][u] = False
    return testCorrectness(testGraph, sayNOK, graphNo,
                           "smazani vsech hran vrcholu %d" % v, False)


def testDelete():
    vertices = [6, 4, 0, 2, 1, 3, 5]
    result = True
    print("Test delete: ", end='')
    for i in range(CORRECT_CASES):
        testGraph = getTestGraph(i)
        if testGraph.graph.size == 0:
            continue
        for j in vertices:
            if j < testGraph.graph.size:
                res = testOneDelete(testGraph, j, result, i)
                result = result and res
    if result:
        print("OK")
    return result


def testPart2():
    b = testInsert()
    b = testDelete() and b
    print("--- Testy casti 2: %s ---" % ("uspesne" if b else "NEUSPESNE"))


# --- testy casti 3 ---

def compareMatrix(m1, m2, upTo):
    for i in range(upTo):
        for j in range(upTo):
            if m1[i][j] != m2[i][j]:
                return False, i, j
    return True, -1, -1


def testPart3():
    result = True
    matrix = [[False for i in range(MAX_GRAPH_SIZE)]
              for j in range(MAX_GRAPH_SIZE)]
    print("Test generateTransitionMatrix: ", end='')
    for i in range(CORRECT_CASES):
        testGraph = getTestGraph(i)
        if testGraph.graph.size == 0:
            continue
        generateTransitionMatrix(testGraph.graph, matrix)
        ok, u, v = compareMatrix(testGraph.matrix, matrix,
                                 testGraph.graph.size)
        if not ok:
            reportGraph(result, i)
            print(", chyba na indexu [%d][%d]" % (u, v))
        result = result and ok
    if result:
        print("OK")
    print("--- Testy casti 3: %s ---" % ("uspesne" if result else "NEUSPESNE"))


# --- testy casti 4 ---

def testPart4():
    result = True
    print("Test detectCycle: ", end='')
    for i in range(CORRECT_CASES):
        testGraph = getTestGraph(i)
        cycle = detectCycle(testGraph.graph)
        if cycle and not testGraph.cycle:
            reportGraph(result, i)
            print(": nalezen cyklus, ale v grafu zadny neni")
            result = False
        elif not cycle and testGraph.cycle:
            reportGraph(result, i)
            print(": nenalezen cyklus, ale v grafu je")
            result = False
    if result:
        print("OK")
    print("--- Testy casti 4: %s ---" % ("uspesne" if result else "NEUSPESNE"))

if __name__ == '__main__':
    main()
