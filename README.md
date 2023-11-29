## IE0527_P_Simulacion:
Este repositorio almacena el código y recursos necesarios para simular la comunicación entre una habitación de una casa y una casita de árbol en el jardín; se establece un mensaje de texto de entrada que está previamente generado, codificamos el mensaje en la fuente utilizando el algoritmo de Huffman y para la codificación del canal se utilizará Hamming para agregar la capacidad de detección de errores; la señal se transmitirá por radiofrecuencia.

# Escenario hipotético: 
Simulación de un chat de texto, entre la habitación de una casa y una casita en el árbol.

## Carga del archivo:
El mensaje que enviaremos en la simulación se encuentra en:
```
PySIM/datasets/INPUT.txt
```
Y la simulación tomará en cuenta que este archivo de text fue previamente generado.

## Codificación de la fuente:
Para la codificación de la fuente implementamos el algoritmo de Huffman. El código para la codificacion de la fuente se encuentra en:
```
PySIM/src/CODIFICADOR.py
```

## Codificación del canal:
Implementamos el algoritmos de [Hamming](https://www.youtube.com/watch?v=WdmGSWrcMvM) para condificar el código generado en la etapa de codificacion de fuente; este algoritmo nos permite la corrección de errores en la recepción del mensaje, incorporando bits de paridad al código.
```
PySIM/src/HAMMING.py
```

## Modulación:
Para la modulación del codigo generado por el algoritmo de Hamming, utilizaremos BPSK, que nos permite representar los bits codificados por medio de 2 fases de onda portadora.
```
PySIM/src/PSK.py
```
### Ejemplo:
Al recibir el codigo de bits "110101011101", la codificación PSK genera la siguiente señal de salida:

![Señal PSK.](images/PSK_EJEMPLO_110101011101.png)

## Transmisión:
Simulamos un medio con ruido y una atenuacion de la señal del 50%, para simular componentes y medios ruidosos que podríamos esperar en la aplicación real de un proyecto de este estilo.
```
PySIM/src/TRANSMISION.py
```
### Ejemplo:
Para la señal transmitida utilizamos el resultado de la señal PSK que diseñamos en la etapa de modulación, el grafico de la señal transmitida es el siguiete:

![Señal transmitida.](images/TRANS_EJEMPLO_110101011101.png)

## Demodulación:
Para demodular la señal transmitida utilizamos un comparador individual de señales; para conocer si el resultado de la transmisión con ruido representa un 0 o un 1. La comparación entre la señal del primer bit enviado y las mascaras de las señales para 0 y 1 es:

![Señal comparada para el primer bit.](images/COMP_BIT1.png)

### Ejemplo:
Continuando con nuestro ejemplo, la señal demodulada del código de ejemplo es:

![Señal Demodulada.](images/DEMOD_EJEMPLO_110101011101.png)

Que coincide con la señal modulada.

El codigo de la demodulación se encuentra en:
```
PySIM/src/PSK.py
```