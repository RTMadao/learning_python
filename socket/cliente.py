import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("192.168.0.34", 1050))

while True:
    n = input("digite un numero ")
    cliente.send(n.encode("utf-8"))
    recibidoServer = cliente.recv(1024)
    recibido = recibidoServer.decode('utf-8')
    if recibido == "salir":
        break
    print("el servidor dice: ",recibido)

print("cerrando")
cliente.close()