#######################################     CODE DE L'IA        ###########################################################
import socket
import json
from threading import Thread
from main import IA#, returnListeIA
from utils import requestSubscribeStringGenerator,jsonEncodeAndSend
import sys
#hey
portMachine = 3000
read_Terminal = True
socketList = []
responseToPing ={
       "response": "pong"
    }






def terminal():
    global read_Terminal
    print('terminal ACTIVE')
    while read_Terminal:
        command_list = ['/connect','/abandon','/exit']
        user_input = str(input(''))
        if user_input == command_list[0]:
            read_Terminal = False
            if connecter() == 0:
                read_Terminal = True
        elif user_input == command_list[1]:
            continue
            #for John in returnListeIA():
            #    John.kill()
        elif user_input == command_list[2]:
            sys.exit()
        else:
            print('commande non reconnue')

                
def connecter():
    global read_Terminal
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
        new_thread = Thread(target=life,args=(ia,port))
        new_thread.start()
        s.close()
        print('réponse ok recue')
        return 0
    s.close()
    print("error no ok response from server")

def life(ia,port):#################################################1) Ecouter 2) JOUeR 3) parler 4) recommence:
    global read_Terminal
    with socket.socket() as s:
        s.bind(('', port))
        s.listen()
        #s.settimeout(5)
        while ia.active:
            try:
                client, address = s.accept()
                with client:
                    msg = json.loads(client.recv(20048).decode())
                    print("message reçu!... Qu'en faire?")
                    if msg["request"] == "play":
                        read_Terminal = False
                        nextMove = ia.think(msg["state"])
                        read_Terminal = True
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
terminal_Thread = Thread(target=terminal)
terminal_Thread.start()
