print()
print("-- RELATIONS ------------------------------")
print()

print("GRAPH 1:\n0 0 0\n0 0 0\n0 0 0")
g1 = Graph(3)
print("REFLEXIVITA:     " + str(is_reflexive(g1)) + " -> spravna odpoved: False")
print("SYMETRIE:        " + str(is_symmetric(g1)) + " -> spravna odpoved: True")
print("ANTISYMETRIE:    " + str(is_antisymmetric(g1)) + " -> spravna odpoved: True")
print("TRANZITIVITA:    " + str(is_transitive(g1)) + " -> spravna odpoved: True")

print("-------------------------------------------")

print("GRAPH 2:\n1 0 0\n0 1 0\n0 0 1")
g2 = Graph(3)
g2.matrix[0][0] = True
g2.matrix[1][1] = True
g2.matrix[2][2] = True
print("REFLEXIVITA:     " + str(is_reflexive(g2)) + " -> spravna odpoved: True")
print("SYMETRIE:        " + str(is_symmetric(g2)) + " -> spravna odpoved: True")
print("ANTISYMETRIE:    " + str(is_antisymmetric(g2)) + " -> spravna odpoved: False")
print("TRANZITIVITA:    " + str(is_transitive(g2)) + " -> spravna odpoved: True")

print("- GOOD GRAPHS -----------------------------")

print("GRAPH 3:\n0 0 0\n0 1 0\n0 1 1")
g3 = Graph(3)
g3.matrix[1][1] = True
g3.matrix[2][1] = True
g3.matrix[2][2] = True
print("REFLEXIVITA:     " + str(is_reflexive(g3)) + " -> spravna odpoved: False")
print("SYMETRIE:        " + str(is_symmetric(g3)) + " -> spravna odpoved: False")
print("ANTISYMETRIE:    " + str(is_antisymmetric(g3)) + " -> spravna odpoved: True")
print("TRANZITIVITA:    " + str(is_transitive(g3)) + " -> spravna odpoved: True")

print("-------------------------------------------")

print("GRAPH 4:\n0 1 1\n0 1 1\n0 0 1")
g4 = Graph(3)
g4.matrix[0][1] = True
g4.matrix[0][2] = True
g4.matrix[1][1] = True
g4.matrix[1][2] = True
g4.matrix[2][2] = True
print("REFLEXIVITA:     " + str(is_reflexive(g4)) + " -> spravna odpoved: False")
print("SYMETRIE:        " + str(is_symmetric(g4)) + " -> spravna odpoved: False")
print("ANTISYMETRIE:    " + str(is_antisymmetric(g4)) + " -> spravna odpoved: True")
print("TRANZITIVITA:    " + str(is_transitive(g4)) + " -> spravna odpoved: True")

print("-------------------------------------------")

print("GRAPH 5:\n1 0 0\n0 0 0\n1 0 0")
g5 = Graph(3)
g5.matrix[0][0] = True
g5.matrix[2][0] = True
print("REFLEXIVITA:     " + str(is_reflexive(g5)) + " -> spravna odpoved: False")
print("SYMETRIE:        " + str(is_symmetric(g5)) + " -> spravna odpoved: False")
print("ANTISYMETRIE:    " + str(is_antisymmetric(g5)) + " -> spravna odpoved: True")
print("TRANZITIVITA:    " + str(is_transitive(g5)) + " -> spravna odpoved: True")

print("-------------------------------------------")

print("GRAPH 6:\n1 0 0\n1 1 0\n0 1 1")
g6 = Graph(3)
g6.matrix[0][0] = True
g6.matrix[1][0] = True
g6.matrix[1][1] = True
g6.matrix[2][1] = True
g6.matrix[2][2] = True
print("REFLEXIVITA:     " + str(is_reflexive(g6)) + " -> spravna odpoved: True")
print("SYMETRIE:        " + str(is_symmetric(g6)) + " -> spravna odpoved: False")
print("ANTISYMETRIE:    " + str(is_antisymmetric(g6)) + " -> spravna odpoved: True")
print("TRANZITIVITA:    " + str(is_transitive(g6)) + " -> spravna odpoved: False")

print()
print("- TRANSITIVE CLOSURE -------------------------")
print()

print("GRAPH 7:\n1 0 0\n1 1 0\n0 1 1")
g7 = Graph(3)
g7.matrix[0][0] = True
g7.matrix[1][0] = True
g7.matrix[1][1] = True
g7.matrix[2][1] = True
g7.matrix[2][2] = True
print("TRANZITIVITA:    " + str(is_transitive(g7)) + " -> spravna odpoved: False")
transitive_closure(g7)
print(str(g7.matrix))
print("TRANZITIVITA:    " + str(is_transitive(g7)) + " -> spravna odpoved: True")
