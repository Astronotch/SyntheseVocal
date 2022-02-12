from decoupe import *

lettres = open("lettre.txt", "r")
TempDico = lettres.readlines()
texte = "Ceci est un essai "

syllabe = open("combinaisonSyllabe.txt", "r")
Temp = syllabe.readlines()
for i in range(len(Temp)):
    Temp[i] = supp(Temp[i])

TempDico = decoupage(TempDico)
phraseDecoupe, test = decoupePhrase(texte, TempDico)
#print(test[0])


PolyCombi = []
cpt = 0
for mot in test:
    r = ""
    TempPolyCombi = []
    for lettre in test[cpt]:
        r = r + lettre
        TempPolyCombi.append(r)
    PolyCombi.append(TempPolyCombi)
    cpt = cpt + 1



z = len(Temp)-1
a = 0
b=0


while PolyCombi[a][b] != Temp[z]:
    while PolyCombi[a][b] != Temp[z] or b < len(PolyCombi[a]):
        print(PolyCombi[a][b])
        b = b + 1
    print(PolyCombi[a][b])
    b = 0
    a = a+1
