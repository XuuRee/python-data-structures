# -*- coding: utf-8 -*-
# Implementační test IB002 - úloha 1. (lehčí, 12 bodů)

# Vyplňte následující údaje:
# Jméno:
# UČO:
# Skupina:

#
# Vytvoří prázdnou matici sousednosti pro graf o n vrcholech.
#
def createGraph(n):
    return [[0] * n for i in range(n)]


#
# Přidá hranu (u,v) do grafu. Graf je neorientovaný, tj. hrany jsou obousměrné.
#
def add_edge(matrix, u, v):
    matrix[u][v] = 1
    matrix[v][u] = 1


#
# ÚKOL:
# Naprogramujte funkci, která ověří, že je daná hrana mostem. Hrana v grafu
# se nazývá most, pokud neleží na žádném cyklu (a jejím odebráním by se tedy
# graf rozpadnul na více komponent).
#
# Funkce dostane graf zadaný maticí sousednosti, a dva vrcholy u, v
# (resp. jejich čísla). Funkce vrací True nebo False.
# Pokud hrana (u,v) v grafu není, vraťte False.
# Pokud hrana (u,v) v grafu je, vraťte True pokud je mostem, False pokud ne.
#
# Příklad:
#       2           4
#     /   \       /   \
#    0  -  1  -  3  -  5     6
#
# is_bridge(graph, 0, 4) = False, neboť tato hrana v grafu není
# is_bridge(graph, 1, 3) = True, odebráním se graf rozpadne na dvě komponenty
# is_bridge(graph, 2, 1) = False, hrana se nachází na cyklu 0 - 1 - 2
#

def is_bridge(matrix, u, v):
    if matrix[u][v] == 0:
        return False
    matrix[u][v] = 0
    matrix[v][u] = 0
    if not is_connected(matrix, u, v):
        add_edge(matrix, u, v)
        return True
    add_edge(matrix, u, v)
    return False

def is_connected(matrix, u, v):
    n = len(matrix)
    visited = [False]*n
    stack = [u]
    while stack:
        current = stack.pop()
        if current == v:
            return True
        else:
            if not visited[current]:
                visited[current] = True
                for x in range(n):
                    if not visited[x] and matrix[current][x] != 0:
                        stack.append(x)
    return False


#
# Následící kod testuje funkcionalitu. Neupravujte.
# Každý test obsahuje několik volání vaší funkce. Test je úspěšný jen pokud
# všechny volání vrátí správnou odpověď.
#

def test(graph, u, v, expectation):
    if is_bridge(graph, u, v) == expectation:
        print("Ok.")
    else:
        print("Chyba, pro hranu (%i, %i) je správná odpověď %s" % (u, v, str(expectation)))

# Graf z obrázku výše
graph = createGraph(7)
add_edge(graph, 0, 1)
add_edge(graph, 1, 2)
add_edge(graph, 2, 0)
add_edge(graph, 1, 3)
add_edge(graph, 3, 4)
add_edge(graph, 4, 5)
add_edge(graph, 5, 3)

print("Test 1.:")
test(graph, 0, 4, False)  # neexistujici hrana v jedné komponenta
test(graph, 5, 6, False)  # neexistujici hrana mezi komponentami

print("Test 2.:")
test(graph, 0, 2, False)  # není mostem
test(graph, 1, 3, True)  # je mostem

print("Test 3.:")
test(graph, 2, 1, False)  # otestovaní všech hran na levém cyklu
test(graph, 1, 0, False)
test(graph, 2, 0, False)
test(graph, 1, 2, False)
test(graph, 0, 1, False)
test(graph, 3, 1, True)  # test mostu druhým směrem

# Složitější graf
graph = createGraph(10)
add_edge(graph, 0, 1)
add_edge(graph, 1, 2)
add_edge(graph, 2, 3)
add_edge(graph, 3, 4)
add_edge(graph, 4, 0)

add_edge(graph, 5, 6)
add_edge(graph, 6, 7)
add_edge(graph, 7, 5)

add_edge(graph, 3, 6)
add_edge(graph, 8, 9)

print("Test 4.:")
test(graph, 8, 9, True)
test(graph, 0, 1, False)  # hrana velkého cyklu
test(graph, 5, 6, False)  # hrana malého cyklu

print("Test 5.:")
test(graph, 3, 6, True)  # propojka mezi cykly
test(graph, 6, 5, False)
test(graph, 6, 7, False)
test(graph, 2, 3, False)
test(graph, 4, 3, False)

print("Test 6.:")
test(graph, 6, 3, True)  # propojka mezi cykly
test(graph, 5, 6, False)
test(graph, 7, 6, False)
test(graph, 3, 2, False)
test(graph, 3, 4, False)
