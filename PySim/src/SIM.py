# =========================================================
# ---------------------------------------------------------
# Bibliotecas:
from tkinter.tix import TEXT
import numpy as np
import matplotlib.pyplot as plt

from CODIFICADOR import *
from HAMMING import HAMMING
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

# Codificar por Huffman para la funete:
TEXT_CODIF, CODIGOS = CODIFICADOR(TEXT)

# Codificar por Hamming para el canal:
TEXT_CANAL = HAMMING(TEXT_CODIF)
TEXT_PRUEBA = '110101011101'
# Modular la señal:
SIGNAL_PSK   = BPSK(TEXT_PRUEBA)
graf_Signal(SIGNAL_PSK, 1000, 'Señal modulada (BPSK).')

# Simular transmisión:
SIGNAL_TRANSMIT = Transmision(SIGNAL_PSK)
graf_Signal(SIGNAL_TRANSMIT, 1000, 'Señal transmitida.')

# Demodular la señal recibida: 
DEMOD_TEXT = DEMOD_BPSK(SIGNAL_TRANSMIT, 1000)
graf_Signal(DEMOD_TEXT,1000, 'Señal demodulada.')

# ---------------------------------------------------------
print("============================================================")
print("Mensaje de entrada   :\n", TEXT)
print("Mensaje Codif Huffman:\n", TEXT_CODIF)
print("Codigos:\n", CODIGOS)
print("Mensaje Codif Hamming:\n", TEXT_CANAL)
print("============================================================")
# ---------------------------------------------------------
# =========================================================
