#!/usr/bin/python
from __future__ import print_function
from copy import deepcopy

# Zadani ukolu:
#
# Mejme graf reprezentovany spolecnym polem nasledniku.
#
# Tato datova struktura ma tri polozky:
# 'size' - cislo vyjadrujici pocet vrcholu grafu
# 'first' - pole obsahujici indexy do 'edges'
# 'edges' - pole spolecnych nasledniku
#
# Podrobne vysvetleni je v prilozenem PDF.
#
# 1. cast (10 bodu): implementujte funkce outDegree, getEven, isCorrect
# 2. cast (10 bodu): implementujte funkci generateTransitionMatrix
# 3. cast (15 bodu): implementujte funkce isEdge a deleteOutEdges
# 4. cast (15 bodu): implementujte funkci countReachable
#
# Presny popis chovani uvedenych funkci je nize u jejich hlavicek.
#
# Pro ziskani plneho poctu bodu je treba dodrzet pozadovane slozitosti
# v zadani funkci. Ve vsech funkcich (krome isCorrect) muzete predpokladat,
# ze parametr graph je korektni graf.
#
# V pripade chyby testy vypisuji graf ve formatu dvou radku se seznamy.
# Tento format si muzete nechat vykreslit pomoci online nastroje na adrese:
# https://www.fi.muni.cz/~xbenes3/graph.cgi
#
# Pro zjednoduseni se omezime na grafy do velikosti MAX_GRAPH_SIZE.
MAX_GRAPH_SIZE = 100


# --- deklarace struktur ---


# Trida reprezentujici graf.  Vrcholy grafu jsou vzdy prirozena
# cisla 0, 1, ..., size - 1. Muzete predpokladat, ze graf nikdy nebude mit
# vice nez MAX_GRAPH_SIZE vrcholu.
class NGraph:
    def __init__(self):
        self.first = [0] * MAX_GRAPH_SIZE
        self.edges = [0] * MAX_GRAPH_SIZE
        self.size = 0


# -- pomocne funkce ---

def isValidVertex(graph, v):
    return v < graph.size and v >= 0


# --- 1. cast (10 bodu) ---


# Vrati vystupni stupen vrcholu 'v' v zadanem grafu.
# V pripade, ze 'v' neni validni vrchol grafu, vrati None.
# Pozadovana slozitost: konstantni.
def outDegree(graph, v):
    if v < 0 or v > graph.size - 1:
        return None
    degree = graph.first[v] - graph.first[v + 1]
    return degree if degree > -1 else (-1) * degree 


# Do seznamu evenList vlozi vsechny vrcholy zadaneho grafu, ktere maji sudy
# vystupni stupen.
# Prirozene predpokladame, ze vrcholy budou usporadane (od nejmensiho).
# Pozadovana slozitost: linearni v poctu vrcholu grafu, tj. O(V).
def getEven(graph, evenList):
    for i in range(len(graph.first)):
        degree = outDegree(graph, i)
        if degree is not None and degree % 2 == 0:
            evenList.append(i)


# Overi, ze zadany graf je korektni graf reprezentovany spolecnym polem
# nasledniku - viz prilozene PDF. Nemusite kontrolovat, jestli nejaka
# hrana neni v grafu vicekrat.
# Pozadovana slozitost: nejvyse linearni vuci poctu vrcholu a hran,
# tj. O(V + E).

def check_vertices(graph):
    if graph.size < 1:
        return True             # False, or not at all?
    minimum = graph.first[0]
    if minimum != 0:
        return False
    for i in range(1, graph.size + 1):
        if minimum > graph.first[i]:
            return False
        minimum = graph.first[i]
    if minimum != graph.first[graph.size]:
        return False
    return True


def check_edges(graph):
    edges = graph.first[graph.size]
    for i in range(edges):
        if graph.edges[i] < 0 or graph.edges[i] > graph.size - 1:
            return False
    return True


def isCorrect(graph):
    return check_vertices(graph) and check_edges(graph)


# --- 2. cast (10 bodu) ---

