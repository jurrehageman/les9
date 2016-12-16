#!/usr/bin/env python3

"""
Vul de invuloefening hieronder in. Maak gebruik van Lambda functies, map, zip en filter.
Gebruik voor deze opgaven GEEN comprehensions en GEEN reguliere for loops als dat niet expliciet is aangegegeven
"""
import random

#opgave 1
#start:
l1 = [9, 1, 3, 8, 7, 6]
#maak een lijst waarbij elk element gekwadrateerd wordt.
#uitkomst:
[81, 1, 9, 64, 49, 36]
antwoord = list(map(lambda x: x**2, l1))
print(1, antwoord)

#opgave 2
#start:
l1 = [9, 1, 3, 8, 7, 6]
#maak een lijst van alle even getallen
#uitkomst:
[8, 6]
antwoord = list(filter(lambda x: x % 2 == 0, l1))
print(2, antwoord)

#opgave 3
#start:
None
#gebruik range() voor het maken van een lijst van even getallen van 0 tot 10. Filter vervolgens de even getallen.
#uitkomst:
[0, 2, 4, 6, 8]
antwoord = list(filter(lambda x: x % 2 == 0, range(10)))
print(3, antwoord)

#opgave 4
# start:
l1 = [9, 1, 3, 8, 7, 6]
#maak een lijst van alle gekwadrateerde getallen, welke een even getal zijn
#uitkomst:
[64, 36]
antwoord = list(filter(lambda x: x % 2 == 0, map(lambda x: x**2, l1)))
print(4, antwoord)

#opgave 5
#start:
l1 = [(1, 2),(3, 4),(5, 6),(7, 8)]
#maak een lijst waarbij per tuple de getallen zijn opgeteld
#uitkomst:
[3, 7, 11, 15]
antwoord = list(map(lambda x: x[0]+x[1], l1))
print(5, antwoord)

#opgave 6
#start:
l1 = [0, 1, 2, 3]
l2 = ['a', 't', 'c', 'g']
#maak een lijst waarbij de twee lijsten zijn samengevoegd
#uitkomst:
[(0, 'a'), (1, 't'), (2, 'c'), (3, 'g')]
antwoord = list(zip(l1, l2))
print(6, antwoord)

#opgave 7
#start:
l1 = [0, 1, 2, 3]
l2 = ['a', 't', 'c', 'g']
#maak een lijst waarbij de twee lijsten zijn samengevoegd en bij de getallen 1 wordt opgeteld
#uitkomst:
[(1, 'a'), (2, 't'), (3, 'c'), (4, 'g')]
antwoord = list(zip(list(map(lambda x: x+1, l1)), l2))
print(7, antwoord)

#opgave 8
#start:
l1 = ['a', 't', 'c', 'g']
#maak een lijst waarbij elk element naar hoofdletters wordt omgezet
#uitkomst:
['A', 'T', 'C', 'G']
antwoord = list(map(lambda x: x.upper(), l1))
print(8, antwoord)

#opgave 9
#start:
l1 = ['a', 'b', 'c', 'g']
#maak een lijst waarbij elk element een ASCII positie is opgeschoven (+1)
#uitkomst:
['b', 'c', 'd', 'h']
antwoord = list(map(lambda x: chr((ord(x)+1)), l1))
print(9, antwoord)

#opgave 10
#start:
None
#Maak een lijst van 10 worpen met een dobbelsteen
#uitkomst:
#variabel bijv: [3, 4, 5, 1, 4, 3, 1, 2, 2, 5]
antwoord = list(map(lambda x: random.randint(1,6), range(10)))
print(10, antwoord)

#opgave 11
#start:
l1 = ["a", "t", "c","g"]
#Maak een lijst van 10 gekozen letters uit de lijst
#uitkomst:
#variabel bijv: ['g', 'c', 'g', 'g', 't', 't', 'a', 't', 't', 'c']
antwoord = list(map(lambda x: random.choice(l1), range(10)))
print(11, antwoord)

