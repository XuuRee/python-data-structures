#!/usr/bin/python3

# UCO: 433439
# Povolene knihovny: copy, math, collections
from collections import deque

# --- Implementacni test 1. 6. 2018: Automaty ---
#
# V tomto testu budeme pracovat s datovou strukturou DFA. Podrobnosti o teto
# datove strukture jsou popsany v textove verzi zadani, kterou jste obdrzeli na
# zacatku zkousky. Jedna se o klasicky (deterministicky) konecny automat, ktery
# zobecnuje Trie ze zadani specialniho domaciho ukolu.


class DFA:
    """Trida DFA slouzi k reprezentaci konecneho automatu.

    Atributy:
        size        pocet uzlu
        accepting   je uzel akceptujici?
        table       matice hran

    2D matice 'table' je velikosti 'size' krat 26.  Kazdy radek odpovida
    jednomu uzlu, kazdy sloupec jednomu pismenu anglicke abecedy.

    Pokud na pozici 'table[s][i]' je hodnota 't', pak z 's' existuje hrana do
    't' pod pismenem s hodnotou 'i'.

    Pokud na pozici 'table[s][i]' je hodnota 'None', pak z 's' hrana pod
    pismenem s hodnotou 'i' neexistuje.

    Zaciname vzdy v prvnim uzlu (tj. uzlu 0). Muzete predpokladat, ze
    automat ma vzdy alespon jeden uzel (tedy plati 'size > 0').
    """

    def __init__(self, size):
        self.size = size
        self.accepting = [False] * size
        self.table = [[None] * 26 for row in range(size)]

# Priklad: viz papirove zadani.

# Pripomenuti prace s dvourozmernymi maticemi a dvojicemi:
# - indexovani 2D matice:
#     matrix[y][x]      # prvni souradnice je radek, druha sloupec
# - vytvoreni 2D matice obsahujici same hodnoty False
#     [[False] * pocet_sloupcu for y in range(pocet_radku)]
#   nebo
#     [[False for x in range(pocet_sloupcu)] for y in range(pocet_radku)]
# - ulozeni dvojice hodnot do promenne
#     d = (x, y)        # zavorky je mozno vynechat
# - rozbaleni dvojice (predpokladame, ze x obsahuje dvojici hodnot)
#     (x, y) = d        # zavorky je mozno vynechat
#   (misto d muze byt i volani funkce f(), indexovani seznamu s[i] apod.)
# - vytvoreni seznamu obsahujiciho dvojici
#     s = [(x, y)]      # zde jsou zavorky nutne
# - pridani dvojice na konec seznamu
#     s.append((x, y))  # zde jsou zdvojene zavorky nutne!


# Nasledujici pomocnou funkci muzete vyuzit pro prevod malych pismen anglicke
# abecedy na cislo mezi 0 a 25 vcetne.

def get_id(x):
    """Pro zadany znak v rozsahu 'a' - 'z' vrati hodnotu 0 - 25."""
    return ord(x) - ord('a')


# Ukol 1. (15 bodu)
# Implementujte funkci accepts, ktera zjisti, zda pro dane
# vstupni slovo 'word' skonci automat v akceptujicim uzlu.
#
# Priklad: viz uvodni priklad automatu v papirovem zadani.
#

def accepts(fa, word):
    """
    vstup:  'fa' korektni objekt typu DFA
    vystup: True pokud automat fa akceptuje zadane slovo 'word'
            False jinak
    casova slozitost: O(d), kde d je delka slova 'word'.
    """
    node = 0
    for character in word:
        node = fa.table[node][get_id(character)]
        if node is None:
            return False
    if not fa.accepting[node]:
        return False
    return True


# Ukol 2. (20 bodu)
# Implementujte funkci unreachable, vracejici seznam uzlu, ktere nelze
# dosahnout z pocatecniho uzlu '0'. Na poradi uzlu ve vracenem seznamu
# nezalezi.
#
# Priklad: viz papirove zadani.

def bfs(fa, root):
    visited = [False] * fa.size
    visited[root], queue = True, deque([root])
    while queue:
        vertex = queue.popleft()
        for j in range(26):
            node = fa.table[vertex][j]
            if node is not None and not visited[node]:
                visited[node] = True
                queue.append(node)
    return visited


def unreachable(fa):
    """
    vstup:  'fa' korektni objekt typu DFA
    vystup: seznam uzlu, ktere jsou nedosazitelne
            Na poradi nezalezi.
    casova slozitost: O(n), kde n je pocet uzlu automatu.
    """
    result = []
    visited = bfs(fa, 0)
    for i in range(len(visited)):
        if not visited[i]:
            result.append(i)
    return result


