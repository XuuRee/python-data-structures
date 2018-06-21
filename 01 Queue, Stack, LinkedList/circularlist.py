#!/usr/bin/env python3


# IB002 Domaci uloha 2.
#
# Jednosmerne spojovany seznam znate z prednasky - jde o zretezeny seznam
# uzlu (Node), kde kazdy uzel ukazuje na sveho naslednika. V tomto prikladu
# nemame first a last, seznam je zadany "prvnim" ze svych uzlu.
#
# Tato uloha pracuje se dvema typy jednosmerne spojovanych seznamu:
# Linearni seznam - kde posledni prvek seznamu ukazuje na None.
# Kruhovy seznam - kde posledni prvek seznamu ukazuje zpet na prvni prvek.
#
# Pro vsechny funkce muzete predpokladat, ze seznam na vstupu je linearni,
# nebo kruhovy, tj. nemusite napriklad osetrovat situaci, kdy naslednikem
# "posledniho" v seznamu je "druhy".
#
# Do definice tridy Node nijak nezasahujte.

class Node:
    """Trida Node reprezentujici prvek ve spojovanem seznamu

    Atributy:
        key        klic daneho uzlu (cele cislo)
        next       odkaz na dalsi prvek seznamu
        opposite   odkaz na protejsi prvek seznamu, viz ukol 3.
    """

    def __init__(self):
        self.key = 0
        self.next = None
        self.opposite = None


# Ukol 1.
# Implementujte funkci is_circular, ktera dostane prvni uzel seznamu
# a otestuje, zda je zadany zretezeny seznam kruhovy.
# Prazdny seznam neni kruhovy.

def is_circular(node):
    """
    vstup: 'node' prvni uzel seznamu, ktery je linearni, nebo kruhovy
    vystup: True, pokud je seznam z uzlu 'node' kruhovy
            False, jinak
    casova slozitost: O(n), kde 'n' je pocet prvku seznamu
    """
    if node is None:
        return False
    first_node = node
    while node.next:
        node = node.next
        if first_node is node:
            return True
    return False


# Ukol 2.
# Implementujte funkci get_length, ktera vrati delku (tj. pocet ruznych uzlu)
# (linearniho nebo kruhoveho) zretezeneho seznamu zacinajiciho v zadanem uzlu.
# Pokud je seznam prazdny (None), vrati 0.

def get_length(node):
    """
    vstup: 'node' prvni uzel seznamu, ktery je linearni, nebo kruhovy
    vystup: pocet prvku v zadanem seznamu
    casova slozitost: O(n), kde 'n' je pocet prvku seznamu
    """
    if node is None:
        return 0
    length = 1
    first_node = node
    while node.next:
        node = node.next
        if first_node is node:
            return length
        length += 1
    return length


# Ukol 3.
# Implementujte funkci calculate_opposites, ktera korektne naplni atributy
# "opposite" v uzlech kruhoveho seznamu sude delky. Tj. pro kruhove seznamy
# delky 2n naplni u kazdeho uzlu atribut opposite uzlem, ktery je o n kroku
# dale (tedy v kruhu je to uzel "naproti").
#
# Napriklad v kruhovem seznamu 1 -> 2 -> 3 -> 4 (-> 1) je opposite
# uzlu 1 uzel 3, uzlu 2 uzel 4, uzlu 3 uzel 1 a uzlu 4 uzel 2.
#
# Pokud vstupni seznam neni kruhovy nebo ma lichou delku, tak funkce
# calculate_opposites seznam neupravuje.
#
# Pozor na casovou a prostorovou slozitost vaseho algoritmu!

def identify_step(node, length):
    step = node
    while length:
        step = step.next
        length -= 1
    return step


def calculate_opposites(node):
    """
    vstup: 'node' prvni uzel seznamu, ktery je linearni, nebo kruhovy
    vystup: nic, kokretne doplni atribut opposite pro seznam sude delky
    casova slozitost: O(n), kde 'n' je pocet prvku seznamu
    """
    if not is_circular(node):
        return
    length = get_length(node)
    if length % 2 != 0:
        return
    length = length // 2
    if length == 1:
        node.opposite = node.next
        node.next.opposite = node
        return
    step = identify_step(node, length)
    length = length * 2
    while length:
        node.opposite = step
        node, step = node.next, step.next
        length -= 1

"""
node_a = Node()
node_a.key = 1
node_b = Node()
node_b.key = 2
node_c = Node()
node_c.key = 3
node_d = Node()
node_d.key = 4
node_e = Node()
node_e.key = 5
node_f = Node()
node_f.key = 6
node_g = Node()
node_g.key = 7
node_h = Node()
node_h.key = 8
node_a.next = node_b
node_b.next = node_c
node_c.next = node_d
node_d.next = node_e
node_e.next = node_f
node_f.next = node_g
node_g.next = node_h
node_h.next = node_a
calculate_opposites(node_a)
print("1 -> {}".format(node_a.opposite.key))
print("2 -> {}".format(node_b.opposite.key))
print("3 -> {}".format(node_c.opposite.key))
print("4 -> {}".format(node_d.opposite.key))
print("5 -> {}".format(node_e.opposite.key))
print("6 -> {}".format(node_f.opposite.key))
print("7 -> {}".format(node_g.opposite.key))
print("8 -> {}".format(node_h.opposite.key))
"""