#!/usr/bin/python3
import sys


###########################
# Dotaz studenta:
#
#
###########################

# Chcete-li dostat odpoved, vlozte do nazvu souboru heslo KONTROLA.


# Tento program obsahuje velke mnozstvi chyb ruznych typu.
#
# Vasim ukolem je projit kod a opravit jej tak,
# abyste vsechny chyby odstranili.
#
# Testy nemodifikujte, jsou jen pro kontrolu a to, ze vsechny
# projdou neznamena, ze je vas kod bez chyby.
#
# Opravujte jen funkce, ktere maji v komentari TODO.


# TODO: opravit tuto funkci
def is_string_palindrom(string):
    """Testuje, zdali je zadany retezec (string) palindrom
    a to bez pouziti funkce reverse. Vraci True v pripade,
    ze je palindrom, jinak False.
    """
    if string is None:
        return False

    i = 0
    while i < len(string):
        if string[i] == string[len(string) -1 - i]:
            i+=1
            continue
        else:
            return False
    return True


class Node:
    """Trida Node slouzi pro reprezentaci objektu v jednosmerne
    spojovanem seznamu.

    Atributy:
        value   reprezentuje ulozenou hodnotu/objekt
        next    reference na nasledujici prvek v seznamu
    """
    def __init__(self):
        self.value = None
        self.next = None


class LinkedList:
    """Trida LinkedList reprezentuje spojovany seznam.

    Atributy:
        first   reference na prvni prvek seznamu
    """
    def __init__(self):
        self.first = None


# TODO: opravit tuto funkci
def insert(linked_list, value):
    """Funkce insert vklada na konec seznamu (linked_list) novy uzel
    s danou hodnotou (value). Vraci referenci na novy uzel seznamu.
    """
    n = Node()
    n.value = value

    tmp = linked_list.first

    if linked_list.first is None:
        linked_list.first = n
    else:
        while tmp.next:
            tmp = tmp.next
        tmp.next = n

    return n


# TODO: opravit tuto funkci
def delete_key(linked_list, key):
    """Funkce delete_key smaze prvni vyskyt klice (key) v seznamu
    (linked_list). Vrati False pokud klic nebyl nalezen, True jinak.
    """
    node = linked_list.first


    previous = None
    while node is not None and node.value != key:
        previous = node
        node = node.next

    if node is None:
        return False

    if previous is None :
        linked_list.first = node.next
    else:
        previous.next = node.next

    return True


# TODO: opravit tuto funkci
def multiply_numbers(bound, numbers):
    """Funkce vypocita soucin cisel v poli numbers, jejichz hodnota
    je z intervalu 1 az bound (vcetne). Pokud se v poli zadna takova
    cisla nenachazeji, vrati 1.

    Parametry:
        bound   horni hranice intervalu pro hodnotu cisel,
                ktera se zapocitavaji do vysledku
        numbers pole cisel k pocitani soucinu
    """
    array = [0 for i in range(bound)]
    for i in range(len(numbers)):
        array[numbers[i]] += 1
    val = 1
    for i in range(len(array)):
        for j in range(array[i]):
            val *= i
    return val


# TODO: opravit tuto funkci
def has_correct_parentheses(string):
    """Funkce otestuje, zdali zadany retezec obsahuje spravne
    ozavorkovani, tedy pred kazdou uzaviraci zavorkou musi byt prislusna
    oteviraci. Resi se pouze zavorky ( ). Vraci True v pripade spravneho
    ozavorkovani, jinak False.
    """
    opened = 0
    for i in range(len(string)):
        if string[i] == '(':
            opened += 1
        if string[i] == ')':
            opened -= 1
        if opened == 0:
            return True

    return False


# TODO: opravit tuto funkci
def sequence_sum(sequence):
    """Funkce secte "sumu" posloupnosti (sequence) a to tak, ze pokud je
    cislo vetsi nez predchazejici (sequence[n] > sequence[n-1]), tak ho
    pricte k "sume", pokud je sequence[n] < sequence[n-1], tak ho odecte
    a pokud je stejne, tak ho preskoci. Prvni cislo se nezapocita.
    """
    strange_sum = 0
    for i in range(len(sequence)):
        if sequence[i] > sequence[i-1]:
            strange_sum += sequence[i]
        if sequence[i] < sequence[i-1]:
            strange_sum -= sequence[i]
    return strange_sum


# TODO: opravit tuto funkci
def find_substring(string, substring):
    """Funkce hleda podretezec (substring) v retezci (string).
    Pokud se podretezec v retezci nachazi, vrati index prvniho vyskytu.
    Jinak vraci -1.
    """
    if len(substring) > len(string):
        return -1

    j = 1
    i = 1
    while i < len(string):
        if string[i] == substring[j]:
            if j == (len(substring) - 1):
                return i - j
            j += 1
    i += 1
    return -1


