#!/usr/bin/env python3

# Povolene knihovny: copy, math
# Import jakekoli jine knihovny neprojde vyhodnocovaci sluzbou.

# IB002 Domaci uloha 4.
#
# Hammingovu vzdalenost dvou stejne dlouhych binarnich retezcu
# definujeme jako pocet bitu, ve kterych se retezce lisi.
#
# Vasim ukolem je implementovat funkci hamming_distance,
# ktera pro binarni retezec 'b' a nezaporne cele cislo 'k' vrati vsechny
# binarni retezce, jejichz Hammingova vzdalenost od 'b' bude prave 'k'.
#
# Priklady chovani:
# hamming_distance('100', 0) vrati vystup: ['100']
# hamming_distance('0001', 2) vrati vystup:
#         ['1101', '1011', '1000', '0111', '0100', '0010']


def hamming_distance(b, k):
    """
    vstup: 'b' binarni retezec, 'k' nezaporne cele cislo
    vystup: pole vsech binarnich retezcu se vzdalenosti 'k' od 'b'
    casova slozitost: polynomialni vzhledem k delce binarniho retezce 'b'
        ( To znamena, ze pocet operaci je v O(n^j), kde 'n' je delka binarniho
          retezce 'b' a 'j' je nejake fixni cislo. Tedy pro slozitostni odhad
          'k' povazujeme za fixni. Vsimnete si, ze pokud budete generovat
          vsechny binarni retezce stejne delky jako 'b' a nasledne merit
          Hammingovu vzdalenost, tak se nevejdete do pozadovane slozitosti.
          Doporucejeme se zamyslet nad rekurzivnim pristupem. )
    """
    if k == 0:
        return [b]
    if k > 1:
        last, result = b[-1], []
        str1 = [i + last for i in hamming_distance(b[:-1], k)] if len(b) > k else []
        str2 = []
        for i in hamming_distance(b[:-1], k - 1):
            str2.append(i + flip(last))
        result += str1 + str2
        return result
    else:
        result = []
        for i in range(len(b)):
            result.append(flip_s(b, i))
        return result


def flip(bit):
    return '0' if bit == '1' else '1'


def flip_s(s, i):
    result = s[:i] + flip(s[i]) + s[i+1:]
    return result
