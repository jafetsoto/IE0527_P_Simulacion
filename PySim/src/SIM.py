# =========================================================
# ---------------------------------------------------------
# Bibliotecas:
from tkinter.tix import TEXT
import numpy as np
import matplotlib.pyplot as plt

from CODIFICADOR import *
from HAMMING import HAMMING, Hamming_DECODE
from PSK import *
from TRANSMISION import Transmision
# ---------------------------------------------------------
# =========================================================
# ----------------------- Main: ---------------------------
def GET_MENSAJE():
    '''Se carga el archivo de texto, enviado desde la casa para simular.
        Outputs: TEXT (varible que contiene el archivo de texto.)'''
    with open('PySim/datasets/INPUT.txt', 'r') as file:
        TEXT = file.read()
    return TEXT
def graf_Signal(PSK_SIGNAL, fs, TITLE):                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    # Tiempo de la señal:
    tiempo_total = np.linspace(0, len(PSK_SIGNAL ) / fs, len(PSK_SIGNAL))
    
    # Graficar la señal:
    plt.figure(figsize=(10, 4))
    plt.plot(tiempo_total, PSK_SIGNAL)
    plt.title(TITLE)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.show()
# ---------------------------------------------------------
# Carga el mensaje:
TEXT = GET_MENSAJE()
TEXT_PRUEBA = '110101011101'
# Codificar por Huffman para la funete:
CODE_Huff, CODIGOS_sim = CODIFICADOR(TEXT_PRUEBA)

# Codificar por Hamming para el canal:
CODE_Hamm = HAMMING(CODE_Huff)

# Modular la señal:
SIGNAL_PSK   = BPSK(CODE_Hamm)
graf_Signal(SIGNAL_PSK, 1000, 'Señal modulada (BPSK).')

# Simular transmisión:
SIGNAL_TRANSMIT = Transmision(SIGNAL_PSK)
graf_Signal(SIGNAL_TRANSMIT, 1000, 'Señal transmitida.')

# Demodular la señal recibida: 
SIGNAL_DEMOD, CODE_DEMOD = DEMOD_BPSK(SIGNAL_TRANSMIT, 1000)
graf_Signal(SIGNAL_DEMOD,1000, 'Señal demodulada.')

# Decodificación Hamming:
DECODE_HM = Hamming_DECODE(SIGNAL_DEMOD, CODE_DEMOD)

# ---------------------------------------------------------
print("============================================================")
print("Mensaje de entrada   :\n", TEXT)
print("Mensaje Codif Huffman:\n", CODE_Huff)
print("Codigos:\n", CODIGOS_sim)
print("Codif Hamming   :\n", CODE_Hamm)
print("Decode Hamming  :\n", CODE_DEMOD)
print("Decode Huffman  :\n", DECODE_HM)
print("============================================================")
# ---------------------------------------------------------
# =========================================================
