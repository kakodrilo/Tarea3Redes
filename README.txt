

Laboratorio 3 - Redes de Computadores

Joaquín Castillo   -  201773520-1
María Paz Morales  -  201773505-8

Para la ejecución correcta de la red y permitir el envío de mensajes entre los host
es necesario instalar pox.
Ubicados en la carpeta mininet, escribir en la terminal:

			~/mininet$ git clone http://github.com/noxrepo/pox
			~/mininet$ cd pox
			~/mininet/pox$ git checkout dart

Además es necesario utilizar python en su version 2.7 y mininet según las instrucciones de Aula.


-> Consideración: Los controladores se construyeron modificando el archivo l2_learinng.py de pox. 
	Especificacemente se modificó la función __handle__PacketIn

------- Red 1: Anillo simple --------

Para la ejecución de esta parte del laboratorio se deben mover los archivos: 

	* red1.py
	* red1_2.py
	* red1_3.py

a la carpeta  "mininet/pox/pox/forwarding".
Y también se debe mover el archivo "Topología.py" a la carpeta "mininet/custom".
Una vez hecho esto se está listo para ejecutar los controladores y la red, para cada caso se deben abrir 2 terminales dentro de la carpeta "mininet".

Descripción de la topología:

                              hE        hF
                                \      /  
                                 \    /
                     ------------- s3 ------------
                     |                           |
                     |                           |
                     |                           |
                     ----- s1 ----------- s2 -----
                          / \            /  \
                         /   \          /    \
                        hA   hB        hC    hD

Para definir de manera más sencillas las reglas en el controlador se definieron los switch X, Y y Z como s1, s2 y s3 
respectivamente, y además se les agregó una id a cada uno: s1 tiene un dpid = 1, el s2 tiene un dpid = 2 y el s3 tiene un dpid = 3. 
Respecto a los host se definieron una MAC de la siguiente manera:

	* host A -> hA con mac 00:00:00:00:00:01
	* host B -> hB con mac 00:00:00:00:00:02
	* host C -> hC con mac 00:00:00:00:00:03
	* host D -> hD con mac 00:00:00:00:00:04
	* host E -> hE con mac 00:00:00:00:00:05
	* host F -> hF con mac 00:00:00:00:00:06

y los enlaces correspondiente están en los siguientes puertos:

	* hA puerto 0  <->  s1 con puerto 1
	* hB puerto 0  <->  s1 con puerto 2

	* hC puerto 0  <->  s2 con puerto 3
	* hD puerto 0  <->  s2 con puerto 4

	* hE puerto 0  <->  s3 con puerto 5
	* hF puerto 0  <->  s3 con puerto 6

	* s1 puerto 7  <->  s2 con puerto 8
	* s1 puerto 9  <->  s3 con puerto 10
	* s2 puerto 11 <->  s3 con puerto 12


Problema 1:

	Controlador:
		Ejecutar en una de las teminales el siguiente comando:

				~/mininet$ python2.7 pox/pox.py --verbose openflow.spanning_tree --no-flood --hold-down openflow.discovery forwarding.red1

	Topología:
		Ejecutar en la otra terminal el siguiente comando:

				~/mininet$ sudo mn --custom custom/Topologia.py --topo Red1 --controller remote --switch ovsk --mac

		notar que se verán cambios en la terminal del controlador, esto quiere decir que está escuchando a la red de la topología.
	
	Una vez iniciado ambos procesos se puede probar las conexiones.

	* Para comprobar la comuniación entre todos los host, en la terminal de la topología ejecutar:
	
				mininet> pingall
	
	Esto mostrara una tabla indicando todas las conexiones de cada host y una X en caso de que cierta conexión no exista.

	* Para borrar uno de los enlaces entre los switch se debe ejecutar en la terminal de la topología:

				mininet> link {s1} {s2} down

	* Para volver a activarlo:

				mininet> link {s1} {s2} up

	donde {s1} y {s2} son los switch entre los que se borrará o levantara el enlace.


	Comentario de lo ocurrido al eliminar uno de los enlaces entre switch:

	Para corroborar y ayudar al análisis se incluyó un print en el controlador, que indica por qué switch pasan los mensajes.
	Antes de eliminar el enlace, se comprobó que todos los host se pudieran comuniar entre sí( se hizo un "pingall"). 
	Luego se eliminó el enlace entre el switch X y el switch Y  (usando "link s1 s2 down" ), se volvió a comprobar 
	la conexión entre los host (pingall), esta vez los host A y B no pudieron comunicarse con los host C y D, pero al 
	realizar otra vez la comprobación, es decir, al ejecutar por segunda vez el comando, estos host sí lograron comunicarse.
	Esto se debe a que en un inicio, al eliminar el enlace, los switch ya no saben cómo llegar, pero una vez que se comunican
	con el switch Z, el switch X aprende un nuevo camino hacia el switch Y, y el switch Y aprende un nuevo camino hacia X.
	En otras palabras, al eliminar un enlace, los switch aprenden nuevas fromas de comunicarse ya que esán bajo el protocolo
	de Openflow y los switch actualizan sus tablas de flujo.