# Pro zadany graf vytvori matici sousednosti, kterou vrati jako vysledek.
# Matici 'matrix' o rozmerech m*n naplnenou hodnotami False v Pythonu vytvorite
# pomoci zapisu matrix = [[False]*n for i in range(m)]
# Pozadovana slozitost: linearni v poctu hran grafu, tj. O(E).
# Do slozitosti funkce nezapocitavame cas potrebny k vytvoreni matice.

def find_edges(graph, vertex, degree):
    while degree == 0:
        vertex += 1
        degree = outDegree(graph, vertex)
    return vertex, degree


def generateTransitionMatrix(graph):
    matrix = [[False]*graph.size for i in range(graph.size)]
    edges = graph.first[graph.size]
    vertex, degree = 0, outDegree(graph, 0)
    for i in range(edges):
        edge = graph.edges[i]
        if degree == 0:
            vertex, degree = find_edges(graph, vertex, degree)
        matrix[vertex][edge] = True
        degree -= 1
    return matrix


# --- 3. cast (15 bodu) ---

# Vraci True, pokud '(u,v)' je hranou zadaneho grafu, jinak vraci False.
# Muzete predpokladat, ze 'u' i 'v' jsou validni vrcholy grafu.
# Pozadovana slozitost: nejvyse linearni k poctu vrcholu, tj. O(V).

def isEdge(graph, u, v):
    start, stop = graph.first[u], graph.first[u + 1]
    for i in range(start, stop):
        if graph.edges[i] == v:
            return True
    return False


# Vymaze vsechny odchozi hrany vrcholu 'v' ze zadaneho grafu. Muzete
# predpokladat, ze 'v' je validni vrchol grafu.
# Pozadovana slozitost: nejvyse linearni vuci poctu vrcholu a hran,
# tj. O(V + E).

def deleteOutEdges(graph, v):
    start, stop = graph.first[v], graph.first[v + 1]
    remove_index, remove_edges = start, 0 
    for i in range(start, stop):
        del graph.edges[remove_index]
        remove_edges += 1
    graph.first[v + 1] = graph.first[v]
    for i in range(v + 2, graph.size + 1):
        graph.first[i] -= remove_edges


# --- 4. cast (15 bodu) ---

# Pro zadany graf a jeho vrchol 'v' spocita pocet vrcholu dosazitelnych z 'v'
# (tj. pocet vrcholu, do kterych z 'v' vede orientovana cesta). Pripominame,
# ze kazdy vrchol je dosazitelny sam ze sebe (cestou delky nula).
# Muzete predpokladat, ze 'v' je validni vrchol grafu.
# Pozadovana slozitost: nejvyse linearni vuci poctu vrcholu a hran,
# tj. O(V + E).
# Reste v zadane datove strukture. Prevodem pomoci generateTransitionMatrix
# prekrocite pozadovanou slozitost, protoze jiz budeme zapocitavat tvorbu
# matice.

import collections

def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        start, stop = graph.first[vertex], graph.first[vertex + 1]
        for i in range(start, stop):
            if graph.edges[i] not in visited:
                visited.add(graph.edges[i])
                queue.append(graph.edges[i])
    return visited


def countReachable(graph, v):
    visited = bfs(graph, v)
    return len(visited)


# Hlavni funkce volana automaticky po spusteni programu.
# Pokud chcete krome dodanych testu spustit vlastni testovaci kod, dopiste ho
# sem. Odevzdavejte reseni s puvodni verzi teto funkce.


def main():
    testForEach("outDegree", testOutDegree)
    testForEach("getEven", testGetEven)
    testForEach("isCorrect", testIsCorrect, correctonly=False)
    testForEach("generateTransitionMatrix", testMatrix)
    b = testForEach("isEdge", testIsEdge)
    if b:
        testForEach("deleteOutEdges", testDeleteOutEdges, report=False)
    else:
        print("Upozorneni: Test deleteEdge je mozno provest pouze",
              "s funkcni implementaci isEdge.")
    testForEach("countReachable", testCountReachable)
    print("------------------------------------")


