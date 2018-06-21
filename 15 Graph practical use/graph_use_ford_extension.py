##
 # Implementacny test IB002 - uloha 1. (12 bodov)
 #
 # Vyplnte nasledujuce udaje:
 # Meno:
 # UCO:
 # Skupina (v ktorej ste zapisany):
 # 
 # Vasou ulohou bude v tomto zadani spocitat dlzku cesty cez nejake konkretne body za pouzitia algoritmu BellmanFord.
 # Pre blizsie informacie citajte nizsie v komentaroch.
 # 
 # Po ukonceni prace nahrajte vas kod do odovzdavarne:
 # IS -> Student -> IB002 -> Odevzdavarny -> PraktickyTest_skupina
 # Odovzdavajte len zdrojovy kod, NEODOVZDAVAJTE subory s nastaveniami pre IDE.
 # 
 # @author Henrich Lauko
 #

 #
 # Trieda path popisuje cestu grafom, je vyuzivana ako vstup pre algoritmus, ktory mate naimplementovat
 # Cesta je reprezentovana spojovanym zoznamom, kde kazdy vrchol predsatvuje jeden uzol zoznamu
 # Uzol obsahuje ukazatel na naslednik (next) a svoju hodnotu vrcholu (vertex)
 #

import sys  

class Path: 
    next = None
    vertex = 1
    
def addVertex(path, vertex):
		p = Path()
		p.vertex = vertex
		p.next = None
		path.next = p
    


#  Vytvori graf s v vrcholmi, bez hran, s nulami na diagonale
#  @param v vrcholov grafu
#  @return ukazatel na vytvoreny graf, tj. strukturu Graph.
def createGraph(n):
	matrix = [[sys.maxint]*n for i in range(n)]
	for i in range(n):
		matrix[i][i] = 0
	return matrix

#  Prida orientovanu hranu z u do v
#  @param matrix matica reprezentujuca graf ktory sa modifikuje
#  @param u pociatok hrany
#  @param v koniec hrany
#  @param w vaha hrany
#  Nespravi nic, ak indexy vrcholov su mimo matice
def addEdge(matrix, u, v, w):
    if u>=0 and v>=0 and u<len(matrix) and v<len(matrix):
        matrix[u][v]=w          
               

# Distance vrati vzdialenost medzi vrcholom from a to
# 
# v pripade ze najkratsia cesta neexistuje - ma zaporny cyklus, alebo vrcholy niesu spojene - vrati sys.maxint
# 
# @param matrix prahladavany graf
# @param f pociatok pocitania vzdialenosti
# @param t koniec hladanej cesty
# @return dlzku najkracsej cesty medzi from a to
# 
# Ak cesta neexistuje pole obsahuje sys.maxint	
#/
def BellmanFord(matrix, f, t):
	distance = {}
	for i in range(len(matrix)):
		distance[i] = sys.maxint
	distance[f] = 0

	for i in range(len(matrix)):
		for u in range(len(matrix)):
			for v in range(len(matrix)):
				if(matrix[u][v] == sys.maxint): pass
				if(distance[u] + matrix[u][v] < distance[v]):
					if(distance[u] == sys.maxint): pass
					distance[v] = distance[u] + matrix[u][v]

	for u in range(len(matrix)):
		for v in range(len(matrix)):
			if(matrix[u][v] == sys.maxint): pass
			if(distance[u] + matrix[u][v] < distance[v]):
				if(distance[u] == sys.maxint): pass
				return sys.maxint	
	return distance[t]
    
    