#opgave 12
#start:
l1 = ['adenine', 'thymine', 'cytosine', 'guanine']
l2 = ['a', 't', 'c', 'g']
#Maak een dict van de twee lijsten waarbij de 1-letter code de keys zijn
#uitkomst:
{'t': 'thymine', 'g': 'guanine', 'a': 'adenine', 'c': 'cytosine'}
antwoord = dict(zip(l2, l1))
print(12, antwoord)

#opgave 13
#start:
l1 = ['ggatccatcag', 'gaa', 'tctagagc', 'aagcttgagcagaggag']
#maak een lijst waarbij de lengte voor elk item uit de lijst berekend is
#uitkomst:
[11, 3, 8, 17]
antwoord = list(map(lambda x: (len(x)), l1))
print(13, antwoord)

#opgave 14
#start:
l1 = ['ggatcc', 'gaattc', 'tctaga', 'aagctt', 'aaattt', 'gggccc']
#maak een lijst van omgekeerde sequenties voor elk element.
#uitkomst:
['cctagg', 'cttaag', 'agatct', 'ttcgaa', 'tttaaa', 'cccggg']
antwoord = list(map(lambda x: x[::-1], l1))
print(14, antwoord)

#opgave 15
#start:
s1 = "ggatcc"
d1 = {'t': 	322.2, 'g': 347.2, 'a': 331.2, 'c': 307.2}
#bereken het molecuulgewicht van s1
#uitkomst:
{'t': 'thymine', 'g': 'guanine', 'a': 'adenine', 'c': 'cytosine'}
antwoord = sum(map(lambda x: d1[x], s1))
print(15, antwoord)

#opgave 16
#start:
l1 = ['ggatccatcag', 'gaa', 'tctagatcgagc', 'aagcttgagcagaggag']
#maak een lijst van elk element van de lijst waarbij de sequentie 'gatc' voorkomt.
#uitkomst:
['ggatccatcag', 'tctagatcgagc']
antwoord = list(filter(lambda x: 'gatc' in x, l1))
print(16, antwoord)

#opgave 17
#start:
l1 = ['ggatcc', 'gaattc', 'tctaga', 'aagctt', 'aaattt', 'gggccc']
#maak een lijst waarbij het GC percentage voor elk item uit de lijst berekend is
#uitkomst:
[66.66666666666666, 33.33333333333333, 33.33333333333333, 33.33333333333333, 0.0, 100.0]
antwoord = list(map(lambda x: (x.count('g')+x.count('c'))/len(x)*100, l1))
print(17, antwoord)

#opgave 18
#start:
l1 = ['ggatcc', 'gaattc', 'tctaga', 'aagctt', 'aaattt', 'gggccc']
#maak een lijst van GC gehaltes voor elk element waarvan het GC gehalte hoger is dan 50%.
#uitkomst:
[66.66666666666666, 100.0]
antwoord = list(filter(lambda x: x>50, (map(lambda x: (x.count('g')+x.count('c'))/len(x)*100, l1))))
print(18, antwoord)

#opgave 19
#start:
l1 = ['ggatcc', 'gaattc', 'tctaga', 'aagctt', 'aaattt', 'gggccc']
#maak een lijst van sequenties voor elk element waarvan het GC gehalte hoger is dan 50%.
#uitkomst:
['ggatcc', 'gggccc']
antwoord = list(filter(lambda x: (x.count('g')+x.count('c'))/len(x)*100 > 50, l1))
print(19, antwoord)

#opgave 20
#start:
l1 = ['ggatcc', 'gaattc', 'tctaga', 'aagctt', 'aaattt', 'gggccc']
#maak een lijst van sequenties voor elk element waarvan het GC gehalte hoger is dan 50%.
#GEBRUIK NU EEN LIST-COMPREHENSION
#uitkomst:
['ggatcc', 'gggccc']
antwoord = [(i.count('c')+i.count('g'))/len(i)*100 for i in l1 if (i.count('c')+i.count('g'))/len(i)*100 >50]
print(20, antwoord)

print("The End")