# Ukol 3. (30 bodu)
# Implementuje funkci bi_reachable, ktera zjisti, zda dany uzel je dosazitelny
# z pocatecniho uzlu alespon dvema ruznymi cestami. Muzete predpokladat, ze
# vsechny uzly jsou dosazitelne z pocatecniho uzlu '0' a do uzlu '0' nevede
# zadna hrana.

# Napoveda: Naleznete libovolnou cestu do zadaneho uzlu. Jelikoz jsou vsechny
# uzly dosazitelne, dve ruzne cesty existuji, prave kdyz na nalezene ceste
# ma alespon jeden uzel vstupni stupen vyssi nez jedna.
#
# Priklad: viz papirove zadani.

class Path:

    def __init__(self):
        self.exist = False


def dfs(fa, vertex, state, visited, path):
    visited[vertex] = True
    if vertex == state:
        return
    for i in range(26):
        node = fa.table[vertex][i]
        if node is not None:
            if visited[node]:
                path.exist = True
            else:
                dfs(fa, node, state, visited, path)


def bi_reachable(fa, state):
    """
    vstup:  'fa' korektni objekt typu DFA
            'state' hledany uzel
            Navic muzete predpokladat, ze vsechny uzly jsou dosazitelne z
            pocatecniho uzlu '0' a do uzlu '0' nevede zadna hrana.
    vystup: True, pokud je uzel 'state' dosazitelny z '0' vice nez jednou
            cestou; False jinak.

    casova slozitost: O(n), kde n je pocet uzlu automatu.
    """
    path = Path()
    visited = [False] * fa.size
    dfs(fa, 0, state, visited, path)
    return path.exist


# Ukol 4. (15 + 20 bodu)
# Implementujte funkci shortest_cycle, ktera najde nejaky cyklus minimalni
# delky v zadanem automatu dosazitelny z '0', a jako vystup vrati delku a
# posloupnost uzlu tohoto cyklu. Pokud neexistuje zadny dosazitelny cyklus,
# vraci None.
#
# Napoveda: Vzhledem k tomu, ze pocet hran je v O(size), mate (pri spravne
# implementaci) dost casu spocitat si pro kazdy uzel 'u' nejkratsi cyklus
# obsahujici 'u'.
#
# Hodnoceni: 15 bodu za vraceni spravne delky cyklu, 20 bodu za vypsani spravne
# posloupnosti vrcholu.
#
# Priklad: viz papirove zadani.

class LCycles:

    def __init__(self):
        self.list = []


def bfs_shortest_cycle(fa, root, state, l_cycles):
    queue, path = deque([(0, root)]), [root]
    while queue:
        vertex = queue.popleft()
        for j in range(26):
            node = fa.table[vertex[1]][j]
            if node is not None:
                if node == state:
                    l_cycles.list.append((vertex[0] + 1, path))
                    return
                queue.append((vertex[0] + 1, node))
                path.append(node)


def dfs_shortest_cycle(fa, vertex, visited, l_cycles):
    visited[vertex] = True
    for i in range(26):
        node = fa.table[vertex][i]
        if node is not None:
            if visited[node]:
                bfs_shortest_cycle(fa, node, node, l_cycles)
            else:
                dfs_shortest_cycle(fa, node, visited, l_cycles)


def shortest_cycle(fa):
    """
    vstup:  'fa' korektni objekt typu DFA
    vystup: dvojice (n, list), kde 'n' je delka (pocet hran) cyklu minimalni
            delky a 'list' je seznam [s1, s2, s3, ..., sn] uzlu takovy,
            ze s1 -> s2 -> s3 -> ... -> sn -> s1 je nejaky cyklus delky n
            Pismena nad hranami nas nezajimaji.
            Pokud v grafu existuje vice cyklu minimalni delky, je mozne vratit
            libovolny z nich.
            Pokud zadny cyklus v grafu neexistuje, vraci None.

    casova slozitost: O(n^2), kde n je pocet uzlu automatu.
    """
    visited, l_cycles = [False] * fa.size, LCycles()
    dfs_shortest_cycle(fa, 0, visited, l_cycles)
    return None  # TODO


"""
Soubory .dot z testu vykreslite napr. na http://www.webgraphviz.com/.
"""

