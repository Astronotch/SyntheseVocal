from decoupe import *

lettres = open("lettre.txt", "r")
TempDico = lettres.readlines()
texte = input("Entrez le mot que vous voulez découper en syllabe :\n")
texte = texte + " "
texteD = DecoupeMot(texte)

syllabe = open("combinaisonSyllabe.txt", "r")
Temp = syllabe.readlines()
for i in range(len(Temp)):
    Temp[i] = supp(Temp[i])

TempDico = decoupage(TempDico)
phraseDecoupe = decoupePhrase(texte, TempDico)

PolyCombi = listeP(phraseDecoupe)
texteDecoupPoly = listeP(texteD)


z = len(Temp)-1
a = 0
b = len(PolyCombi[a])-1
SyllabeMot1 = []
SyllabeMot2 = []

while a < len(PolyCombi):
    b = len(PolyCombi[a])-1  
    while b > 0:
        while z > 0:
            if a < len(PolyCombi) and Temp[z] == PolyCombi[a][b] and PolyCombi[a] != []:
                SyllabeMot1.append(Temp[z])
                SyllabeMot2.append(texteDecoupPoly[a][b])
                texteDecoupPoly[a] = supprimerTexte(texteDecoupPoly[a], b)
                PolyCombi[a] = supprimerModele(PolyCombi[a], b)                 
                if len(PolyCombi[a]) == 0:
                    a = a+1
                if a < len(PolyCombi):
                    b = len(PolyCombi[a])-1
                    z = len(Temp)-1
            elif z > 0:
                z = z-1
            elif PolyCombi[a] == []:
                a = a+1
        b = b-1
        z = len(Temp)-1
    a = a+1
print("Fini: ", SyllabeMot2)