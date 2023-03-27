#######################################     CODE DE L'IA        ###########################################################
import socket
import json
from threading import Thread
from main import IA
from utils import requestSubscribeStringGenerator,jsonEncodeAndSend

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
        s.close()
        return 0
    rep = json.loads(response.decode())
    if rep["response"] == "ok":
        ia = IA(modele)
        new_thread = Thread(target=life,args=(ia,adress,port,))
        new_thread.start()
        s.close()
        print('réponse ok recue')
        return 0
    s.close()
    print("error no ok response from server")

def life(ia,adresse,port):#################################################1) Ecouter 2) JOUeR 3) parler 4) recommence:
    while ia.active:
        with socket.socket() as s:
                s.bind(('', port))
                s.listen()
                s.settimeout(5)
                try:
                    client, address = s.accept()
                    with client:
                        msg = json.loads(client.recv(2048).decode())
                        print('message reçu! DATA:  ' + str(msg))
                        if msg["request"] == "play":
                            nextMove = ia.think(msg["state"])
                            print("message de request play recu ")
                            client.send(nextMove)
                        elif msg["request"] == "ping":
                            client.send(json.dumps(responseToPing).encode())
                            print("requested ping... responding")
                        else:
                            print('message arrivé différent de play request ou ping!')
                except socket.timeout:
                    continue
                
    
    
    
    


    

    
#################################################################       ACTOIN      #############################################


#adress = str(input("Entrez l'adresse i.p. du serveur:   "))
adress = "localhost"
connecter()