########################################################################
#               Nasleduje kod testu, NEMODIFIKUJTE JEJ                 #
########################################################################


def print_fa(fa, fileName):
    """
    Zde mate k dispozici funkci `print_fa`, ktera vam z `fa` na vstupu
    vygeneruje do souboru `fileName` reprezentaci automatu pro graphviz.
    Graphviz je nastroj, ktery vam umozni vizualizaci datovych struktur,
    coz se hodi predevsim pro ladeni.
    Pro zobrazeni graphvizu muzete vyuzit:
    http://www.webgraphviz.com/
    """

    def makeGraphviz(fa, f):
        n = fa.size
        for s in range(n):
            if fa.accepting[s]:
                style = 'shape="doublecircle"'
            else:
                style = ""
            f.write('{} [label="{}"{}]\n'.format(s, s, style))

        for s in range(n):
            for i, t in enumerate(fa.table[s]):
                if t is not None:
                    char = chr(i + ord('a'))
                    f.write('{} -> {} [label=" {}"]\n'.format(s, t, char))

    with open(fileName, 'w') as f:
        f.write("digraph {\n")
        f.write('node [shape="circle",ordering="out"]\n')
        makeGraphviz(fa, f)
        f.write("}\n")


class Ib002TestCase:
    from copy import deepcopy as _copy

    def __init__(self, size, code, accepts, rejects, unreachable, length,
                 bireach_list):
        self.fa = \
            Ib002TestCase._decode(size, code)
        self.accepts = accepts
        self.rejects = rejects
        self.unreachable = unreachable
        self.length = length
        self.bireach_list = bireach_list

    @staticmethod
    def _decode(size, code):
        fa = DFA(size)
        for s in range(size):
            row = code[s]
            fa.accepting[s] = row[0]
            for i in range(1, len(row), 2):
                fa.table[s][get_id(row[i])] = row[i + 1]

        return fa

    def clone_fa(self):
        return Ib002TestCase._copy(self.fa)


IB002_CASES = [
    Ib002TestCase(3,  # basic test for accepts
                  [[True, 'a', 1, 'b', 2, 'c', 0], [False, 'a', 1, 'b', 2],
                   [True, 'a', 1, 'b', 2]],
                  ['c', 'cc', 'ccc', 'b', 'ab', 'abb', 'abab', 'bb', 'cbb',
                   ''],
                  ['a', 'aba', 'ca', 'caa', 'baba', 'bzz', 'zz'], (), 1,
                  [(0, True), (1, True), (2, True)]),
    Ib002TestCase(8,  # basic test for unreachable
                  [[False, 'e', 1], [False, 'a', 2], [False, 'b', 3],
                   [True, 'c', 1], [False, 'a', 0, 'b', 1, 'c', 5],
                   [False, 'd', 4], [False, 'x', 7], [True]],
                  ['eab', 'eabcab'], ['x', 'dbab', 'bab', ''],
                  [4, 5, 6, 7], 3, ()),
    Ib002TestCase(5,  # basic test for bi_reachable
                  [[False, 'x', 4, 'y', 1], [False, 'x', 2],
                   [False, 'z', 3], [True], [False, 'x', 4, 'y', 2]],
                  ['yxz', 'xyz', 'xxyz'], ['x', 'z', 'xz', 'yz'], (), 1,
                  [(0, False), (1, False), (2, True), (3, True),
                   (4, True)]),
    Ib002TestCase(4,  # basic test for shortest cycle
                  [[False, 'a', 1], [True, 'a', 2], [False, 'a', 3],
                   [False, 'a', 0, 'b', 1]],
                  ['a', 'aaab', 'aaaaa'], ['aa', 'aaa', 'aaba', 'b', 'ba'],
                  (), 3, [(0, True), (1, True), (2, True), (3, True)]),
    Ib002TestCase(5,
                  [[False, 'x', 1, 'y', 4], [False, 'x', 2],
                   [False, 'z', 3], [True], [False, 'x', 4, 'y', 2]],
                  ['xxz', 'yyz', 'yxyz'], ['x', 'z', 'xz', 'yz'], (), 1,
                  [(0, False), (1, False), (2, True), (3, True),
                   (4, True)]),
    Ib002TestCase(3,
                  [[True, 'a', 0, 'b', 1], [False, 'a', 1, 'b', 0],
                   [False, 'a', 1, 'b', 1]],
                  ['bb', 'a'], ['ba', 'baa', 'b'], [2], 1,
                  [(0, True), (1, True)]),
    Ib002TestCase(3, [[True, 'a', 1], [False, 'a', 2], [False, 'b', 0]],
                  ['aab'], ['ba', 'baa', 'b'], [], 3,
                  [(0, False), (1, False), (2, False)]),
    Ib002TestCase(3, [[False, 'a', 1, 'b', 2], [True], [False, 'c', 1]],
                  ['a', 'bc'], ['', 'aa', 'bb', 'ca'], [], None,
                  [(0, False), (1, True), (2, False)]),
    Ib002TestCase(5,
                  [[True, 'a', 1, 'b', 2], [True], [False, 'c', 1],
                   [True, 'a', 3], [False]],
                  ['', 'a', 'bc'], ['aa', 'bb', 'ca'], [3, 4], None,
                  [(0, False), (1, True), (2, False)]),
    Ib002TestCase(1, [[True, 'a', 0]], ['', 'a', 'aa', 'aaa'],
                  ['b', 'bc', 'ab'], [], 1, ()),
    Ib002TestCase(1, [[True]], [''], ['a', 'b'], [], None, ()),
    Ib002TestCase(1, [[False]], (), ['', 'a', 'b'], (), None, []),
    Ib002TestCase(2, [[False, 'a', 1, 'b', 1], [True, 'a', 1]],
                  ['a', 'b', 'aa', 'ba'], ['bb', 'ab'], [], 1,
                  [(1, True)]),
    Ib002TestCase(2, [[False, 'a', 1, 'z', 1], [False]], (),
                  ['a', '', 'z', 'az'], [], None, [(1, True)]),
    Ib002TestCase(5,
                  [[False, 'a', 1], [False, 'a', 2], [True, 'a', 0],
                   [False, 'a', 4], [False, 'a', 3]],
                  ['aa'], ['zz'], [3, 4], 3, ()),
]


