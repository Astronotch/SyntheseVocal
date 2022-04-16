from decoupe import *

def listeP(phraseDecoupe):
    PolyCombi = []
    Temp1PolyCombi = ""
    Temp2PolyCombi = []
    mot = 0
    for lettre in phraseDecoupe:
        for lettre in phraseDecoupe[mot]:
            Temp1PolyCombi = Temp1PolyCombi + lettre
            Temp2PolyCombi.append(Temp1PolyCombi)
        PolyCombi.append(Temp2PolyCombi)
        Temp1PolyCombi = ""
        Temp2PolyCombi = []
        mot = mot+1
    return PolyCombi

def supprimerModele(CombNom, cpt):
    #passer le mot en une liste puis supprimer les élements correspondants
    liste2 = []
    for i in range(cpt+1):
        CombNom.pop(0)
    for a in range(len(CombNom)):
        liste1 = []
        for b in range(len(CombNom[a])):
            liste1.append(CombNom[a][b])
        print(liste1)
        liste2.append(liste1)
    for c in range(cpt+1):
        if c < len(CombNom):
            for d in range(len(CombNom)):
                liste2[c].pop()
    CombNom = []
    for i in range(len(liste2)):
        mot = ""
        for j in range(len(liste2[i])):
            mot = mot + liste2[i][j]
        CombNom.append(mot)
    return CombNom

def supprimerTexte(texte, cpt):
    #Passer texte dans une liste avec chaque lettre
    #Enlever les cpt premiers éléments avec une boucle for
    #Remettre tout les éléments de la liste en place puis les remettre dans une liste
    liste1 = []
    for i in range(cpt+1):
        texte.pop(0)
    for a in range(len(texte)):
        liste2 = []
        for b in range(len(texte[a])):
            liste2.append(texte[a][b])
        liste1.append(liste2)
    texte = []
    for c in range(len(liste1)):
        mot = ""
        for d in range(cpt+1):
            liste1[c].pop(0)
        for e in range(len(liste1[c])):
            mot = mot + liste1[c][e]
        texte.append(mot)
    return texte

def DecoupeMot(texte):
    liste1 = []
    lettre = ""
    for i in texte:
        if i == " ":
            liste1.append(lettre)
            lettre = ""
        else:
            lettre = lettre + i
    return liste1


lettres = open("lettre.txt", "r")
TempDico = lettres.readlines()
texte = "essai"
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
                PolyCombi[a] = supprimerModele(PolyCombi[a], b) #Le problème est le fait que Polycombi[a] devient une liste de liste, peut-être essayer de faire un .append dans la fonction supprimer et d'agir directement sur PolyCombi[a]
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

#Il faudrait ajouter une fonction qui prend la syllabe qui a été découpé et la stock dans une liste