# Testy implmentace
def test_palindrom():
    print("Test 1: je \"abccba\" palindrom?")
    try:
        res = is_string_palindrom("abccba")
        if res:
            print("OK.")
        else:
            print("NOK, \"abccba\" je palindrom, ale program vraci 0.")
    except IndexError as e:
        print("NOK: pristup mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(e))

    print("Test 2: je \"abcba\" palindrom?")
    try:
        res = is_string_palindrom("abcba")
        if res:
            print("OK.")
        else:
            print("NOK, \"abcba\" je palindrom, ale program vraci 0.")
    except IndexError as e:
        print("NOK: pristup mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(e))

    print("Test 3: je \"abcabc\" palindrom?")
    try:
        res = is_string_palindrom("abcabc")
        if res:
            print("NOK, \"abcabc\" neni palindrom, ", end="")
            print("ale program vraci 1.")
        else:
            print("OK.")
    except IndexError as e:
        print("NOK: pristup mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(e))


def test_list():
    try:
        l1 = LinkedList()
        l1.first = None
        print("Test 4: vkladani 1. prvku do listu.")
        tmp1 = insert(l1, 1)
        if tmp1.value == 1 and l1.first is tmp1 and tmp1.next is None:
            print("OK.")
        else:
            print("NOK, vlozeni prvniho prvku neprobehlo v poradku, ", end="")
            print("zkontrolujte, zdali je spravne nastavena hodnota ", end="")
            print("a reference next.")
    except AttributeError as e:
        print("NOK: spatna prace s pameti.")
        print("Chybova hlaska Pythonu: {}".format(e))

    try:
        print("Test 5: vkladani 2. prvku do listu.")
        l2 = LinkedList()
        tmp21 = insert(l2, 1)
        tmp22 = insert(l2, 2)
        if (tmp22.value == 2 and l2.first is tmp21 and
                tmp22.next is None and tmp21.next is tmp22):
            print("OK.")
        else:
            print("NOK, vlozeni druheho prvku neprobehlo v poradku, ", end="")
            print(" zkontrolujte, zdali je spravne nastavena hodnota", end="")
            print(" a reference next.")
    except AttributeError as e:
        print("NOK: spatna prace s pameti.")
        print("Chybova hlaska Pythonu: {}".format(e))

    try:
        print("Test 6.1: odstraneni 2. prvku z listu.")
        l3 = LinkedList()
        tmp31 = insert(l3, 1)
        tmp32 = insert(l3, 2)
        if delete_key(l3, 2) and tmp31.next is None:
            print("OK.")
        else:
            print("NOK, neodstranili jste prvek, ", end="")
            print("muze to byt dano i spatnym vkladanim.")
    except AttributeError as e:
        print("NOK: spatna prace s pameti.")
        print("Chybova hlaska Pythonu: {}".format(e))

    try:
        print("Test 6.2: odstraneni prvku z prazdneho listu.")
        l3 = LinkedList()
        if delete_key(l3, 2):
            print("NOK, odstranili jste prvek z prazdneho listu ", end="")
            print("a nebo vratili True")
        else:
            print("OK.")
    except AttributeError as e:
        print("NOK: spatna prace s pameti.")
        print("Chybova hlaska Pythonu: {}".format(e))

    try:
        print("Test 6.3: odstraneni chybejiciho prvku z listu.")
        l3 = LinkedList()
        tmp31 = insert(l3, 1)
        tmp32 = insert(l3, 2)
        if delete_key(l3, 4):
            print("NOK, odstranili jste prvek, ktery v listu nebyl ", end="")
            print("a nebo vratili True")
        else:
            print("OK.")
    except AttributeError as e:
        print("NOK: spatna prace s pameti.")
        print("Chybova hlaska Pythonu: {}".format(e))


def test_multiply_numbers():
    print("Test 7: multiply_numbers(1, [1, 1, 1])")
    try:
        res = multiply_numbers(1, [1, 1, 1])
        if res is not 1:
            print("NOK: {} != 1".format(str(res)))
        else:
            print("OK.")
    except IndexError as e:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(e))

    print("Test 8: multiply_numbers(2, [3, 3, 3])")
    try:
        res = multiply_numbers(2, [3, 3, 3])
        if res is not 1:
            print("NOK: {} != 1".format(str(res)))
        else:
            print("OK.")
    except IndexError as e:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(e))

    print("Test 9: multiply_numbers(3, [1, 1, 2])")
    try:
        res = multiply_numbers(3, [1, 1, 2])
        if res is not 2:
            print("NOK: {} != @".format(str(res)))
        else:
            print("OK.")
    except IndexError as e:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(e))

    print("Test 10: multiply_numbers(3, [1, 4, 3])")
    try:
        res = multiply_numbers(3, [1, 4, 3])
        if res is not 3:
            print("NOK: {} != 3".format(str(res)))
        else:
            print("OK.")
    except IndexError as e:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(e))

    print("Test 11: multiply_numbers(4, [3, 3, 3, 2])")
    try:
        res = multiply_numbers(4, [3, 3, 3, 2])
        if res is not 54:
            print("NOK: " + str(res) + " != 54")
        else:
            print("OK.")
    except IndexError as e:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(e))

    print("Test 12: multiply_numbers(3, [3, 3, 4])")
    try:
        res = multiply_numbers(3, [3, 3, 4])
        if res is not 9:
            print("NOK: {} != 9".format(str(res)))
        else:
            print("OK.")
    except IndexError as e:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(e))


