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
#		 2           4
#     /   \       /   \
#    0  -  1  -  3  -  5     6
#
# is_bridge(graph, 0, 4) = False, neboť tato hrana v grafu není
# is_bridge(graph, 1, 3) = True, odebráním se graf rozpadne na dvě komponenty
# is_bridge(graph, 2, 1) = False, hrana se nachází na cyklu 0 - 1 - 2
#

#funkcia vyuziva find_all_cycles na vytvorenie zoznamu cyklov v grafe
#v tych potom hlada u, v sucasne, ak ich ani v jednom cykle spolocne nenajde
#prehlasi cestu medzi u, v za most
def is_bridge(matrix, u, v):
	if matrix[u][v] == 0:	#kontrolujeme ci cesta medzi zadanymi u, v vobec existuje
		return False	#ak nie, vraciame automaticky false
	u_bool = False	#priznak oznacujuci najdenie/nenajdenie premennej u v jednom z cyklov
	v_bool = False	#priznak oznacujuci najdenie/nenajdenie premennej v v jednom z cyklov
	list = []	#pomocny zoznam
	graph = {}	#dictionary v ktorom ukladame vsetky hrany v grafe pre funkciu find_all_cycles
	for x in range(len(matrix)):	#naplnenie slovnika graph
		for y in range(len(matrix)):
			if matrix[x][y] == 1:
				list.append(y)
		graph[x]=list
		list = []
	#na tomto mieste uz graph obsahuje vsetky hrany v tvare {0: [1, 4], 1: [0, 2], 2: [1, 3]} ....
	cycles = find_all_cycles(graph)	#zavolame funkciu na slovnik
	if cycles == -1:	#ak funkcia nenasla ani jeden cyklus
		return False	#vratime false
	for cycle in cycles:	#cyklus zapise do zoznamu list len tie cykly z cycles, ktore su dlhsie ako 2
		if len(cycle) > 2:
			list.append(cycle)
	#na tomto mieste uz list obsahuje vsetky cykly v grafe, dlhsie ako 2
	for x in list:	#hladame v zozname list taky cyklus, ktory obsahuje oba dane vrcholy u, v
		for i in x:
			if i == u:
				u_bool = True	#ak najde u oznaci priznak za true
			if i == v:
				v_bool = True	#ak najde v oznaci priznak za true
		if u_bool and v_bool:	#ak nasiel obe v jednom cykle, znamena to ze hrana medzi nimi nie je most
			return False	#takze vrati false
		u_bool = False	#"vynuluje" oba priznaky
		v_bool = False
	return True	#ak nenasiel taky cyklus, ktory by obsahoval oba vrcholy, znamena to, ze vrcholy su v samostatnych cykloch a teda tvoria most

def find_cycle_to_ancestor(spanning_tree, node, ancestor):
	path = []
	while (node != ancestor):
		if node is None:
			return []
		path.append(node)
		node = spanning_tree[node]
	path.append(node)
	return path

#funkcia najde pomocou dfs vsetky cykly v grafe danom slovnikom graph
def find_all_cycles(graph):
	cycles = []
	visited = []
	spanning_tree = {}
	check_cycles = 0

	def dfs(node):
		visited.append(node)
		for each in graph[node]:
			if each not in visited:
				spanning_tree[each] = node
				dfs(each)
			else:
				cycle = find_cycle_to_ancestor(spanning_tree, node, each)
				if cycle:
					cycles.append(cycle)

	for each in graph:
		if each not in visited:
			spanning_tree[each] = None
			dfs(each)

	if len(cycles) >= 1:
		return cycles	#vrati cykly vo forme zoznamu zoznamov
	else:
		return -1	#ak nenasiel ani jeden cyklus v grafe vrati -1

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
