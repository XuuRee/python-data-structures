# Implementacny test IB002 - uloha 2. (8 bodov)
#
# Vyplnte nasledujuce udaje:
# Meno:
# UCO:
# Skupina (v ktorej ste zapisany):
#
# Vasou ulohou je v tomto zadani naimplementovat modifikovany zasobnik.
# Implementujete modifikovane metody push a pop. Pre blizsi popis citajte
# komentare v kode.
#
# Po ukonceni prace nahrajte vas kod do odovzdavarne:
# IS -> Student -> IB002 -> Odevzdavarny -> PraktickyTest_skupina
# Odovzdavajte len zdrojovy kod, NEODOVZDAVAJTE subory s nastaveniami pre IDE.
#
# @author Henrich Lauko


# Trieda Item sluzi pre reprezentaciu objektu v zasobniku
# obsahuje atribut value reprezrezentujuci hodnotu v zasobniku
# a atribut prev reprezentujuci ukazatel na predchadzajuci prvok Item 
# v zasobniku.
class StackItem:
	value = None  # hodnota v zasobniku
	prev = None  # predchadzajuci prvok v zasobniku


# Trieda BrokenStack obsahuje ukazatel na vrchol zasobniku
class BrokenStack:
	top = None  # vrchol zasobniku


# Push vklada na vrchol zasobniku tak, ze pokial vkladana hodnota je
# vacsia alebo rovna ako vrchol zasobniku(top), vklada normalne,
# tj. prida ju nad vrchol a zmeni(top). Ak je vkladana hodnota mensia,
# vlozi ju na prvu poziciu pod vrchol.  V pripade prazdneho zasobniku (na
# vrchole je None) vkladame normalne.  Ukazku mozete vidiet na
# nasledujucom priklade:
#
# Stav zasobniku:      10| 5|       (10 je na vrchu zasobniku)
# Volame Push(11):     11|10| 5|    (11 bola vacsia ako 10)
# Volame Push(6):      11| 6|10| 5| (6 bola mensia ako 11)
#
# Pri implementacii treba z argumentu value naalokovat objekt Item a spravne
# nastavit vsetky ukazatele "prev".
#
# Dajte si pozor na pristupovanie ku objektom, ktore mozu byt None. Vzdy
# kontrolujte, k akym objektom pristupujete.
#
# Dno zasobniku kontrolujete podla toho ci je ukazatiel (top alebo prev) == None
def push(stack, value):
	item = StackItem()
	item.value = value
	if stack.top is None:	#overime ci nie je zasobnik prazdny
		stack.top = item	#ak je dame nan item
	else:
		if item.value >= stack.top.value:	#inak porovnavame hodnotu nasho item s hodnotou na vrchole a podla toho vkladame
			item.prev = stack.top
			stack.top = item
		else:
			item.prev = stack.top.prev
			stack.top.prev = item



# Metoda Pop() funguje obdobne. Pokial hodnota na vrchu zasobniku je
# vacsia alebo rovna ako hodnota hned pod vrcholom, pop funguje
# normalne, tj. odobere hornu polozku. V pripade, ze hodnota na vrchu je
# mensia ako hodnota pod vrcholom, odstrani sa zo zasobniku polozka pod
# vrcholom. Tj. odstrani sa vzdy vacsia z hodnot na vrchole a pod nim.
# Ak je v zasobniku len jedna polozka, odstani sa tato.  
# 
# Pop() vracia hodnotu polozky, ktora je odstranena zo zasobniku.
#
# V pripade zavolania pop() na prazdny zasobnik vrati sa -1;
#
# Vid priklad:
#
# Stav zasobniku:      11| 6|10| 5|
# Volame Pop():         6|10| 5|    (11 bola vacsia ako 6) Pop() vrati hodnotu 11
# Volame Pop():         6| 5|       (10 bola vacsia ako 6) Pop() vrati hodnotu 10
# Volame Pop():         5|          Pop() vrati hodnotu 5
# Volame Pop():        Empty stack! Pop() vrati -1
#
# Opat kontrolujte spravne ukazate a davajte si pozor na pracu s None.
# Nezabudnite udrziavat korektny top.
def pop(stack):
	if stack.top is None:	#overime ci nie je zasobnik prazdny
		return -1

	if stack.top.prev is None:	#overime ci v zasobniku nie je len jedna hodnota
		ret = stack.top
		stack.top = None
		return ret.value

	if stack.top.value >= stack.top.prev.value:	#inak porovnavame hodnotu prvych dvoch itemov v zasobniku a podla toho odoberame
		ret = stack.top
		stack.top = stack.top.prev
		return ret.value
	else:
		ret = stack.top.prev
		stack.top.prev = stack.top.prev.prev
		return ret.value


