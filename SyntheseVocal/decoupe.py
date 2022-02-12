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
    phrase2 = []
    mot2 = ""
    for i in txt:
        a = 0
        while i.lower() != TempDico[a][0]:
            a = a+1

        if TempDico[a][1] != "P":
            mot = mot + TempDico[a][0]
            mot2 = mot2 + TempDico[a][1]

        else:
            phrase.append(mot)
            phrase2.append(mot2)
            mot, mot2 = "", ""
    return phrase, phrase2