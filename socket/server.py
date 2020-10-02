import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.0.34", 1050))
server.listen(5)

print("esperando conexion...")
sc, addr = server.accept()

while True:
    print("cliente recibido: ", addr)
    recibidoCliente = sc.recv(1024)
    recibido = recibidoCliente.decode('utf-8')
    if recibido == "salir":
        mensaje = "salir"
        sc.send(mensaje.encode('utf-8'))
        break
    print("Recibido: ", recibido)
    
    try:
        n = int(recibido)
        if n % 2 == 0:
            mensaje = "el numero es par"
        else:
            mensaje = "el numero es ipar"
    except:
        print("valor no valido recibido")
        mensaje = "valor no valido"
    sc.send(mensaje.encode('utf-8'))

print("cerrando conexion")
sc.close()
server.close()