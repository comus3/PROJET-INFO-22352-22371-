import json
#### ---FAIT---    ######CREER CLASSE QUI VA CREER DES OBJETS IA, CHAQUE OBJET IA A UN ATRIBUT Active LES OBJETS SAPPELLLENT IA ET SONT RANGES DANS UNE LISTE
#aussi un attribut socket qui est son socket
#chaque objet ia possede uun attribut modèle qui pinte vers la fonction a utiliser pour calculer le next move
#ecdrire le premier modèle
#### ---A FAIRE--- ######
#-Simulateur du jeu
#-modele d'ia


listeIA = []

def returnListeIA():
    return listeIA

class IA:
    def __init__(self,modele):
        global listeIA
        self.active = True
        if modele == "manuel":
            self.modele = Manuel([])
        else:
            self.modele = Manuel([])
        listeIA.append(self)
        self.name = "IA" + str(len(listeIA))
    def __str__(self):
        print("je suis l'ia associée au port" + self.port)
    def think(self,msg):
        print("message pour "+self.name)
        return self.modele.nextMove(msg)
    def kill(self):
        self.active = False
        
        

####################### MODèLES IA  ################################

class Manuel:
    def __init__(self,state):
        self.state = state
        self.history = []
    def nextMove(self,status):
        cardinaux = [False,False,False,False]
        user_input_orientation = str(input("message d'orignie:  \n\n\n\n"+str(status) + "\n\n\n\n\n orientation? (N/E/S/W... 1 et 0)   >>"))
        user_input_gate = input("which gate..?  \n>>")
        user_input_newpos = input("and new pos? \n>>")
        try:
            j = 0
            for i in user_input_orientation:
                cardinaux[j] = bool(i)
                j= j+1
            tile ={
                "N": cardinaux[0],
                "E": cardinaux[1],
                "S": cardinaux[2],
                "W": cardinaux[3],
                "item": 1
            }
            move ={
                "tile": tile,
                "gate": user_input_gate,
                "new_position": user_input_newpos
            }
            output = {
                "response": "move",
                "move": move,
                "message": "Y o Y"
            }
            return json.dumps(output).encode()
        except:
            print('erreur au moment de créer la réponse, veuillez reessayer')
            self.nextMove(status)