# Vasou ulohou bude v tomto zadani spravne aplikovat prilozeny algoritmus BellmanFord,
# ktory spocita najkratsiu vzdialenost 2 vrcholov v grafe.
# 
# Metoda pathLength dostava na vstupe pole vrcholov vasou ulohou bude spocitat dlzku najkratsej
# cesty ktora postupne prechadza vsetkymi vrcholmi. 
# 
# Ak path = 1,2,3 tak vysledna cesta bude dlzka cesty medzi vrcholom 1 a vrcholom 3 cez vrchol 2.
# 
# V pripade ze cesta obsahuje zaporny cyklus alebo neexistuje vratte sys.maxint	. 
# Ak je cesta prazdna algoritmus vrati None.
# Ak Cesta obsahuje jeden vrchol algoritmus vrati 0.
# 
# V ostatnych pripadoch vrati najkratsiu cestu ktora prejde v poradi vsetky vrcholi zo zoznamu. Nie je vylucene ze 
# sa cesta bude vracat cez niektore vrcholy.
def pathLength(matrix,path):
	length = 0	#vytvorime si premennu na pocitanie dlzky
	if path is None:	#overime ci cesta ktoru sme dostali existuje
		return sys.maxint	#ak nie tak vratime sys.maxint
	if path.next is None:	#overime ci cesta ktoru sme dostali obsahuje viac ako jeden vrchol
		return 0	#ak nie tak vratime 0
	while path.next is not None:	#prechadzame cestu (spojeny zoznam) a pripocitavame dlzku najkratsej cesty do length
		if BellmanFord(matrix, path.vertex, path.next.vertex) == sys.maxint:	#ak cesta neexistuje vratime sys.maxint
			return sys.maxint
		length = length + BellmanFord(matrix, path.vertex, path.next.vertex)	#pripocitavame
		path = path.next	#presuvame sa na dalsi vrchol
	return length	#vratime dlzku



##### nasledujuci kod sluzi na testovanie, NEMENTE jeho obsah

def getPathEnd(path):
	if path == None:
		return None
	while not path.next == None:
		path = path.next
	return path

def createPath(vertices):
	if vertices == None:
		return None
	path = Path()
	path.next = None
	path.vertex = vertices[0]
	for i in range(1, len(vertices)):
		newOne = Path()
		tmp = getPathEnd(path)
		tmp.next = newOne
		newOne.vertex = vertices[i]
		newOne.next = None
	return path
  
def test(g, p, expected):
	value = pathLength(g,p)
	if(value == expected):
		print "OK"
	else:
		print("Chyba vasa dlzka cesty je: "),
		print value,
		print " != ",
		print expected
        
    
    
g = createGraph(6)
addEdge(g,0, 1, 1)
addEdge(g,1, 2, 2)
addEdge(g,0, 2, 1)
addEdge(g,2, 3, 3)
addEdge(g,3, 4, 1)
addEdge(g,4, 0, 1)
#Test 1.
print("Test 1.: ")
test(g, None, sys.maxint)#prazdna cesta
#Test 2.
print("Test 2.: ")
p = createPath([1,2,3,4]) #cesta 1 -> 2 -> 3 -> 4
test(g,p, 6)
p = createPath([0,2,3])
test(g,p, 4)
p = createPath([0,1,5]) #nedosiahnutelny vrchol
test(g,p, sys.maxint)
#Test 3
print("Test 3.: ") 
p = createPath([0,1,2,1,0])
test(g,p, 16)
#Test 4.
print("Test 4.: ")
p = createPath([0,3,1,4,2])
test(g,p, 15)

#Test 5.
print("Test 5.: ")
g2 = createGraph(2)
addEdge(g2, 0, 1, -1)
addEdge(g2, 1, 0, -1)
p = createPath([0,1])
test(g2, p, sys.maxint)#zaporny cyklus v grafe
p = createPath([0,1,0])
test(g2, p, sys.maxint)#zaporny cyklus v grafe
#Test 6.
print("Test 6.: ")
g3 = createGraph(4)
addEdge(g3,0, 1, 1)
addEdge(g3,1, 2, 1)
addEdge(g3,2, 3, 1)
addEdge(g3,3, 0, 1)
p = createPath([1,1,2]) #prechod cez jeden vrchol dvakrat
test(g3, p, 1)
#Test 7.
print("Test 7.: ")
p = createPath([3,2,1,0])
test(g3, p, 9)
#Test 8.
print("Test 8.: ") 
p = createPath([3,3,2,2,1,1,0,0])
test(g3, p, 9)
#Test 9.
print("Test 9.: ")
g4 = createGraph(5)
addEdge(g4, 0, 1, 1)
addEdge(g4, 2, 3, 1)
addEdge(g4, 3, 4, 1)
p = createPath([0,1])
test(g4, p, 1)
p = createPath([1,0])
test(g4, p, sys.maxint) #cesta neexistuje
p = createPath([2,4])
test(g4, p, 2)
p = createPath([4,2])
test(g4, p, sys.maxint) #cesta neexistuje
p = createPath([0,4])
test(g4, p, sys.maxint) #cesta neexistuje
#Test 10.
print("Test 10.: ") 
addEdge(g4, 0, 1, -1)
addEdge(g4, 1, 2, -3)
p = createPath([0,1])
test(g4, p, -1)
p = createPath([0,2,4])
test(g4, p, -2)





