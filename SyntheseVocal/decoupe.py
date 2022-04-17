def supp(txt):
    txt=txt.replace("\n", "")
    txt=txt.replace("consonne", "C")
    txt=txt.replace("voyelle", "V")
    txt=txt.replace("ponctuation", "P")
    return txt

def decoupage(TempDico):
    dico = []
    for i in range(0, len(TempDico)-1, 2):
        TempDico[i] = supp(TempDico[i])
        dic = []
        dic.append(TempDico[i])
        i=i+1
        TempDico[i] = supp(TempDico[i])
        dic.append(TempDico[i])
        dico.append(dic)
    return dico

def decoupePhrase(txt, TempDico):
    phrase = []
    mot = ""
    for i in txt:
        a = 0
        while i.lower() != TempDico[a][0]:
            a = a+1

        if TempDico[a][1] == "P":
            phrase.append(mot)
            mot = ""
        else:
            mot = mot + TempDico[a][1]
    return phrase

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
        liste2.append(liste1)
    for c in range(cpt+1):
        if c < len(CombNom):
            for d in range(len(CombNom)):
                liste2[d].pop()
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