#######################################     CODE DE L'IA        ###########################################################
import socket

s = socket.socket()

def requestSubscribeStringGenerator(port):
    request_subscribe = {
        "request": "subscribe",
        "port": port,
        "name": "BOss",
        "matricules": ["22352", "22371"]
    }
    return request_subscribe



def connecter():
    adress = str(input("Entrez l'adresse i.p. du serveur"))
    port = int(input("Entrez le port de l'IA actuelle"))
    try:
        s.connect(adress,port)
    except:
        print("erreur connection non reussie")
    try:
        s.send(requestSubscribeStringGenerator(port))
    except:
        print("subscribe raté")
    
    
connecter()


