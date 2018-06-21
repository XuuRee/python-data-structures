 # Tento priklad sluzi ako vzorovy priklad, co vas moze cakat na implementacnom teste.
 # Vasou ulohou je pochopit uz implementovanu datovu strukturu Dictionary a implementovat 
 # niektore jej metody s pouzitim metod, ktore uz Dictionary obsahuje. Je mozne si doprogramovat
 # aj vlastne metody, ak vam uz naimplementovane nevyhovuju.
 
 # Slova su v slovniku reprezentovane tak, ze v kazdom uzle sa nachadza jeden znak 
 # a zoznam vsetkych moznych nasledujucich znakov. 
 
 # V nasledujucom kode implementujte metodu printWordsWithPrefix, ktora vypise v abecednom poradi
 # vsetky slova v slovniku zacinajuce na dany prefix . Davajte si pozor na to, ze znaky v jednotlivych
 # uzloch niesu nutne usporiadane.
  
 # Na vypracovanie ulohy budete mat hodinu, mozete pouzivat vlastne materialy (zbierka, slajdy) pristup na internet nebude povoleny.
 # V ramci implementacneho testu naostro budete mat vyriesit dva priklady. Toto je vzorove zadanie len jedneho prikladu.
 # Riesenie prikladu by ste mali zvladnut za 15 - 20 minut.
 
class Node:
    key = None
    children = []

#Trieda Dictionary popisuje datovu strukturu slovniku.
class Dictionary:
#Dictionary obsahuje zoznam znakov, kde pod kazdym znakom je strom so slovami
#zacinajucimi na dany znak. Slovnik nerozlisuje medzi malymi a velkymi pismenami.
    characters = []

# Vlozi slovo do slovnik
def insert(dictionary, word):
    insertToList(dictionary.characters, word)

# Funkcia pouzita pre implementaciu insert
def insertToList(chars, word):
    if word == "":
        return
    w = word[0]
    for c in chars:
        if c.key == w:
            insertToList(c.children, word[1:])
            return
    # we haven't found a successor
    n = Node()
    n.key = w
    n.children = []
    chars.append(n)
    insertToList(n.children, word[1:])
    
# Vyhlada podstrom so slovami zacinajucimi na prefix
def search(dictionary, prefix):
    return searchInList(dictionary.characters, prefix)

# Funkcia pouzita pre implementaciu search
def searchInList(chars, prefix):
    if prefix == "":
        return chars
    p = prefix[0]
    for c in chars:
        if c.key == p:
            return searchInList(c.children, prefix[1:])
    return None


 # TODO: Vrati v abecednom poradi usporiadany zoznam slov nachadzajucich sa v slovniku a zacinajucich na zadany prefix.
 # Za slovo sa povazuju tie postupnosti uzlov, ktore koncia uzlom bez deti.
 # Priklad:
 #				a
 #			  /  \	
 #			h	   u
 #		  /	  \		\	
 #		 a	   o     t	
 #				\     \
 #				 j	   o
 #				  \
 #                 t
 #                  \
 #					 e
 
 # Slova s prefixom "ah" su ["aha", "ahojte"] 
 # V pripade ze slova s prefixom neexistuju, vrati sa null.
 # V pripade ze cely prefix je jedno slovo, vrati sa zoznam obsahujuci prave toto slovo.    
def listWordsWithPrefix(dictionary, prefix):
    root = None #vytvorime novu premennu koren
    for i in range(len(dictionary.characters)): #prejdeme vsetky pociatocne pismena v slovniku
        if dictionary.characters[i].key == prefix[0]:   #a urcitme to, na ktore zacina prefix
            root = dictionary.characters[i] #priradime ho ako koren stromu, ktory budeme prechadzat
    if root is None:    #overime ci sme takyto koren nasli
        return None #ak sme nenasli znamena to ze mozme vratit none
    for i in range(len(prefix)):    #prechadzame od tohto korena dalej az kym neprideme na koniec prefixu
        for j in range(len(root.children)): #vzdy pozerame ktore z children vyhovuje nasledujucemu znaku v prefixe
            if root.children[j].key == prefix[i]:   #a tak sa pohybujeme
                root = root.children[j]
                break
    #na tomto mieste uz sme v koreni stromu obsahujuci vsetky slova zacinajuce na dany prefix
    list = []   #vytvori prazdny zoznam
    string = prefix #do novej premennej, kam si budeme ukladat postupne slova, dame implicitne dany prefix
    gimmielist(prefix,root,list,string) #zavola pomocnu funkciu, do ktorej posle prefix, odkaz na koren, prazdny list a premennu
    return sorted(list)

def gimmielist(prefix,root,list,string):
    if not root.children:   #ak sme v liste
        list.append(string) #slovo prida do zoznamu
    temp = string   #ulozime si pred rozvetvovanim poziciu kde sa nachadzame ako doposial vypocitane slovo
    for child in root.children: #v pripade ze sa strom rozvetvuje, prejdeme vsetky vetvy
        string = string + child.key #do premennej pripiseme kluc aktualneho uzlu
        root = child    #a z tohto uzlu spravime novy koren
        gimmielist(prefix,root,list,string) #rekurzivne zavolame
        string = temp   #vratime sa na ulozenu poziciu pred rozvetvenim

def testy():
    dic = Dictionary()
    insert(dic, "algoritmus")
    insert(dic, "algoritmizacia")
    insert(dic, "algologia")
    insert(dic, "funkcionalny")
    insert(dic, "funkcionalizmus")
    insert(dic, "funktiv")
    insert(dic, "futurizmus")
    insert(dic, "fuzia")

    # listWordsWithPrefix("a") vrati slova v slovniku zacinajuce na "a"
    print("Test 1:")
    print("Pozadovany vystup:\t['algologia', 'algoritmizacia', 'algoritmus']")
    print("Vas vystup:\t\t"),
    print(listWordsWithPrefix(dic, "a"))

    # listWordsWithPrefix("b") vrati slova v slovniku zacinajuce na "b"
    print("Test 2:")
    print("Pozadovany vystup:\tNone")
    print("Vas vystup:\t\t"),
    print(listWordsWithPrefix(dic, "b"))

    # listWordsWithPrefix("funkc") vrati slova v slovniku zacinajuce na "funkc"
    print("Test 3:")
    print("Pozadovany vystup:\t['funkcionalizmus', 'funkcionalny']")
    print("Vas vystup:\t\t"),
    print(listWordsWithPrefix(dic, "funkc"))

    # listWordsWithPrefix("funkc") vrati slova v slovniku zacinajuce na "fuz"
    print("Test 4:")
    print("Pozadovany vystup:\t['fuzia']")
    print("Vas vystup:\t\t"),
    print(listWordsWithPrefix(dic, "fuz"))

testy()