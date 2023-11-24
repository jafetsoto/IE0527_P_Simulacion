# =========================================================
# ---------------------------------------------------------
# Bibliotecas:
import numpy as np
import matplotlib.pyplot as plt

from CODIFICADOR import *
from HAMMING import HAMMING
from PSK import PSK
# ---------------------------------------------------------
# =========================================================
# ----------------------- Main: ---------------------------
def GET_MENSAJE():
    '''Se carga el archivo de texto, enviado desde la casa para simular.
        Outputs: TEXT (varible que contiene el archivo de texto.)'''
    with open('PySim/datasets/INPUT.txt', 'r') as file:
        TEXT = file.read()
    return TEXT
def grafica_PSK(PSK_SIGNAL):                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    # Tiempo de la señal:
    tiempo_total = np.linspace(0, len(PSK_SIGNAL ) / 1000, len(PSK_SIGNAL))
    
    # Graficar la señal:
    plt.figure(figsize=(10, 4))
    plt.plot(tiempo_total, PSK_SIGNAL)
    plt.title('Señal Modulada PSK')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.show()
# ---------------------------------------------------------
# Cargae el mensaje:
TEXT = GET_MENSAJE()

# Codificar por Huffman para la funete:
TEXT_CODIF, CODIGOS = CODIFICADOR(TEXT)

# Codificar por Hamming para el canal:
TEXT_CANAL = HAMMING(TEXT_CODIF)

# Modular la señal:
TEXT_PSK   = PSK(TEXT_CANAL)
# grafica_PSK(TEXT_PSK)

# Simular transmisión:


# ---------------------------------------------------------
print("============================================================")
print("Mensaje de entrada   :\n", TEXT)
print("Mensaje Codif Huffman:\n", TEXT_CODIF)
print("Codigos:\n", CODIGOS)
print("Mensaje Codif Hamming:\n", TEXT_CANAL)
print("============================================================")
# ---------------------------------------------------------
# =========================================================
