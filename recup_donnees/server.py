import socket


host, port = ('', 5566)



socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("Le serveur est démarré")

while True:
    socket.listen(5)
    conn, address = socket.accept()
    print("En écoute")

    data = conn.recv(4096)
    data = data.decode("utf8")
    print(data)

conn.close()
socket.close()