# Nasledujuci kod nemente!

# Vytvori retazec z hodnot v zasobniku v podobe: top|hodnota|hodnota|...|
def toString(stack):
	s = ""
	item = stack.top
	while item != None:
		s = s + str(item.value) + "|"
		item = item.prev
	if s == "":
		return "Empty stack!"
	else:
		return s


# Spocita pocet prvkov v zasobniku
def countItems(stack):
	count = 0
	item = stack.top
	while item != None:
		count += 1
		item = item.prev
	return count


print "Testing:"
stack1 = BrokenStack()
stack2 = BrokenStack()
stack3 = BrokenStack()

# Test 1.
push(stack1, 12)
print "Test 1.:",
if "12|" == toString(stack1):
	push(stack1, 9)
	if "12|9|" == toString(stack1):
		push(stack1, 11)
		push(stack1, 1)
		if "12|1|11|9|" == toString(stack1):
			print "OK"
		else:
			print "Chyba, vas stav zasobniku: " + toString(stack1) + " != 12|1|11|9|"
	else:
		print "Chyba, vas stav zasobniku: " + toString(stack1) + " != 12|9|"
else:
	print "Chyba, vas stav zasobniku: " + toString(stack1) + " != 12|"

#Test 2.
item = StackItem()
item.value = 10
stack2.top = item
push(stack2, 15)
print "Test 2.:",
if "15|10|" == toString(stack2):
	print "OK"
else:
	print "Chyba, vas stav zasobniku: " + toString(stack2) + " != 15|10|"

#Test 3.
value = pop(stack1)
print "Test 3.:",
if "1|11|9|" == toString(stack1):
	if value == 12:
		value = pop(stack1)
		if "1|9|" == toString(stack1):
			if value == 11:
				print "OK"
			else:
				print "Pop vraci jinou hodnotu " + str(value) + " != 11"
		else:
			print "Chyba, vas stav zasobniku: " + toString(stack1) + " != 1|9|"
	else:
		print "Pop vraci jinou hodnotu " + str(value) + " != 12"
else:
	print "Chyba, vas stav zasobniku: " + toString(stack1) + " != 1|11|9|"

#Test 4.
pop(stack1)
value = pop(stack1)
print "Test 4.:",
if "Empty stack!" == toString(stack1):
	if value == 1:
		value = pop(stack1)
		if "Empty stack!" == toString(stack1):
			if value == -1:
				print "OK"
			else:
				print "Pop vraci jinou hodnotu " + str(value) + " != -1"
		else:
			print "Chyba, vas stav zasobniku: " + toString(stack1) + " != Empty stack!"
	else:
		print "Pop vraci jinou hodnotu " + str(value) + " != 1"
else:
	print "Chyba, vas stav zasobniku: " + toString(stack1) + " != Empty stack!"

#Test 5.
print "Test 5.:",
for i in range(100):
	push(stack3, i)

count = countItems(stack3)

if count != 100:
	print "Chyba, pocet prvkov v zasobniku: " + str(count) + " != 100"
else:
	print "OK"

#Test 6.
print "Test 6.:",
for i in range(50):
	pop(stack3)

count = countItems(stack3)

if count != 50:
	print "Chyba, pocet prvkov v zasobniku: " + str(count) + " != 50"
else:
	for i in range(50):
		pop(stack3)

	count = countItems(stack3)

	if count != 0:
		print "Chyba, pocet prvkov v zasobniku: " + str(count) + " != 50"
	else:
		print "OK"
	
