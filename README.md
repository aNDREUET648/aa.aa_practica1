# Arquitecturas Avanzadas. Práctica 1. 

_Simular una sala de espera para jugar empleando ¿socketserver?_

## Enunciado 🚀

 Los jugadores se conectan al servidor hasta que haya un número máximo _(TOPE)_.
 En ese momento el servidor avisará que ya están todos los jugadores y avisará de que están listos
 Enviará un mensaje de _Empieza el juego"_ y el programa acabará.
 
 Por otro lado, los jugadores que vayan conectándose recibirán un mensaje de acuse de recibo
 del servidor como que los ha identificado y que se esperen mientras llegan el resto de los demás jugadores.
 
 ---
[Enunciado Original](https://github.com/aNDREUET648/aa.aa_practica1/blob/master/DS_Networking_Activity.pdf) 😊
 
 

## Aspectos iniciales de la aplicación  📋

 He definido:
  - Constante **TOPE** donde inicializaré el tamaño de mi habitación _(Waiting Room)_
  - Lista **hilos_activos** que guardará el nombre del los hilo que se conecta.

 Cualquier mensaje que envíe un jugador (escribir texto en su consola) al servidor será respondido con
 un mensaje del servidor tipo: 
 
  **Gracias _Thread n_, aún quedan _p_ clientes por conectar. Vamos a esperar**
   
## Ejecutando las pruebas ⚙️
 
Tras iniciar el servidor 
 
```
$python3 waiting.py
```
 
desde otros terminales (locales o remotos pertenecientes a la LAN) iré realizando conexiones (de cliente) 
mediante el comando:

```
$nc localhost 9999
```

tantas como clientes máximos deban esperar en la sala para comenzar el juego

## Lenguaje utilizado 🛠️

* [Python 3](https://www.python.org/) - Versión 3.8.10

## Documentación y base bibliográfica 🛠️

_Las herramientas utilizadas para la realización de la práctica_

* [La Biblioteca Estándar de Python » Protocolos y soporte de Internet](https://docs.python.org/es/3.8/library/socketserver.html) - Módulo socketserver
* [La Biblioteca Estándar de Python » Ejecución Concurrente](https://docs.python.org/es/3/library/threading.html) - Threading - Paralelismos basado en hilos
* [Python 3 para impacientes](https://python-para-impacientes.blogspot.com/) - Blog acerca del lenguaje de programación Python



---
[aNDREUET648](https://github.com/aNDREUET648) 😊