Problema 2 - Sentido Horario:

	Controlador:
		Ejecutar en una de las teminales el siguiente comando:

				~/mininet$ python2.7 pox/pox.py --verbose openflow.spanning_tree --no-flood --hold-down openflow.discovery forwarding.red1_2

	Topología:
		Ejecutar en la otra terminal el siguiente comando:

				~/mininet$ sudo mn --custom custom/Topologia.py --topo Red1 --controller remote --switch ovsk --mac

		notar que se verán cambios en la terminal del controlador, esto quiere decir que está escuchando a la red de la topología.
	
	Una vez iniciado ambos procesos se puede probar las conexiones.
	En el controlador se agregó un print que indica los switch por los que pasa el paquete.

	* Para hacer un ping de 1 paquete entre dos hot específicos se debe ingresar en la terminal de la topología:

				mininet> {hA} ping -c 1 {hC}

	donde {hA} y {hC} son los host en los que se realiza el ping.

	En la terminal del controlador se mostrará los switch por los que pasa el mensaje, que ayuda a identificar
	el camino que sigue el paquete.


Problema 3 - Maximizar el uso del enlace entre X e Y:

	Controlador:
		Ejecutar en una de las teminales el siguiente comando:

				~/mininet$ python2.7 pox/pox.py --verbose openflow.spanning_tree --no-flood --hold-down openflow.discovery forwarding.red1_3

	Topología:
		Ejecutar en la otra terminal el siguiente comando:

				~/mininet$ sudo mn --custom custom/Topologia.py --topo Red1 --controller remote --switch ovsk --mac

		notar que se verán cambios en la terminal del controlador, esto quiere decir que está escuchando a la red de la topología.
	
	Una vez iniciado ambos procesos se puede probar las conexiones.
	En el controlador se agregó un print que indica los switch por los que pasa el paquete.

	* Para hacer un ping de 1 paquete entre dos host específicos se debe ingresar en la terminal de la topología:

				mininet> {hA} ping -c 1 {hC}

	donde {hA} y {hC} son los host en los que se realiza el ping.

	En la terminal del controlador se mostrará los switch por los que pasa el mensaje, que ayuda a identificar
	el camino que sigue el paquete.



------- Red 2: Dos Caminos --------

Para la ejecución de esta parte del laboratorio se deben mover el archivo: 

	* red2.py

a la carpeta  "mininet/pox/pox/forwarding".
Y también se debe mover el archivo "Topología.py" a la carpeta "mininet/custom".
Una vez hecho esto se está listo para ejecutar los controladores y la red, para cada caso se deben abrir 2 terminales dentro de la carpeta "mininet".

Descripción de la topología:

                  ------ s2 ----------- s3 ---------- s4   
                  |      |              |             |
                  |      |              |             |
        hG ----- s1      |              |             |
                  |      |              |             |
                  |      |              |             |
                  ----- s5 ----------- s6 ----------- s7 
                       / \            /  \           /  \
                      /   \          /    \         /    \
                     hA   hB        hC    hD       hF    hG

Para definir de manera más sencillas las reglas en el controlador se definieron los switch T, U, W, 
Y, V, X y Z como s1, s2, s3, s4, s5, s6 y s7 respectivamente, y además se les agregó una id a cada uno 
correspondiente al numero mostrado.
Respecto a los host se definieron una MAC de la siguiente manera:

	* host A -> hA con mac 00:00:00:00:00:01
	* host B -> hB con mac 00:00:00:00:00:02
	* host C -> hC con mac 00:00:00:00:00:03
	* host D -> hD con mac 00:00:00:00:00:04
	* host E -> hE con mac 00:00:00:00:00:05
	* host F -> hF con mac 00:00:00:00:00:06
	* host G -> hG con mac 00:00:00:00:00:07

y los enlaces correspondiente están en los siguientes puertos:

	* hA puerto 0   <->  s5 con puerto 1
	* hB puerto 0   <->  s5 con puerto 2

	* hC puerto 0   <->  s6 con puerto 3
	* hD puerto 0   <->  s6 con puerto 4

	* hE puerto 0   <->  s7 con puerto 5
	* hF puerto 0   <->  s7 con puerto 6

	* hG puerto 16  <->  s1 con puerto 15

	* s1 puerto 14  <->  s2 con puerto 13
	* s1 puerto 17  <->  s5 con puerto 18

	* s5 puerto 23  <->  s2 con puerto 24

	* s2 puerto 12  <->  s3 con puerto 11
	* s5 puerto 19  <->  s6 con puerto 20

	* s6 puerto 25  <->  s3 con puerto 26

	* s3 puerto 10  <->  s4 con puerto 9
	* s6 puerto 21  <->  s7 con puerto 22

	* s7 puerto 7   <->  s4 con puerto 8


Problema:
	
	Controlador:
		Ejecutar en una de las teminales el siguiente comando:

				~/mininet$ python2.7 pox/pox.py --verbose openflow.spanning_tree --no-flood --hold-down openflow.discovery forwarding.red2

	Topología:
		Ejecutar en la otra terminal el siguiente comando:

				~/mininet$ sudo mn --custom custom/Topologia.py --topo Red2 --controller remote --switch ovsk --mac

		notar que se verán cambios en la terminal del controlador, esto quiere decir que está escuchando a la red de la topología.


	* Para convertir al hG en un servidor http se debe esctibir lo siguiente en la terminal de la Terminología:

				mininet> hG python2.7 -m SimpleHTTPServer 80 &

	* Para realizar la consulta http poner en la terminal de la topología:

				mininet> {hB} wget -O - hG

	 donde hB debe ser uno de los host definidos anteriormente.

	 Si se realiza un "pingall" en la red, se comprueba que ninguín host puede comunicarse entre sí.
	 Y que tampoco puede comunicarse con el Servidor a no ser que sea una consulta http.