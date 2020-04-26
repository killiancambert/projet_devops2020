import socket


host, port = ('localhost', 5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    socket.connect((host, port))
    print("client connecté")

    data = "Bonjour blablabla"
    data = data.encode("utf8")
    socket.sendall(data)


except:
    print("Connexion au serveur échouée")

finally:
    socket.close()
