#!/usr/bin/python3


import heapq as pq  # prioritni fronta


###########################
# Dotaz studenta:
#
#
###########################

# Chcete-li dostat odpoved, vlozte do nazvu souboru heslo KONTROLA.

# V teto uloze mate naimplementovat probirane algoritmy na nalezeni
# nejkratsich cest v grafu, tedy Dijkstruv a Belmannuv-Forduv algoritmus.
#
# Krome testu je pro vas i pripraven vypis v jazyce dot, staci z vaseho
# kodu zavolat funkci makeGraph(graph, fileName), ktere predate graf
# a jmeno souboru, do ktereho chcete graf vypsat.


# jako vzdalenost nedosazitelneho vrcholu
infinity = 2 ** 31

# jako vzdalenost v pripade nalezeni negativniho cyklu,
# tedy nedefinovana vzdalenost
negative_infinity = - (2 ** 31)


class DiGraph:
    """Trida DiGraph slouzi k reprezentaci orientovaneho grafu.

    Atributy:
        matrix          matice, ktera obsahuje hrany grafu
        distances       pole vzdalenosti ze zadaneho vrcholu
        predecessors    pole predchudcu, podle ktereho lze zpetne urcit,
                        kudy vedla cesta
        size            pocet vrcholu grafu
    """
    def __init__(self):
        self.matrix = [[]]
        self.distances = []
        self.predecessors = []
        self.size = 0


def initialize(graph, s):
    """Funkce slouzi k inicializaci grafu. Nastavi vzdalenost
    inicialniho vrcholu 's' na 0 a zbytek na nekonecno. Predchudce
    inicialniho vrcholu je None.
    """
    pass
    # TODO
    n = (graph.size)
    graph.distances = n * [infinity]
    graph.distances[s] = 0
    graph.predecessors = n * [None]



def relax(graph, u, v):
    """Funkce slouzi k relaxaci hrany ('u', 'v') v orientovanem
    grafu 'graph'.
    """
    pass
    # TODO
    graph.distances[v] = graph.distances[u] + graph.matrix[u][v]
    graph.predecessors[v] = u


def bellman_ford(graph, ux, vx):
    """Bellman-Forduv algoritmus pro nalezeni stromu nejkratsich cest
    z vrcholu 'u' v grafu 'graph'. Funkce vraci delku cesty z 'u' do 'v'.
    V poli 'graph.distances' budou po vypoctu vzdalenosti vrcholu od 'u'
    a v poli 'graph.predecessors' budou prechudci vrcholu na ceste z 'u'.
    """
    # TODO
    initialize(graph,ux)
    for i in range(len(graph.matrix)-1):
        for u in range(len(graph.matrix)):
            for v in range(len(graph.matrix)):
                if graph.matrix[u][v] is not None:
                    if graph.distances[v] > graph.distances[u] + graph.matrix[u][v]:
                        relax(graph,u,v)
    for u in range(len(graph.matrix)):
        for v in range(len(graph.matrix)):
            if graph.matrix[u][v] is not None:
                if graph.distances[v] > graph.distances[u] + graph.matrix[u][v]:
                    return False
    return graph.distances[vx]


def dijkstra(graph, ux, vx):
    """Dijkstruv algoritmus pro nalezeni nejkratsi cesty z vrcholu 'u'
    do vrcholu 'v' v grafu 'graph'. Dunkce vraci delku cesty z 'u' do
    'v'. Jako prioritni frontu pouzijte funkce z knihovny:
    https://docs.python.org/3/library/heapq.html
    """
    # TODO
    initialize(graph,ux)
    s = set()
    q = [ux]
    while q:
        u = pq.heappop(q)
        s.add(u)
        for i in range(len(graph.matrix)):
            for j in range(len(graph.matrix)):
                if graph.matrix[i][j] is not None :
                    if graph.distances[j] > graph.distances[i] + graph.matrix[i][j]:
                        relax(graph,i,j)
    return graph.distances[vx]


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
def makeGraph(graph, fileName):
    f = open(fileName, 'w')
    f.write("digraph MyGraph {\n")
    makeGraphviz(graph.matrix, f)
    f.write("}\n")
    f.close()


def makeGraphviz(matrix, f):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] is not None:
                m = matrix[i][j]
                f.write("\"%i\" -> \"%i\" [ label = %i ]\n" % (i, j, m))


def add_edge(graph, u, v, w):
    """Prida hranu ('u', 'v') vahy 'w' do matice vzdalenosti 'matrix'.
    Funkce nic nedela v pripade, ze 'u' nebo 'v' je mimo rozsah matice.
    """
    if u >= 0 and v >= 0 and u < graph.size and v < graph.size:
        graph.matrix[u][v] = w


def is_edge(graph, u, v):
    """Pokud v matici vzdalenosti 'matrix' existuje hrana (u, v),
    vraci True, jinak False.
    """
    return graph.matrix[u][v] is not None


