#!/usr/bin/env python3

# Povolene knihovny: copy, math, collections
# Z knihovny collections se vam muze hodit datova struktura deque:

from collections import deque


# IB002 Domaci uloha 11.
#
# Tento tyden bude vasim ukolem implementovat dva grafove algoritmy.
# Ukoly jsou zamereny na aplikace pruchodu grafem.
#
# Reprezentace grafu je stejna jako v ukolu cv11, tedy matici sousednosti.
# Matice je indexovana od [0][0], vrcholum odpovidaji cisla 0 .. graph.size-1.
# V matici je na indexu [u][v] hodnota True, pokud graf obsahuje hranu u -> v,
# jinak je tam hodnota False.
#
# Grafy (i neorientovane!) mohou obsahovat smycky (tj. situace, kdy v matici
# na indexu [u][u] je True) a mohou byt i nesouvisle.
#
# Pripomenuti prace s frontou typu deque:
# inicializace fronty: queue = deque() nebo queue = deque([seznam prvku])
# vlozeni prvku do fronty: queue.append(prvek)
# vybrani prvku z fronty: queue.popleft(prvek)
#
# Definici tridy Graph nijak nemodifikujte, ani nepridavejte zadne atributy.
# Zamerne se v teto uloze budete muset obejit bez pomocnych poli ve tride
# Graph; budete muset pouzit lokalni promenne a pripadne parametry v rekurzi.
#
# Nepouzivejte globalni promenne. I kdyz je mozne, ze vyhodnocovaci sluzba
# neodhali vsechna pouziti globalnich promennych, u implementacnich testu
# vas pouzivani globalnich promennych zbytecne pripravi o body. Ma tedy smysl
# se naucit programovat spravne uz ted.


class Graph:
    """Trida Graph drzi graf reprezentovany matici sousednosti.
    Atributy:
        size: velikost (pocet vrcholu) grafu
        matrix: matice sousednosti
                [u][v] reprezentuje hranu u -> v
    """

    def __init__(self, size):
        self.size = size
        self.matrix = [[False] * size for _ in range(size)]


# Ukol 1.
# Implementujte funkci colourable, ktera zjisti, zda je dany neorientovany graf
# obarvitelny dvema barvami tak, aby kazde dva sousedni vrcholy mely ruznou
# barvu.
#
# Neorientovany graf v nasi reprezentaci znamena, ze
#    graph.matrix[u][v] == graph.matrix[v][u] pro vsechny vrcholy u, v.


def bfs(graph, root, visited, white, black):
    white.add(root)
    queue = deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        if vertex in white:
            good_color, bad_color = black, white
        else:
            good_color, bad_color = white, black
        for item in range(graph.size):
            if graph.matrix[vertex][item]:
                if item in bad_color:
                    return False
                good_color.add(item)
                if item not in visited:
                    visited.add(item)
                    queue.append(item)
    return True


def colourable(graph):
    """Zjisti, zda je zadany neorientovany graf obarvitelny dvema barvami.
    Vstup:
        graph - neorientovany graf typu Graph
    Vystup:
        True, pokud je graf obarvitelny dvema barvami
        False, jinak
    casova slozitost: O(n^2), kde n je pocet vrcholu grafu
    extrasekvencni prostorova slozitost: O(n), kde n je pocet vrcholu grafu
    """
    visited, not_visited = set(), set([x for x in range(graph.size)])
    black, white = set(), set()
    while not_visited:
        if not bfs(graph, not_visited.pop(), visited, white, black):
            return False
        not_visited -= visited
    return True


# Ukol 2.
# Implementujte funkci compute_dependencies, ktera pro zadany orientovany graf
# spocita topologicke usporadani vrcholu, tj. ocislovani vrcholu takove, ze
# kazda hrana vede z vrcholu s nizsim cislem do vrcholu s vyssim cislem.
#
# Vystupem je pole zadavajici topologicke usporadani (ocislovani vrcholu),
# kde na prvni pozici (tedy s indexem 0) je vrchol nejmensi
# v tomto usporadani, tj. nevede do nej zadna hrana,
# a na posledni pozici vrchol nejvetsi, tj. nevede z nej zadna hrana.
# Pokud topologicke usporadani neexistuje, algoritmus vraci None.
#
# Priklad:
#    mejme graf s vrcholy 0, 1, 2 a hranami 0 -> 1, 2 -> 1, 2 -> 0;
#    vystupem bude pole (Pythonovsky seznam] [2, 0, 1]


class GraphCycle:

    def __init__(self):
        self.cycle = False


def topological_sort(vertex, visited, graph, stack, contains, path):
    visited[vertex] = True
    path.add(vertex)
    for item in range(graph.size):
        if graph.matrix[vertex][item]:
            if visited[item] and item in path:
                contains.cycle = True
            if not visited[item]:
                topological_sort(item, visited, graph, stack, contains, path)
    path.remove(vertex)
    stack.insert(0, vertex)


def compute_dependencies(graph):
    """Spocita topologicke usporadani vrcholu v grafu.
    Vstup:
        graph - orientovany graf typu Graph
    Vystup:
        pole cisel reprezentujici topologicke usporadani vrcholu
        None, pokud zadne topologicke usporadani neexistuje
    casova slozitost: O(n^2), kde n je pocet vrcholu grafu
    extrasekvencni prostorova slozitost: O(n), kde n je pocet vrcholu grafu
    """
    contains = GraphCycle()
    stack = []
    if graph.size < 1:
        return stack
    visited = [False] * graph.size
    for vertex in range(graph.size):
        if not visited[vertex]:
            topological_sort(vertex, visited, graph, stack, contains, set())
    if contains.cycle:
        return None
    return stack
