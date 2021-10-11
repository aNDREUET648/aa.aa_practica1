import socketserver
import threading

# TOPE Número máximo de clientes que esperan en la sala (Watiting Room)
TOPE =  3          


# hilos_activos es donde guardo los nombres de los hilos
#  cgit staonectados y consecuentemente la cantidad de ellos
hilos_activos =list()  


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True
    
class WaitingHandler(socketserver.StreamRequestHandler):

    def handle(self):
        cliente_actual = threading.currentThread().getName() #nombre del cliente conectado
        client = f'{self.client_address} on {cliente_actual}'
        hilos_activos.append(cliente_actual)
        pendientes = TOPE - len(hilos_activos)
        while pendientes >= 0:
            if pendientes > 0:
                print("Mensaje del handler: Cliente {} conectado, quedan {} clientes por conectar.".format(cliente_actual, pendientes))
                # Ahora le enviamos este mismo mensaje al cliente que se ha conectado. Que esté tranquilo!!
                texto = "Gracias {}, aún quedan {} clientes por conectar. Vamos a esperar \n".format(cliente_actual, pendientes)
                self.wfile.write(bytes(texto, "utf-8"))
                data = self.rfile.readline()
            else:
                # El último cliente recibe que ya se ha conectado y que acabamos.
                texto = "Gracias {}, eras el que faltaba. Ya estamos todos\n".format(cliente_actual, pendientes)
                self.wfile.write(bytes(texto, "utf-8"))
                # El servidor ya ha completado su sala de espera y finaliza su servicio
                print("\nMensaje del handler: Cliente {} conectado, ya estamos todos..._\n".format(cliente_actual))
                print(f'Lista de Clientes activos: {hilos_activos}\n')
                break
        print("Mensaje del handler: Vamos acabando!!!")
        # Limpiamos el servidor y detenemos el bucle serve_forever()
        server.server_close()
        server.shutdown()

if __name__ == "__main__":
    lista_hilos = threading.enumerate() # hilos actuales. Si se arranca de visual studio aparecen 6 hilos
    print("\nHilo    Nombre\n")
    for i in range (len(lista_hilos)):
        print(" {}\t{}".format(i,lista_hilos[i]))
    print(f'Objetos thread activos: {threading.active_count()}')
    print(f'Nombre del hilo principal: {threading.currentThread().name}')
        
with ThreadedTCPServer(('', 9999), WaitingHandler) as server:
    print('Room server is running now and Waiting for {} customers'.format(str(TOPE)))
    server.serve_forever()