#!/usr/bin/env python3

import copy

# Povolene knihovny: copy, math, collections

# IB002 Domaci uloha 12.
#
# S relacemi se vetsina z vas setkala na predmetu Matematicke zaklady
# informatiky. Relace na mnozine intuitivne popisuje vztah mezi prvky
# teto mnoziny. Mejme treba relaci "byt kamaradem", kdy prvky A a B
# (z mnoziny lidi) jsou v relaci, pokud A je kamaradem B.
# Orientovany graf lze chapat jako (binarni) relaci mezi prvky, kde uzly
# reprezentuji prvky mnoziny a z uzlu A do B vede hrana, prave kdyz je
# A v relaci s B.

# Mezi zakladni vlastnosti binarnich relaci patri:
#
# *reflexivita*
# Relace je reflexivni, pokud je kazdy prvek v relaci sam se sebou.
#
# *symetrie*
# Relace je symetricka, pokud pro libovolne dva prvky A a B plati:
# Pokud A je v relaci s B, pak je taky B v relaci s A.
#
# *antisymetrie*
# Relace je antisymetricka, pokud pro libovolne dva ruzne prvky A a B plati:
# Pokud A je v relaci s B, pak B neni v relaci s A.
#
# *tranzitivita*
# Relace je tranzitivni, pokud pro libovolne prvky A, B, C plati:
# Je-li A v relaci s B a B je v relaci s C, pak taky A je v relaci s C.


# Nasledujici definici tridy Graph nijak nemodifikujte.
# Reprezentace grafu je stejna jako v minulem du.

class Graph:
    """Trida Graph drzi graf reprezentovany matici sousednosti.
    Atributy:
        size: velikost (pocet vrcholu) grafu
        matrix: matice sousednosti
                [u][v] reprezentuje hranu u -> v
                (True: hrana existuje, False: hrana neexistuje)
    """

    def __init__(self, size):
        self.size = size
        self.matrix = [[False] * size for _ in range(size)]


# Ukol 1.
# Implementujte funkce is_reflexive, is_symmetric, is_antisymmetric
# a is_transitive, ktere pro vstupni graf overi, zda jim reprezentovana relace
# splnuje podminky dane vlastnosti.

def is_reflexive(graph):
    """Zjisti, zda je relace zadana grafem reflexivni.
    Vstup: graph - orientovany graf typu Graph
    Vystup: True/False
    casova slozitost: O(n), kde n je pocet vrcholu grafu
    extrasekvencni prostorova slozitost: O(1)
    """
    for i in range(graph.size):
        if not graph.matrix[i][i]:
            return False
    return True


def is_symmetric(graph):
    """Zjisti, zda je relace zadana grafem symetricka.
    Vstup: graph - orientovany graf typu Graph
    Vystup: True/False
    casova slozitost: O(n^2), kde n je pocet vrcholu grafu
    extrasekvencni prostorova slozitost: O(1)
    """
    for i in range(graph.size):
        for j in range(graph.size):
            if graph.matrix[i][j]and not graph.matrix[j][i]:
                return False
    return True


def is_antisymmetric(graph):
    """Zjisti, zda je relace zadana grafem antisymetricka.
    Vstup: graph - orientovany graf typu Graph
    Vystup: True/False
    casova slozitost: O(n^2), kde n je pocet vrcholu grafu
    extrasekvencni prostorova slozitost: O(1)
    """
    for i in range(graph.size):
        for j in range(graph.size):
            if graph.matrix[i][j] and graph.matrix[j][i] and i != j:
                return False
    return True


def is_transitive(graph):
    """Zjisti, zda je relace zadana grafem tranzitivni.
    Vstup: graph - orientovany graf typu Graph
    Vystup: True/False
    casova slozitost: O(n^3), kde n je pocet vrcholu grafu
    extrasekvencni prostorova slozitost: O(1)
    """
    for i in range(graph.size):
        for j in range(graph.size):
            if graph.matrix[i][j]:
                for k in range(graph.size):
                    if graph.matrix[j][k] and not graph.matrix[i][k]:
                        return False
    return True


# Ukol 2.
# Implementujte funkci transitive_closure, ktera spocita tranzitivni
# uzaver daneho grafu. Tranzitivni uzaver je nejmensi nadmnozina relace,
# ktera splnuje podminky pro tranzitivitu (relace je chapana jako mnozina
# vsech dvojic, ktere jsou v dane relaci).
#
# Tranzitivni uzaver grafu lze taky definovat jako graf, ve kterem vede
# hrana z vrcholu A do vrcholu B, pokud v puvodnim grafu existovala
# nejaka orientovana cesta vedouci z vrcholu A do vrcholu B.
#
# Puvodni graf nemente, vytvorte si kopii.

def transitive_closure(graph):
    """Vypocita tranzitivni uzaver zadaneho grafu.
    Vstup: graph - orientovany graf typu Graph
    Vystup: tranzitivni uzaver grafu (objekt typu Graph)
    casova slozitost: O(n^3), kde n je pocet vrcholu grafu
    """
    closure = copy.deepcopy(graph)
    for k in range(closure.size):
        for i in range(closure.size):
            for j in range(closure.size):
                closure.matrix[i][j] = closure.matrix[i][j] or (closure.matrix[i][k] and closure.matrix[k][j])
    return closure
