def voisins_entrants(adj:list, x:int)->list:
    liste = []
    for y in range(len(adj)):
        if x in adj[y]:
            liste.append(y)
    return liste


def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(1, len(s)): 
        if s[i] == chiffre:
            compte += 1 
        else:
            resultat += str(compte) + chiffre 
            chiffre = s[i] 
            compte = 1
    lecture_chiffre = str(compte) + chiffre 
    resultat += lecture_chiffre
    return resultat


