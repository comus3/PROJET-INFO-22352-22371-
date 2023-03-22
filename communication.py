#######################################     CODE DE L'IA        ###########################################################
import socket
import json
from threading import Thread
from main import IA


portMachine = 3000
socketList = []
responseToPing ={
       "response": "pong"
    }



def requestSubscribeStringGenerator(port):
    request_subscribe = {
        "request": "subscribe",
        "port": port,
        "name": "BOSS",#"name": "¯\_(^__^)_/¯",
        "matricules": ["22352", "22371"]
    }
    req = json.dumps(request_subscribe)
    req = req.encode()

    return req

def jsonEncodeAndSend(message,s):
    message = json.dumps(message)
    message = message.encode()
    send =False
    while send:
        try:
            s.send(message)
            send = False
        except Exception as e:
            print("envoi échoué: ", e)

def respondToPing(socket):
    jsonEncodeAndSend(responseToPing,socket)
            

def connecter():
    s = socket.socket()
    socketList.append(s)
    port = int(input("Entrez le port d'écoute de l'IA actuelle:   "))
    try:
        s.connect((adress,portMachine))
        s.send(requestSubscribeStringGenerator(port))
        response = s.recv(2048)
    except Exception as e:
        print("connection echouée: ", e)
        return 0
    rep = json.loads(response)
    if rep["response"] == "ok":
        ia = IA(s,port,adress)
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
            except Exception as e:
                #print("message arrival error!       ", e)
                continue
            msg = json.loads(rep)
            if msg["request"] == "play":
                nextMove = ia.think(msg["state"])
                read = False
                print("message de request recu !     "  + str(msg))
            elif msg["request"] == "ping":
                respondToPing(ia.socket)
            else:
                print('message arrivé différent de play request ou ping!')
                
        jsonEncodeAndSend(nextMove)

    
    
    
    


    

    
    
#adress = str(input("Entrez l'adresse i.p. du serveur:   "))
adress = "localhost"
connecter()
connecter()