def print_matrix(graph):
    for i in range(graph.size):
        for j in range(graph.size):
            print("{0:4} ".format(graph.matrix[i][j]), end="")
        print("")


def create_graph(n):
    """Vytvori n.n matici vzdalenosti."""
    g = DiGraph()
    g.matrix = [[None]*n for i in range(n)]
    for i in range(n):
        g.matrix[i][i] = 0
    g.size = n
    return g


def create_test_graph():
    graph = create_graph(6)
    graph.matrix[0][1] = 7
    graph.matrix[0][2] = 9
    graph.matrix[0][5] = 14
    graph.matrix[1][3] = 15
    graph.matrix[1][2] = 10
    graph.matrix[2][3] = 11
    graph.matrix[2][5] = 2
    graph.matrix[3][4] = 6
    graph.matrix[4][5] = 9
    graph.matrix[1][0] = 7
    graph.matrix[2][0] = 9
    graph.matrix[5][0] = 14
    graph.matrix[3][1] = 15
    graph.matrix[2][1] = 10
    graph.matrix[3][2] = 11
    graph.matrix[5][2] = 2
    graph.matrix[4][3] = 6
    graph.matrix[5][4] = 9
    return graph


def test_initialize():
    print("Test 1. initialize pro Bellman-Forduv algoritmus: ")

    graph1 = create_graph(1)
    initialize(graph1, 0)
    if (graph1.distances == [] or
            graph1.distances[0] != 0 or
            graph1.predecessors[0] is not None):
        print("NOK - init nefunguje jak ma na grafu o velikosti 1.")
        print("Matice vypada takto:")
        print_matrix(graph1)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(graph1.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(graph1.predecessors)
        return False

    graph2 = create_test_graph()
    initialize(graph2, 2)
    is_ok = (graph2.distances[2] == 0 and
             graph2.distances[0] == infinity and
             graph2.predecessors[2] is None)
    if not is_ok:
        print("NOK - init nefunguje jak ma na grafu o velikosti 6.")
        print("Matice vypada takto:")
        print_matrix(graph2)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(graph2.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(graph2.predecessors)
        return False

    print("OK")
    return True


def test_relax():
    print("Test 2. funkce relax: ")

    graph1 = create_test_graph()
    initialize(graph1, 0)
    relax(graph1, 0, 1)
    if graph1.distances[1] != 7 or graph1.predecessors[1] != 0:
        print("NOK - relax nefunguje jak ma na testovacim grafu ", end="")
        print("pri volani na vrcholy 0 1")
        print("Matice vypada takto:")
        print_matrix(graph1)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(graph1.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(graph1.predecessors)
        return

    graph2 = create_test_graph()
    initialize(graph2, 2)
    relax(graph2, 2, 0)
    relax(graph2, 0, 1)
    relax(graph2, 2, 1)
    if graph2.distances[1] != 10 or graph2.predecessors[1] != 2:
        print("NOK - init nefunguje jak ma na grafu o velikosti 6.")
        print("posloupnost provedenych akci - 1. initialize(g, 2):")
        tmp_graph = create_test_graph()
        initialize(tmp_graph, 2)
        print("Matice vypada takto:")
        print_matrix(tmp_graph)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(tmp_graph.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(tmp_graph.predecessors)

        print("\n2. relax(g, 2, 0):")
        relax(tmp_graph, 2, 0)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(tmp_graph.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(tmp_graph.predecessors)

        print("\n3. relax(g, 0, 1):")
        relax(tmp_graph, 0, 1)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(tmp_graph.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(tmp_graph.predecessors)

        print("\n4. relax(g, 2, 1):")
        relax(tmp_graph, 2, 1)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(tmp_graph.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(tmp_graph.predecessors)
        return

    print("OK")


def test_bellman_ford():
    print("Test 3. Bellman-Forduv algoritmus: ")

    graph1 = create_graph(5)
    add_edge(graph1, 0, 1, 1)
    ret = bellman_ford(graph1, 0, 1)
    if ret != 1:
        print("NOK - cesta z 0 do 1 ma delku 1.")
        print("Vas vystup je: {}".format(ret))
        print("Matice vypada takto:")
        print_matrix(graph1)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(graph1.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(graph1.predecessors)
        return

    graph2 = create_graph(5)
    add_edge(graph2, 0, 1, 1)
    ret = bellman_ford(graph2, 1, 2)
    if ret != infinity:
        print("NOK - cesta z 1 do 2 neexistuje ", end="")
        print("(delka je {}).".format(infinity))
        print("Vas vystup je: {}".format(ret))
        print("Matice vypada takto:")
        print_matrix(graph2)
        print("Seznam vzdalenosti z vrcholu 1 vypada takto:")
        print(graph2.distances)
        print("Seznam predchudcu na ceste z vrcholu 1 vypada takto:")
        print(graph2.predecessors)
        return

    graph3 = create_graph(1)
    ret = bellman_ford(graph3, 0, 0)
    if ret != 0:
        print("NOK - cesta z 0 do 0 ma delku 0.")
        print("Vas vystup je: {}".format(ret))
        print("Matice vypada takto:")
        print_matrix(graph3)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(graph3.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(graph3.predecessors)
        return

    graph4 = create_test_graph()
    ret = bellman_ford(graph4, 0, 4)
    if ret != 20:
        print("NOK - cesta z 0 do 4 ma delku 20.")
        print("Vas vystup je: {}".format(ret))
        print("Matice vypada takto:")
        print_matrix(graph4)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(graph4.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(graph4.predecessors)
        return

    print("OK")


def test_dijkstra():
    print("Test 4. Dijkstruv algoritmus: ")

    graph1 = create_graph(5)
    add_edge(graph1, 0, 1, 1)
    ret = dijkstra(graph1, 0, 1)
    if ret != 1:
        print("NOK - cesta z 0 do 1 ma delku 1.")
        print("Vas vystup je: {}".format(ret))
        print("Matice vypada takto:")
        print_matrix(graph1)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(graph1.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(graph1.predecessors)
        return

    graph2 = create_graph(5)
    add_edge(graph2, 0, 1, 1)
    ret = dijkstra(graph2, 1, 2)
    if ret != infinity:
        print("NOK - cesta z 1 do 2 neexistuje ", end="")
        print("(delka je {}).".format(infinity))
        print("Vas vystup je: {}".format(ret))
        print("Matice vypada takto:")
        print_matrix(graph2)
        print("Seznam vzdalenosti z vrcholu 1 vypada takto:")
        print(graph2.distances)
        print("Seznam predchudcu na ceste z vrcholu 1 vypada takto:")
        print(graph2.predecessors)
        return

    graph3 = create_graph(1)
    ret = dijkstra(graph3, 0, 0)
    if ret != 0:
        print("NOK - cesta z 0 do 0 ma delku 0.")
        print("Vas vystup je: {}".format(ret))
        print("Matice vypada takto:")
        print_matrix(graph3)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(graph3.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(graph3.predecessors)
        return

    graph4 = create_test_graph()
    ret = dijkstra(graph4, 0, 4)
    if ret != 20:
        print("NOK - cesta z 0 do 4 ma delku 20.")
        print("Vas vystup je: {}".format(ret))
        print("Matice vypada takto:")
        print_matrix(graph4)
        print("Seznam vzdalenosti z vrcholu 0 vypada takto:")
        print(graph4.distances)
        print("Seznam predchudcu na ceste z vrcholu 0 vypada takto:")
        print(graph4.predecessors)
        return

    print("OK")


def test_reflexive():
    print("Test 5. reflexive")
    graph1 = create_graph(2)
    graph1.matrix[0][0] = 1
    graph1.matrix[1][1] = 1
    if not is_reflexive(graph1):
        print("NOK1")
        return

    graph2 = create_graph(2)
    graph2.matrix[0][1] = 1
    graph2.matrix[1][0] = 1
    graph2.matrix[1][1] = None
    if is_reflexive(graph2):
        print("NOK2")
        return

    print("OK")

def test_symetric():
    print("Test 6. symetric")
    graph1 = create_graph(2)
    graph1.matrix[0][0] = 1
    graph1.matrix[1][1] = 1
    if is_symmetric(graph1):
        print("NOK1")
        return

    graph2 = create_graph(5)
    graph2.matrix[0][1] = 1
    graph2.matrix[1][0] = 1
    graph2.matrix[1][1] = None
    graph2.matrix[3][2] = 1
    graph2.matrix[2][3] = 1
    if not is_symmetric(graph2):
        print("NOK2")
        return

    graph3 = create_graph(5)
    graph3.matrix[0][1] = 1

    graph3.matrix[1][1] = None
    graph3.matrix[3][2] = 1
    graph3.matrix[2][3] = 1
    if is_symmetric(graph3):
        print("NOK2")
        return

    print("OK")


def test_antisymetric():
    print("Test 7. antisymetric")
    graph1 = create_graph(2)
    graph1.matrix[0][0] = 1
    graph1.matrix[1][1] = 1
    if not is_antisymmetric(graph1):
        print("NOK1")
        return

    graph2 = create_graph(5)
    graph2.matrix[0][1] = 1
    graph2.matrix[1][0] = 1
    graph2.matrix[1][1] = None
    graph2.matrix[3][2] = 1
    graph2.matrix[2][3] = 1
    if is_antisymmetric(graph2):
        print("NOK2")
        return

    graph3 = create_graph(5)
    graph3.matrix[0][1] = 1

    graph3.matrix[1][1] = None
    graph3.matrix[3][2] = 1
    graph3.matrix[2][3] = 1
    if is_antisymmetric(graph3):
        print("NOK3")
        return

    print("OK")


if __name__ == '__main__':
    if test_initialize():
        test_relax()
        test_bellman_ford()
        test_dijkstra()
        test_reflexive()
        test_symetric()
        test_antisymetric()
    makeGraph(create_test_graph(), "test12.dot")