def ib002_output_fa(fa, name):
    file_name = "Er_{}_input.dot".format(name)
    print_fa(fa, file_name)
    print("Vstupni automat je v souboru {}".format(file_name))


def ib002_test_report(ok, basic):
    if ok:
        print("[ OK ] {} prosel.".format("Zakladni test" if basic else "Test"))
    elif basic:
        print("[FAIL] Zakladni test neprosel.",
              "Tato cast bude automaticky hodnocena 0 body.")
    else:
        print("[FAIL] Test neprosel.")


def ib002_test_header(msg, basic):
    print("\n*** {} {}:".format("Zakladni test" if basic else "Test", msg))


def ib002_test_accepts(case):
    def test_one(fa, cases, correct):
        for w in cases:
            result = accepts(fa, w)
            if (fa.table != case.fa.table) or \
               (fa.accepting != case.fa.accepting):
                print("Chyba! Doslo k modifikaci vstupniho automatu.")
                return False
            if result != correct:
                print("Hledane slovo: {}".format(w))
                print("Spatna odpoved {}, spravna mela byt {}."
                      .format(result, correct))
                ib002_output_fa(fa, 'accepts')
                return False
        return True

    fa = case.clone_fa()

    if not test_one(fa, case.accepts, True):
        return False

    if not test_one(fa, case.rejects, False):
        return False

    return True


def ib002_test_unreachable(case):
    fa = case.clone_fa()

    result = unreachable(fa)
    if (fa.table != case.fa.table) or (fa.accepting != case.fa.accepting):
        print("Chyba! Doslo k modifikaci vstupniho automatu.")
        return False

    correct = case.unreachable
    missing = set(correct) - set(result)
    extra = set(result) - set(correct)

    if missing:
        print("Vraceny seznam: {}".format(result))
        print("Uzel {} chybi, i kdyz je nedosazitelny."
              .format(missing.pop()))
        ib002_output_fa(fa, 'unreachable')
        return False

    if extra:
        print("Vraceny seznam: {}".format(result))
        print("Uzel {} vsak neni nedosazitelny."
              .format(extra.pop()))
        ib002_output_fa(fa, 'unreachable')
        return False

    return True


def ib002_test_shortest_cycle_length(case):
    fa = case.clone_fa()

    result = shortest_cycle(fa)
    if (fa.table != case.fa.table) or (fa.accepting != case.fa.accepting):
        print("Chyba! Doslo k modifikaci vstupniho automatu.")
        return False

    correct = case.length

    if result is None:
        if result != correct:
            print("Spatna odpoved {}, nejkratsi cyklus ma delku {}."
                  .format(result, correct))
            ib002_output_fa(fa, 'shortest')
            return False
        else:
            return True

    # result is a pair
    (length, cycle) = result

    # check the length
    if length != correct:
        print("Spatna odpoved {}, nejkratsi cyklus ma delku {}."
              .format(length, correct))
        ib002_output_fa(fa, 'shortest')
        return False

    return True


