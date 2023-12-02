# =========================================================
# ---------------------------------------------------------
# Bibliotecas:
import numpy as np
import matplotlib.pyplot as plt

from CODIFICADOR import *
from HAMMING import *
from PSK import *
from TRANSMISION import Transmision
# ---------------------------------------------------------
# =========================================================
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
# ----------------------- Main: ---------------------------
# Carga el mensaje:
TEXT = GET_MENSAJE()
TEXT_PRUEBA = 'Funcional.'
print(TEXT)

# Codificar por Huffman para la funete:
CODE_Huff, CODIGOS_sim = Huffman_CODING(TEXT_PRUEBA)

# Codificar por Hamming para el canal:
CODE_Hamm = Hamming_CODING(CODE_Huff)

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

# Decodificación Huffman:
DECODE_HF = Huffman_DECODE(DECODE_HM)
# ---------------------------------------------------------
# -------------------- Resultados: ------------------------
print("============================================================")
print("====================== Simulación =========================")
print("= Mensaje de texto:\n", TEXT)
print("= Codigos de los simbolos:\n", CODIGOS_sim)
print("= Mensaje codificado por Huffman:\n", CODE_Huff)
print("= Código codificado por Hamming:\n", CODE_Hamm)
print("= Decodificación por Hamming:\n", CODE_DEMOD)
print("= Decodificación por Huffman:\n", DECODE_HM)
print("= Mensaje recibido:\n", DECODE_HF)
print("============================================================")
# ---------------------------------------------------------
# =========================================================
