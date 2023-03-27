
#### ---FAIT---    ######CREER CLASSE QUI VA CREER DES OBJETS IA, CHAQUE OBJET IA A UN ATRIBUT Active LES OBJETS SAPPELLLENT IA ET SONT RANGES DANS UNE LISTE
#aussi un attribut socket qui est son socket
#chaque objet ia possede uun attribut modèle qui pinte vers la fonction a utiliser pour calculer le next move
#ecdrire le premier modèle
#### ---A FAIRE--- ######
listeIA = []


class IA:
    def __init__(self,modele):
        self.active = True
        if modele == "manuel":
            modele = Manuel([])
            self.modele = modele
        listeIA.append(self)
    def __str__(self):
        print("je suis l'ia associée au port" + self.port)
    def think(self,msg):
        return self.modele.nextMove(msg)
        
        

####################### MODèLES IA  ################################

class Manuel:
    def __init__(self,state):
        self.state = state
        self.history = []
    def nextMove(status):
        return input("reponse demandée! message d'orignie:  "+status)
    