# testy se na delku se spousti dvakrat nenadelam nic
def ib002_test_shortest_cycle_nodes(case):
    fa = case.clone_fa()

    result = shortest_cycle(fa)
    if (fa.table != case.fa.table) or (fa.accepting != case.fa.accepting):
        print("Chyba! Doslo k modifikaci vstupniho automatu.")
        return False

    correct = case.length

    if result is None:
        if result != correct:
            print("Spatna odpoved {}, nejkratsi cyklus ma delku {}."
                  .format(result, correct))
            ib002_output_fa(fa, 'shortestC')
            return False
        else:
            return True

    # result is a pair
    (length, cycle) = result

    # check the length
    if length != correct:
        print("Spatna odpoved {}, nejkratsi cyklus ma delku {}."
              .format(length, correct))
        ib002_output_fa(fa, 'shortestC')
        return False

    # check if this cycle exists
    if len(cycle) != length:
        print("Seznam {} nema delku {}."
              .format(cycle, length))
        return False

    s = cycle[-1]
    try:
        for i in range(0, len(cycle)):
            if cycle[i] is None:
                raise ValueError()
            fa.table[s].index(cycle[i])  # raises ValueError
            s = cycle[i]
    except ValueError:
        print("Vraceny seznam {} neni cyklus.".format(cycle))
        ib002_output_fa(fa, 'shortestC')
        return False

    return True


def ib002_test_bi_reachable(case):
    # skip tests with unreachable states
    if case.unreachable != []:
        return True

    fa = case.clone_fa()

    # skip tests when 0 has an incoming edge
    for s in range(fa.size):
        for j in range(26):
            if fa.table[s][j] == 0:
                return True

    for (state, correct) in case.bireach_list:
        result = bi_reachable(fa, state)
        if result != correct:
            print("Hledany uzel: {}".format(state))
            print("Spatna odpoved {}, spravna mela byt {}."
                  .format(result, correct))
            ib002_output_fa(fa, 'bireachable')
            return False

        if (fa.table != case.fa.table) or (fa.accepting != case.fa.accepting):
            print("Chyba! Doslo k modifikaci vstupniho automatu.")
            return False

    return True


def ib002_run_test(test, msg):
    # basic
    ib002_test_header(msg, basic=True)
    if test is ib002_test_accepts:
        result = ib002_try_test(test, IB002_CASES[0])
    elif test is ib002_test_unreachable:
        result = ib002_try_test(test, IB002_CASES[1])
    elif test is ib002_test_bi_reachable:
        result = ib002_try_test(test, IB002_CASES[2])
    elif test is ib002_test_shortest_cycle_length:
        result = ib002_try_test(test, IB002_CASES[3])
    elif test is ib002_test_shortest_cycle_nodes:
        result = ib002_try_test(test, IB002_CASES[3])
    ib002_test_report(ok=result, basic=True)

    if not result:
        return

    # extended
    ib002_test_header(msg, basic=False)
    for i in range(len(IB002_CASES)):
        if not ib002_try_test(test, IB002_CASES[i]):
            ib002_test_report(ok=False, basic=False)
            return

    ib002_test_report(ok=True, basic=False)


def ib002_try_test(test, *args):
    import traceback
    import sys
    try:
        return test(*args)
    except Exception:
        print("Test vyhodil vyjimku:")
        traceback.print_exc(file=sys.stdout)
        return False


def ib002_main():
    for test, msg in ((ib002_test_accepts, "accepts"),
                      (ib002_test_unreachable, "unreachable"),
                      (ib002_test_bi_reachable, "bi_reachable"),
                      (ib002_test_shortest_cycle_length,
                       "shortest_cycle (delka cyklu)"),
                      (ib002_test_shortest_cycle_nodes,
                       "shortest_cycle (uzly cyklu)")):
        ib002_run_test(test, msg)


def ib002_draw_all():
    print("\nVsechny testovaci automaty jsou v souborech 1.dot, 2.dot ...")
    for i in range(len(IB002_CASES)):
        print_fa(IB002_CASES[i].fa, "{}.dot".format(i))


if __name__ == '__main__':
    ib002_main()
#     ib002_draw_all()