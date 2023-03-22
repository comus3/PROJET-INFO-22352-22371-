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
        with socket.socket() as s:
            s.send(requestSubscribeStringGenerator(port))
            response = s.recv(2048).decode()
    except:
        print("subscribe raté")
    if response != "ok":
        print("error no ok response from server")
    

    
    
    
connecter()


