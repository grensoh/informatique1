char_adn = ['a','t','c','g'] #loiste des caractères acceptés
def is_adn(s): #fonction vérifiant si une chaine de caractère est de l'adn
    is_adn = True
    s = s.lower() #on met tout en minuscule
    for i in s:
        if i not in char_adn: #on regarde si l'élément ne se trouve pas dans la liste
            is_adn = False #si oui, la variable bascule sur False
    return is_adn

def positions(s, p): #fonction comparant 2 chaines d'AdN
    position = []
    if is_adn(s) and is_adn(p): #on vérifie si s et p sont de l'adn
        s = s.lower() #on met tout en minuscule
        p = p.lower()
        for i in range(len(s)): #pour chaque élément de s, on regarde si les caractères qui suivent correspondes à p
            if s[i:i+len(p)] == p:
                position.append(i) #si oui, on note la position de départ de la chaine p dans s
    return position


def distance_h(s, p): #fonction regardanbt le nombre de termes identiques entre s et p
    distance = 0
    if is_adn(s) and is_adn(p): #on vérifie si c'est de l'adn
        if len(s) != len(p): #on vérifie que s et p sont de même longueur
            return None
        else:
            for i in range(len(s)): #pour chaque élément on vérifie s'il est identique à l'élément correspondant dans l'autre chaine
                if s[i] != p[i]:
                    distance += 1 #si différent -> on ajoute 1 à la distance
            return distance
    else:
        return None

def distances_matrice(l): #fonction vérifiant le nombre de termes identiques entre chaque chaines d'une liste
    distance = []
    for i in range(len(l)): #pour chaque chaine de caractères, on la compare avec chaque chaine de caractères de la liste
        tempo = []
        for j in range(len(l)):
            tempo.append(distance_h(l[i], l[j])) #on appelle distance_h pour compter le nombre d'éléments différents
        distance.append(tempo)
    return distance
