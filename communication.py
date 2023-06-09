#######################################     CODE DE L'IA        ###########################################################
import socket
import json
from threading import Thread
from main import IA#, returnListeIA
from utils import requestSubscribeStringGenerator,jsonEncode
import sys

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
        command_list = ['/connect','/connect -m','/abandon','/exit','/connect -t','/connect -c']
        user_input = str(input('\n>>'))
        if user_input == command_list[0]:
            read_Terminal = False
            port = int(input("Entrez le port d'écoute de l'IA actuelle:   "))
            modele = str(input("quel modele d'ia souhaitez vous utilisez? (blank for default)"))
            if connecter(port,modele) == 0:
                read_Terminal = True
        elif user_input == command_list[1]:
            numberofAIs = int(input('combien de ia?'))
            modele = input('quel modele?')
            for i in range(numberofAIs):
                port = 5596+i
                connecter(port,modele)
        elif user_input == command_list[2]:
            continue
            #for John in returnListeIA():
            #    John.kill()
        elif user_input == command_list[3]:
            sys.exit()
        elif user_input == command_list[4]:
            modeleTest = str(input('quel modele voulez vous tester?'))
            connecter(6432,'random')
            connecter(5232,modeleTest)
        elif user_input == command_list[5]:
            adress = str(input('alors, cest le grand jour?\nquelle est ladresse du serv? :  >>'))
            connecter(7120,'MPST')  
        else:
            print('commande non reconnue')

                
         
def connecter(port,modele):
    global read_Terminal
    s = socket.socket()
    
    if modele == None:
        modele = "random"
    try:
        s.connect((adress,portMachine))
        (a,b) = requestSubscribeStringGenerator(port)
        s.send(a)
        name = b
        response = s.recv(2048)         
    except Exception as e:
        print("connection echouée: ", e)
        s.close()
        return 0
    rep = json.loads(response.decode())
    if rep["response"] == "ok":
        ia = IA(modele,name)
        new_thread = Thread(target=life,args=(ia,port))
        new_thread.start()
        s.close()
        print('réponse ok recue')
        return 0
    s.close()
    print("error no ok response from server")

def receiveJSON(client):
    ok = False
    chunks = []
    data = None
    while not ok:
        chunks.append(client.recv(2048))
        try:
            data = json.loads(b''.join(chunks).decode())
            ok = True
        except json.decoder.JSONDecodeError:
            pass
    return data

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
                    #data = client.recv(20048).decode()
                    msg = receiveJSON(client)
                    print("message reçu!... Qu'en faire?")
                    if msg["request"] == "play":
                        read_Terminal = False
                        nextMove = ia.think(msg["state"])
                        read_Terminal = True
                        client.send(jsonEncode(nextMove))
                    elif msg["request"] == "ping":
                        client.send(jsonEncode(responseToPing))
                        print("requested ping... responding")
                    else:
                        print('message arrivé différent de play request ou ping!')
            except socket.timeout:
                continue
            #except Exception as e:
                #print('erreur lors du recv: ', e)

 
#################################################################       ACTOIN      #############################################
#adress = str(input("Entrez l'adresse i.p. du serveur:   "))
adress = "localhost"
terminal_Thread = Thread(target=terminal)
terminal_Thread.start()