#
# Nasleduje kod testu, NEMODIFIKUJTE JEJ               ## #
#


def printArray(array, size):
    print(array[:size])


def printGraph(graph):
    printArray(graph.first, graph.size + 1)
    printArray(graph.edges, graph.first[graph.size])


class TestCase:
    def __init__(self, graph, outDegree, evenList, matrix,
                 deleteVertices, reachable, correct):
        self.graph = NGraph()
        self.graph.size = graph[0]
        self.graph.first[:len(graph[1])] = graph[1]
        self.graph.edges[:len(graph[2])] = graph[2]
        self.outDegree = outDegree
        self.evenList = evenList
        self.matrix = matrix
        self.deleteVertices = deleteVertices
        self.reachable = reachable
        self.correct = correct


testCases = [
    # z PDF
    TestCase([4, [0, 2, 3, 3, 7], [1, 2, 1, 3, 0, 1, 2]],
             [2, 1, 0, 4],
             [0, 2, 3],
             [[0, 1, 1, 0],
              [0, 1, 0, 0],
              [0, 0, 0, 0],
              [1, 1, 1, 1]],
             [3, 1, 2, 1, 3],
             [3, 1, 1, 4],
             True),
    # jeden vrchol bez hran
    TestCase([1, [0, 0], [0]],
             [0],
             [0],
             [[0]],
             [0, 0, 0, 0, 0],
             [1],
             True),
    # 4 vrcholy bez hran
    TestCase([4, [0, 0, 0, 0, 0], [0]],
             [0, 0, 0, 0],
             [0, 1, 2, 3],
             [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]],
             [3, 1, 3, 0, 3],
             [1, 1, 1, 1],
             True),
    # puvodni z testu
    TestCase([6, [0, 2, 3, 5, 9, 10, 10], [1, 2, 0, 0, 3, 0, 1, 2, 3, 5]],
             [2, 1, 2, 4, 1, 0],
             [0, 2, 3, 5],
             [[0, 1, 1, 0, 0, 0],
              [1, 0, 0, 0, 0, 0],
              [1, 0, 0, 1, 0, 0],
              [1, 1, 1, 1, 0, 0],
              [0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0]],
             [3, 4, 5, 5, 3],
             [4, 4, 4, 4, 2, 1],
             True),
    # dalsi nejaky
    TestCase([4, [0, 1, 2, 2, 5], [1, 1, 3, 0, 1]],
             [1, 1, 0, 3],
             [2],
             [[0, 1, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 0, 0],
              [1, 1, 0, 1]],
             [3, 0, 0, 3, 3],
             [2, 1, 1, 3],
             True),
    # cyklus vicenasobny na 4 vrcholech
    TestCase([4, [0, 1, 2, 3, 6], [1, 2, 3, 3, 0, 1]],
             [1, 1, 1, 3],
             [],
             [[0, 1, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1],
              [1, 1, 0, 1]],
             [1, 0, 2, 2, 1],
             [4, 4, 4, 4],
             True),
    # uplny na 1 vrcholu
    TestCase([1, [0, 1], [0]],
             [1],
             [],
             [[1]],
             [0, 0, 0, 0, 0],
             [1],
             True),
    # uplny na 2 vrcholech
    TestCase([2, [0, 2, 4], [0, 1, 0, 1]],
             [2, 2],
             [0, 1],
             [[1, 1],
              [1, 1]],
             [1, 0, 1, 0, 1],
             [2, 2],
             True),
    # uplny na 3 vrcholech
    TestCase([3, [0, 3, 6, 9], [0, 1, 2, 0, 1, 2, 0, 1, 2]],
             [3, 3, 3],
             [],
             [[1, 1, 1],
              [1, 1, 1],
              [1, 1, 1]],
             [2, 1, 2, 2, 2],
             [3, 3, 3],
             True),
    # uplny na 4 vrcholu
    TestCase([4, [0, 4, 8, 12, 16],
              [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]],
             [4, 4, 4, 4],
             [0, 1, 2, 3],
             [[1, 1, 1, 1],
              [1, 1, 1, 1],
              [1, 1, 1, 1],
              [1, 1, 1, 1]],
             [0, 3, 1, 0, 0],
             [4, 4, 4, 4],
             True),
    # uplny na 5 vrcholech
    TestCase([5, [0, 5, 10, 15, 20, 25],
              [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0,
               1, 2, 3, 4]],
             [5, 5, 5, 5, 5],
             [],
             [[1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1]],
             [4, 1, 4, 2, 4],
             [5, 5, 5, 5, 5],
             True),
    # DAG doprednych hran v usporadani se smyckami
    TestCase([5, [0, 5, 9, 12, 14, 15],
              [0, 1, 2, 3, 4, 1, 2, 3, 4, 2, 3, 4, 3, 4, 4]],
             [5, 4, 3, 2, 1],
             [1, 3],
             [[1, 1, 1, 1, 1],
              [0, 1, 1, 1, 1],
              [0, 0, 1, 1, 1],
              [0, 0, 0, 1, 1],
              [0, 0, 0, 0, 1]],
             [2, 1, 3, 1, 2],
             [5, 4, 3, 2, 1],
             True),
    # DAG doprednych hran v usporadani bez smycek
    TestCase([5, [0, 4, 7, 9, 10, 10], [1, 2, 3, 4, 2, 3, 4, 3, 4, 4]],
             [4, 3, 2, 1, 0],
             [0, 2, 4],
             [[0, 1, 1, 1, 1],
              [0, 0, 1, 1, 1],
              [0, 0, 0, 1, 1],
              [0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0]],
             [2, 1, 4, 2, 2],
             [5, 4, 3, 2, 1],
             True),
    # prehazene poradi nasledniku
    TestCase([5, [0, 4, 7, 9, 10, 10], [1, 4, 3, 2, 4, 3, 2, 3, 4, 4]],
             [4, 3, 2, 1, 0],
             [0, 2, 4],
             [[0, 1, 1, 1, 1],
              [0, 0, 1, 1, 1],
              [0, 0, 0, 1, 1],
              [0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0]],
             [3, 3, 3, 0, 3],
             [5, 4, 3, 2, 1],
             True),
    # nesouvisly, dve komponenty
    TestCase([8, [0, 4, 8, 12, 16, 18, 20, 20, 20],
              [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 5, 7, 6, 5]],
             [4, 4, 4, 4, 2, 2, 0, 0],
             [0, 1, 2, 3, 4, 5, 6, 7],
             [[1, 1, 1, 1, 0, 0, 0, 0],
              [1, 1, 1, 1, 0, 0, 0, 0],
              [1, 1, 1, 1, 0, 0, 0, 0],
              [1, 1, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 1],
              [0, 0, 0, 0, 0, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]],
             [2, 4, 4, 2, 2],
             [4, 4, 4, 4, 4, 2, 1, 1],
             True),
    # ternarni strom
    TestCase([19, [0, 3, 6, 9, 12, 15, 18, 18, 18, 18, 18, 18, 18, 18, 18,
                   18, 18, 18, 18, 18],
              [3, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]],
             [3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
             [[0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
             [7, 8, 4, 17, 7],
             [19, 10, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             True),
    # predchozi s DAG hranou
    TestCase([19, [0, 3, 6, 9, 12, 15, 18, 18, 18, 18, 18, 18, 18, 18, 18,
                   18, 18, 18, 18, 19],
              [3, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
               4]],
             [3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
             [[0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
             [17, 6, 10, 16, 17],
             [19, 10, 4, 4, 4, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5],
             True),
    # predchozi se zpetnou hranou
    TestCase([19, [0, 3, 6, 9, 12, 15, 18, 18, 18, 18, 18, 18, 18, 18, 18,
                   18, 18, 18, 18, 19],
              [3, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
               1]],
             [3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
             [[0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
             [10, 3, 15, 5, 10],
             [19, 10, 4, 4, 4, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10],
             True),
    # DAG s vice "koreny"
    TestCase([11, [0, 3, 7, 9, 11, 13, 14, 15, 15, 16, 16, 16],
              [5, 7, 8, 5, 7, 9, 10, 8, 10, 5, 8, 8, 10, 6, 10, 10]],
             [3, 4, 2, 2, 2, 1, 1, 0, 1, 0, 0],
             [1, 2, 3, 4, 7, 9, 10],
             [[0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
              [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
              [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
             [4, 0, 2, 5, 4],
             [6, 6, 3, 5, 3, 3, 2, 1, 2, 1, 1],
             True),
    # DAG s vice "koreny" + dve zpetne hrany
    TestCase([11, [0, 3, 5, 6, 7, 9, 11, 11, 12, 13, 13, 14],
              [5, 7, 10, 4, 7, 7, 6, 9, 10, 8, 10, 10, 9, 1]],
             [3, 2, 1, 1, 2, 2, 0, 1, 1, 0, 1],
             [1, 4, 5, 6, 9],
             [[0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
              [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
             [3, 2, 8, 0, 3],
             [8, 5, 6, 2, 5, 7, 1, 5, 2, 1, 5],
             True),
    # nekorektni
    TestCase([1, [0, 1], [1]],
             [0], [], [[0]], [0], [0], False),
    TestCase([5, [0, 2, 4, 6, 5], [0, 1, 0, 1, 0, 1]],
             [0], [], [[0]], [0], [0], False),
    TestCase([4, [0, 2, 3, 4], [1, 1, 1, 1]],
             [0], [], [[0]], [0], [0], False),
    TestCase([3, [1, 2, 3, 4], [1, 1, 1, 1]],
             [0], [], [[0]], [0], [0], False),
    TestCase([6, [0, 3, 3, 3, 3, 3, 3], [0, 1, 6]],
             [0], [], [[0]], [0], [0], False),
    TestCase([2, [0, 2, 4], [0, 1, 0, 7]],
             [0], [], [[0]], [0], [0], False),
    TestCase([6, [0, 3, 3, 3, 3, 3, 3], [0, 1, -1]],
             [0], [], [[0]], [0], [0], False),
    TestCase([3, [0, 2, 2, 0], [0, 1]],
             [0], [], [[0]], [0], [0], False),
    # korektni
    TestCase([1, [0, 1], [0, 42]],
             [1],
             [],
             [[1]],
             [0, 0, 0, 0, 0],
             [1],
             True),
]
testCount = len(testCases)


def equalGraph(graphA, graphB):
    if graphA.size != graphB.size:
        return False
    for i in range(graphA.size + 1):
        if graphA.first[i] != graphB.first[i]:
            return False
    for i in range(graphA.first[graphA.size]):
        if graphA.edges[i] != graphB.edges[i]:
            return False
    return True


def reportGraph(graph):
    print("\tGraf na kterem byla nalezena chyba:")
    printGraph(graph)


def testEqualGraph(original, current):
    if not equalGraph(original, current):
        print("NOK: pri volani funkce doslo ke zmene puvodniho grafu")
        print("\tZmeneny graf:")
        printGraph(current)
        current.size = original.size
        current.first = deepcopy(original.first)
        current.edges = deepcopy(original.edges)
        return False
    return True


def testODAux(v, graph, correct):
    original = deepcopy(graph)
    result = outDegree(graph, v)
    if not testEqualGraph(original, graph):
        return False
    if result != correct:
        print("NOK, spatna odpoved pro vrchol %s:" % v,
              "melo byt %s, ale odpoved byla %s" % (correct, result))
        return False
    return True


def testOutDegree(t):
    invalid = [-1, -17, t.graph.size, t.graph.size + 1, 2000]

    for i in range(t.graph.size):
        if not testODAux(i, t.graph, t.outDegree[i]):
            return False

    for inv in invalid:
        if not testODAux(inv, t.graph, None):
            return False

    return True


def testGetEven(t):
    original = deepcopy(t.graph)
    l = []
    getEven(t.graph, l)
    if not testEqualGraph(original, t.graph):
        return False
    if l != t.evenList:
        print("NOK\n\tVase odpoved: %s" % l,
              "\n\tspravna odpoved: %s" % t.evenList)
        return False
    return True


def testIsCorrect(t):
    original = deepcopy(t.graph)
    result = isCorrect(t.graph)
    if not testEqualGraph(original, t.graph):
        return False
    if result != t.correct:
        print("NOK, spatna odpoved %s, melo byt %s" % (result, t.correct))
        return False
    return True


def testMatrixAux(answer, correct, i, j):
    if answer != correct:
        print("NOK, v matici je chyba na pozici [%s][%s] --" % (i, j),
              "ma byt %s, ale je %s" % (bool(correct), answer))
        return False
    return True


def testMatrix(t):
    if t.graph.size == 0:
        return True
    original = deepcopy(t.graph)
    matrix = generateTransitionMatrix(t.graph)
    if not testEqualGraph(original, t.graph):
        return False
    if matrix is None:
        print("NOK, funkce vraci None")
        return False
    for i in range(t.graph.size):
        for j in range(t.graph.size):
            if not testMatrixAux(matrix[i][j], t.matrix[i][j], i, j):
                return False
    return True


def testIsEdgeAux(graph, matrix):
    original = deepcopy(graph)
    for i in range(graph.size):
        for j in range(graph.size):
            result = isEdge(graph, i, j)
            if not testEqualGraph(original, graph):
                return False, -1, -1, -1, -1
            if result != matrix[i][j]:
                return False, i, j, matrix[i][j], result
    return True, 0, 0, 0, 0


def testIsEdge(t):
    result, u, v, b, answer = testIsEdgeAux(t.graph, t.matrix)
    if not result:
        if u == -1:
            return False
        print("NOK, chybna odpoved pro hranu (%s, %s):" % (u, v),
              "ma byt %s ale je %s" % (bool(b), answer))
        return False
    return True


def testDeleteOutEdges(t):
    original = deepcopy(t.graph)
    for v in t.deleteVertices:
        copy = deepcopy(t.graph)
        deleteOutEdges(t.graph, v)
        if t.graph.size != copy.size:
            print("NOK, chyba pri mazani hran vrcholu %d:" % v,
                  "vysledny graf ma spatnou velikost",
                  "(%d misto %d)" % (t.graph.size, copy.size))
            print("\tPuvodni graf (pred mazanim):")
            printGraph(copy)
            print("\tVas graf po mazani:")
            printGraph(t.graph)
            t.graph = original
            return False
        for u in range(t.graph.size):
            t.matrix[v][u] = False
        result, x, y, b, a = testIsEdgeAux(t.graph, t.matrix)
        if not result:
            if x == -1:
                print("\t(Zrejme je chybna funkce isEdge.)")
                return False
            print("NOK, chyba pri mazani hran vrcholu %s:" % v,
                  "ve vyslednem grafu", "chybi" if b else "prebyva",
                  "hrana (%s, %s)" % (x, y))
            print("\tPuvodni graf (pred mazanim):")
            printGraph(copy)
            print("\tVas graf po mazani:")
            printGraph(t.graph)
            t.graph = original
            return False
    t.graph = original
    return True


def testCountReachable(t):
    original = deepcopy(t.graph)
    for i in range(t.graph.size):
        count = countReachable(t.graph, i)
        if not testEqualGraph(original, t.graph):
            return False
        if count != t.reachable[i]:
            print("NOK: spatna odpoved pro vrchol %s:" % i,
                  "melo byt %s, ale odpoved byla %s" % (t.reachable[i], count))
            return False
    return True


def testForEach(msg, test, report=True, correctonly=True):
    print("------------------------------------\nTest %s: " % msg, end="")
    for i in range(testCount):
        if correctonly and not testCases[i].correct:
            continue
        b = test(testCases[i])
        if not b:
            if report:
                reportGraph(testCases[i].graph)
            return False
    print("OK")
    return True


if __name__ == '__main__':
    main()
