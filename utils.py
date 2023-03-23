import socket
import json

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

