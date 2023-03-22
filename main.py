
#CREER CLASSE QUI VA CREER DES OBJETS IA, CHAQUE OBJET IA A UN ATRIBUT Active LES OBJETS SAPPELLLENT IA ET SONT RANGES DANS UNE LISTE
#aussi un attribut socket qui est son socket
listeIA = []


class IA:
    def __init__(self,s,port,adress):
        self.active = True
        self.socket = s
        self.port = port
        self.adress = adress
        listeIA.append(self)
    def __str__(self):
        print("je suis l'ia associée au port" + self.port)
    def think(self,msg):
        
        return input('reponse demandée  ')