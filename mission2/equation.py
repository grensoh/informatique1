solutions = 0
#on demande à l'utilisateur d'entrer des valeurs pour a, b, c
a = int(input("Entrez une valeur pour a : "))
b = int(input("Entrez une valeur pour b : "))
c = int(input("Entrez une valeur pour c : "))

max = int(input("Entrez la valeur maximale pour x, y et z : ")) #valeur maximale du bruteforcze

#fonction pour chercher le diviseur commun aux solutions
def div_commun(x, y, z):
    list_div = [] #liste pour stocker le ou les diviseurs
    for diviseur in range(2, max+1): #on exclut 1 car mentionné dans la consigne
        if x%diviseur == 0 and y%diviseur == 0 and z%diviseur == 0:
            list_div.append(diviseur)
            continue
    return list_div #output de la fonction

for x in range(1, max+1): #3 variables, donc 3 boucles for
    for y in range(1, max+1):
        for z in range(1, max+1):
            if x**a + y**b == z**c: #on pose l'équation
                print(f"Racines :\nx = {x}, y = {y}, z = {z}")
                list_div = div_commun(x, y, z) #vérification de la conformité des solutions
                if len(list_div) == 0: #la liste ne contient aucun diviseur
                    print("Aucun diviseur commun trouvé")
                else: #la liste contient des diviseurs
                    print(f"Ces racines possèdent un diviseur commun")
                    solutions += 1

#mise en forme claire du nombre de solutions conformes à l'équation
if solutions == 0:
    print("Aucune solution trouvée")
else:
    print(f"Il y a {solutions} solution(s) à l'équation x**{a} + y**{b} = z**{c}")
