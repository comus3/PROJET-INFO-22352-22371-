#######################################     CODE DE L'IA        ###########################################################
import socket
import json
from threading import Thread
from main import IA
from utils import requestSubscribeStringGenerator,jsonEncodeAndSend,respondToPing

portMachine = 3000
socketList = []
responseToPing ={
       "response": "pong"
    }






            

def connecter():
    s = socket.socket()
    socketList.append(s)
    port = int(input("Entrez le port d'écoute de l'IA actuelle:   "))
    modele = str(input("quel modele d'ia souhaitez vous utilisez? (blank for default)      "))
    if modele == None:
        modele = "manuel"
    try:
        s.connect((adress,portMachine))
        s.send(requestSubscribeStringGenerator(port))
        response = s.recv(2048)
    except Exception as e:
        print("connection echouée: ", e)
        return 0
    rep = json.loads(response)
    if rep["response"] == "ok":
        ia = IA(s,port,adress,modele)
        new_thread = Thread(target=life,args=(ia,))
        new_thread.start()
        print('réponse ok recue')
        return 0
    print("error no ok response from server")

def life(ia):#################################################1) Ecouter 2) JOUeR 3) parler 4) recommencer
    while ia.active:
        read = True
        while read:
            try:
                rep = ia.socket.recv(2048)
                msg = json.loads(rep)
                if msg["request"] == "play":
                    nextMove = ia.think(msg["state"])
                    read = False
                    print("message de request recu !     "  + str(msg))
                elif msg["request"] == "ping":
                    respondToPing(ia.socket)
                else:
                    print('message arrivé différent de play request ou ping!')
            except Exception as e:
                #print("message arrival error!       ", e)
                continue
            jsonEncodeAndSend(nextMove)

    
    
    
    


    

    
#################################################################       ACTOIN      #############################################


#adress = str(input("Entrez l'adresse i.p. du serveur:   "))
adress = "localhost"
connecter()