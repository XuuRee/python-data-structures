# TESTS FOR COLOURABLE


# graph with no vertices
g0 = Graph(0)
print(str(colourable(g0)) + "... should be TRUE")

# graph with one vertice (no edge)
g1 = Graph(1)
g1.matrix[0][0] = True
print(str(colourable(g1)) + "... should be FALSE")

# graph with one vertice (and edge)
g2 = Graph(1)
print(str(colourable(g2)) + "... should be TRUE")

# two vertices 
g3 = Graph(2)
print(str(colourable(g3)) + "... should be TRUE")

g4 = Graph(2)
g4.matrix[0][0] = True
print(str(colourable(g4)) + "... should be FALSE")

g5 = Graph(2)
g5.matrix[0][1] = True
g5.matrix[1][0] = True
print(str(colourable(g5)) + "... should be TRUE")

g6 = Graph(2)
g6.matrix[1][1] = True
print(str(colourable(g6)) + "... should be FALSE")

# three vertices
g7 = Graph(3)
print(str(colourable(g7)) + "... should be TRUE")

g8 = Graph(3)
g8.matrix[0][1] = True
g8.matrix[1][0] = True
print(str(colourable(g8)) + "... should be TRUE")

g9 = Graph(3)
g9.matrix[0][1] = True
g9.matrix[1][0] = True
g9.matrix[2][2] = True
print(str(colourable(g9)) + "... should be FALSE")

g10 = Graph(3)
g10.matrix[0][1] = True
g10.matrix[1][0] = True
g10.matrix[0][2] = True
g10.matrix[2][0] = True
print(str(colourable(g10)) + "... should be TRUE")

g11 = Graph(3)
g11.matrix[0][1] = True
g11.matrix[1][0] = True
g11.matrix[0][2] = True
g11.matrix[2][0] = True
g11.matrix[2][2] = True
print(str(colourable(g11)) + "... should be FALSE")

g12 = Graph(3)
g12.matrix[0][1] = True
g12.matrix[1][0] = True
g12.matrix[0][2] = True
g12.matrix[2][0] = True
g12.matrix[2][1] = True
g12.matrix[1][2] = True
print(str(colourable(g12)) + "... should be FALSE")

g13 = Graph(3)
g13.matrix[0][2] = True
g13.matrix[1][2] = True
g13.matrix[2][0] = True
g13.matrix[2][1] = True
print(str(colourable(g13)) + "... should be TRUE")

g14 = Graph(4)
g14.matrix[0][1] = True
g14.matrix[0][2] = True
g14.matrix[1][3] = True
g14.matrix[2][3] = True
g14.matrix[1][0] = True
g14.matrix[2][0] = True
g14.matrix[3][1] = True
g14.matrix[3][2] = True
print(str(colourable(g14)) + "... should be TRUE")

#same graph as 14, but no backwards edges
g15 = Graph(4)
g15.matrix[0][1] = True
g15.matrix[0][2] = True
g15.matrix[1][3] = True
g15.matrix[2][3] = True
print(str(colourable(g15)) + "... should be TRUE")

g16 = Graph(6)
g16.matrix[0][1] = True
g16.matrix[0][2] = True
g16.matrix[1][3] = True
g16.matrix[2][3] = True
g16.matrix[1][0] = True
g16.matrix[2][0] = True
g16.matrix[3][1] = True
g16.matrix[3][2] = True
g16.matrix[4][5] = True
g16.matrix[5][4] = True
print(str(colourable(g16)) + "... should be TRUE")

g17 = Graph(4)
g17.matrix[0][1] = True
g17.matrix[1][0] = True
g17.matrix[1][3] = True
g17.matrix[3][1] = True
g17.matrix[2][3] = True
g17.matrix[3][2] = True
print(str(colourable(g17)) + "... should be TRUE")

g18 = Graph(5)
g18.matrix[4][3] = True
g18.matrix[4][1] = True
g18.matrix[1][0] = True
g18.matrix[0][2] = True
g18.matrix[2][4] = True
g18.matrix[4][2] = True
g18.matrix[2][0] = True
g18.matrix[0][1] = True
g18.matrix[1][4] = True
g18.matrix[3][4] = True
print(str(colourable(g18)) + "... should be TRUE")

g20 = Graph(4)
g20.matrix[3][0] = True
g20.matrix[0][1] = True
g20.matrix[0][2] = True
g20.matrix[0][3] = True
g20.matrix[1][0] = True
g20.matrix[2][0] = True
print(str(colourable(g20)) + "... should be TRUE")


# TEST FOR DEPENDENCY

g1 = Graph(0)
print(str(compute_dependencies(g1)) + " ... should be []")

g2 = Graph(1)
g2.matrix[0][0] = True
print(str(compute_dependencies(g2)) + " ... should be None")

g3 = Graph(3)
g3.matrix[0][1] = True
g3.matrix[2][0] = True
g3.matrix[2][1] = True
print(str(compute_dependencies(g3)) + " ... [2, 0, 1]")

g4 = Graph(3)
g4.matrix[1][2] = True
print(str(compute_dependencies(g4)) + " ... [0, 1, 2], [1, 0, 2], [1, 2, 0]")

g5 = Graph(4)
g5.matrix[0][1] = True
g5.matrix[2][3] = True
print(str(compute_dependencies(g5)) + " ... [2, 3, 0, 1], [0, 2, 1, 3]")

g6 = Graph(3)
g6.matrix[0][1] = True
g6.matrix[1][2] = True
g6.matrix[2][0] = True
print(str(compute_dependencies(g6)) + " ... None")