def test_brackets():
    print("Test 13: zavorkovani na \"()\"")
    try:
        if has_correct_parentheses("()"):
            print("OK.")
        else:
            print("NOK, \"()\" je spravne uzavorkovani a funkce vrati False")
    except IndexError as e:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(e))

    print("Test 14: zavorkovani na \")(\"")
    try:
        if has_correct_parentheses(")("):
            print("NOK, \")(\" neni spravne uzavorkovani a funkce vrati True")
        else:
            print("OK.")
    except IndexError as e:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(e))

    print("Test 15: zavorkovani na \"aaa\"")
    try:
        if has_correct_parentheses("aaa"):
            print("OK.")
        else:
            print("NOK, \"aaa\" je spravne uzavorkovani a funkce vrati False")
    except IndexError as e:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(e))

    print("Test 16: zavorkovani na \"((\"")
    try:
        if has_correct_parentheses("(("):
            print("NOK, \"((\" neni spravne uzavorkovani a funkce vrati True")
        else:
            print("OK.")
    except IndexError as e:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(e))


def test_sequence_sum():
    print("Test 17: sequence_sum([1, 2, 3])")
    try:
        res = sequence_sum([1, 2, 3])
        if res == 5:
            print("OK.")
        else:
            print("NOK, sequence_sum([1, 2, 3]) je 5 ", end="")
            print("a vam vyslo {}".format(str(res)))
    except IndexError as e:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(e))

    print("Test 18: sequence_sum([1, 2, 1])")
    try:
        res = sequence_sum([1, 2, 1])
        if res == 1:
            print("OK.")
        else:
            print("NOK, sequence_sum([1, 2, 1]) je 1 ", end="")
            print("a vam vyslo {}".format(str(res)))
    except IndexError as e:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(e))

    print("Test 18: sequence_sum([1,2,2])")
    try:
        res = sequence_sum([1, 2, 2])
        if res == 2:
            print("OK.")
        else:
            print("NOK, sequence_sum([1, 2, 2]) je 2 ", end="")
            print("a vam vyslo {}".format(str(res)))
    except IndexError as e:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(e))


def test_find():
    print("Test 19: je v \"abc\" podretezec \"abc\"?")
    try:
        res = find_substring("abc", "abc")
        if res == 0:
            print("OK.")
        else:
            print("NOK, podretezec je na pozici 0, ", end="")
            print("vy vracite {}".format(str(res)))
    except IndexError as e:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(e))

    print("Test 20: je v \"abc\" podretezec \"b\"?")
    try:
        res = find_substring("abc", "b")
        if res == 1:
            print("OK.")
        else:
            print("NOK, podretezec je na pozici 1, ", end="")
            print("vy vracite {}".format(str(res)))
    except IndexError as e:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(e))

    print("Test 21: je v \"abc\" podretezec \"abb\"?")
    try:
        res = find_substring("abc", "abb")
        if res == -1:
            print("OK.")
        else:
            print("NOK, podretezec zde neni, vy vracite {}".format(str(res)))
    except IndexError as e:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(e))

    print("Test 22: je v \"aaab\" podretezec \"aab\"?")
    try:
        res = find_substring("aaab", "aab")
        if res == 1:
            print("OK.")
        else:
            print("NOK, podretezec je na pozici 1, ", end="")
            print("vy vracite {}".format(str(res)))
    except IndexError as e:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(e))


if __name__ == '__main__':
    test_palindrom()
    test_list()
    test_multiply_numbers()
    test_brackets()
    test_sequence_sum()
    test_find()

    print("Testy netestuji vse. Pokud vam tedy prosly vsude na OK,")
    print("neznamena to, ze mate bezchybnou implementaci. To, ze")
    print("je nejaky test NOK ale znamena, ze mate neco spatne.")