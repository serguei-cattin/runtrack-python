def BioCestBon(type, saison):
    if type=="fruits" and saison=="hiver":
        print("orange, mandarine et kiwi")
    if type=="fruits" and saison=="ete":
        print("Poire, fraise et cassis")
    if type=="legume" and saison=="hiver":
        print("carotte, topinambour et endive")
    if type=="fruits" and saison=="ete":
        print("artichaut, aubergine et navet")

BioCestBon("fruits", "ete")
BioCestBon("fruits", "hiver")
BioCestBon("legume", "ete")
BioCestBon("legume", "hiver")