liste = [1, 6, 8, 13, 15]
temporaire = liste[0]
liste[0] = liste[-1]
liste[-1] = temporaire
print(liste)