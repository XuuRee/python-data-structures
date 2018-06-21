#!/usr/bin/python3


# IB002 Domaci uloha 1.
#
# Vasi ulohou v tomto priklade je modifikovat jiz existujici strukturu
# obousmerne zretezeneho linearniho seznamu.
#
# Obousmerne zretezeny seznam ma atribut first, ktery ukazuje na zacatek
# seznamu, a atribut last, ktery ukazuje na konec seznamu.
#
# Kazdy uzel v seznamu ma tri atributy (value, next a prev). Vlastni seznam
# s hodnotami a, b, c, d, e, f vypada bezne takto (v nakresu vynechavame
# atribut first ukazujici na a a atribut last ukazujici na f):
#       ___   ___   ___   ___   ___
#      /   \ /   \ /   \ /   \ /   \
#     a <-- b <-- c <-- d <-- e <-- f
#
# kde obloucky nad pismeny reprezentuji dopredne sipky (napr. a --> b),
# tedy atributy next.
#
# Nas modifikovany StrangeList pouziva pro reprezentaci stejne promenne,
# pouze atributy ukazuji jinam. Atributy next budou ukazovat ob jeden
# uzel, atributy prev zustanou zachovany. Po prevedeni predchoziho
# seznamu na StrangeList vznikne takovyto seznam (opet vynechavame
# atributy first a last):
#       _________   _________
#      /         \ /         \
#     a <-- b <-- c <-- d <-- e <-- f
#            \_________/ \_________/
#
# StrangeList take obsahuje atribut first, ktery ukazuje na jeho zacatek,
# a atribut last, ktery ukazuje na jeho konec, v tomto pripade:
# first - a, last - f.


# Ukol 1.
# Definujte datovou strukturu StrangeList.
# Muzete se inspirovat definici ze zakladniho domaciho ukolu.

class Node:
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None


class StrangeList:
    def __init__(self):
        self.first = None
        self.last = None


# Ukol 2.
# Implementujte funkci list_to_strange_list, ktera z obousmerne
# zretezeneho seznamu vytvori nas StrangeList, tj. upravi atributy next.
# Reprezentaci obousmerne zretezeneho seznamu muzete prevzit ze
# zakladniho domaciho ukolu.

def list_to_strange_list(linkedList):
    """
    vstup: 'linkedList' korektni seznam typu LinkedList
    vystup: stejny seznam s upravenymi atributy next, aby to byl koretni
            StrangeList
    casova slozitost: O(n), kde 'n' je pocet prvku seznamu 'linkedList'
    """
    node = linkedList.first
    while node != None and node.next != None:
        next_node = node.next
        node.next = next_node.next
        node = next_node
    return linkedList


# Ukol 3.
# Implementujte funkci check_strange_list, ktera zkontroluje, ze atributy
# first a last jsou nastaveny spravne. Korektnost next a prev muzete
# predpokladat.

def check_strange_list(strangeList):
    """
    vstup: 'strangeList' typu StrangeList s korektnimi atributy next a prev
    vystup: True, pokud jsou v 'strangeList' atributy first a last nastaveny
            korektne
            False, jinak
    casova slozitost: O(1)
    """
    first_node = strangeList.first
    last_node = strangeList.last
    if first_node is None and last_node is None:
        return True
    if first_node is None and last_node is not None:
        return False
    if first_node is not None and last_node is None:
        return False
    if first_node.prev != None:
        return False
    if last_node.next != None:
        return False
    if last_node.prev != None:
        if last_node.prev.next != None:
            return False
    return True
