# Arquitecturas Avanzadas. Práctica 1. 
## Simular una sala de espera para jugar empleando ¿socketserver?

### - 👋 Hi, I’m @aNDREUET648

##### El objetivo del proyecto es que mediante conexiones externas a un servidor que yo definiré
 
##### Players connect to the server and wait until there are enough players (i.e. 3, 4, or 5).
### When a new user connects, the server sends a message to the waiting users of the
### number of players remaining. Once the number of players has been reached, the
### server starts and communicates a countdown to all connected users. Finally, the server
### sends a "start" message and the program ends. Implement a gentle shutdown of
### communication
### 
## Ejemplo de uso
### tras ejecutar el comando: 
###         $python3 waiting.py
### 
### iré realizando conexiones (de cliente) mediante el comando:
###         $nc localhost 9999
### tantas como clientes máximos deban esperar en la sala para comenzar el juego
### 
### Un ejemplo rápido de uso
### Las instrucciones de instalación
El resto de la documentación pertinente.
