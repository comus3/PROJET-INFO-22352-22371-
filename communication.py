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
    rep = json.loads(response.decode())
    if rep["response"] == "ok":
        ia = IA(modele)
        new_thread = Thread(target=life,args=(ia,adress,port,))
        new_thread.start()
        s.close()
        print('réponse ok recue')
        return 0
    print("error no ok response from server")

def life(ia,adresse,port):#################################################1) Ecouter 2) JOUeR 3) parler 4) recommence:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', port))
    s.connect((adresse,portMachine))
    while ia.active:
        read = True
        while read:
            try:
                chunks = []
                finished = False
                while not finished:
                    data = s.recv(1024)
                    chunks.append(data)
                    print(data)
                    finished = data == b' '
                msg = json.loads(b' '.join(chunks).decode())
                print(msg)
                if msg["request"] == "play":
                    nextMove = ia.think(msg["state"])
                    read = False
                    print("message de request recu !     "  + str(msg))
                elif msg["request"] == "ping":
                    respondToPing(s)
                    print("requested ping... responding")
                else:
                    print('message arrivé différent de play request ou ping!')
            except Exception as e:
                print("message arrival error!       ", e)
        jsonEncodeAndSend(nextMove)

    
    
    
    


    

    
#################################################################       ACTOIN      #############################################


#adress = str(input("Entrez l'adresse i.p. du serveur:   "))
adress = "localhost"
connecter()