# Deuxième implémentation pour les piles
class Pile:

    '''classe Pile création d’une instance Pile avec une liste'''
    
    def __init__(self):
        '''Initialise une pile vide'''
        self.liste = []
        
    def est_vide(self):
        '''Renvoie un booléen, True si la pile est vide et False sinon'''
        return len(self.liste) == 0

    def empiler(self, element):
        '''Empile element au sommet de pile'''
        self.liste.append(element)

    def depiler(self):
        '''Renvoie et enlève la valeur du sommet de pile'''
        return self.liste.pop()


    def __repr__(self):
        return repr(self.liste)
    
    
def sommet(pile):
    
    ''' Renvoie la valeur au sommet de la pile mais sans la supprimer de la pile '''
    a=pile.depiler()
    pile.empiler(a)
    return a


def mettre_disques(pile, n):
    '''met des disques de taille n à 1 sur la pile'''
    for i in range(n,0,-1):
        pile.empiler(i)
        
        
def creation_tours(n):
    ''' renvoie une liste de 3 piles,
    la première correspond à la pile des n disques,
    les autres étant vides.'''
    
    pile_1=Pile()
    pile_2=Pile()
    pile_3=Pile()
    mettre_disques(pile_1,n)
    return [pile_1,pile_2,pile_3]