# =========================================================
# ---------------------------------------------------------
# Bibliotecas:
import numpy as np
from CODIFICADOR import *
from HAMMING import HAMMING
# ---------------------------------------------------------
# =========================================================
# ----------------------- Main: ---------------------------
def GET_MENSAJE():
    '''Se carga el archivo de texto, enviado desde la casa para simular.
        Outputs: TEXT (varible que contiene el archivo de texto.)'''
    with open('PySim/datasets/INPUT.txt', 'r') as file:
        TEXT = file.read()
    return TEXT
# ---------------------------------------------------------
# Cargae el mensaje:
TEXT = GET_MENSAJE()

# Codificar por Huffman para la funete:
TEXT_CODIF, CODIGOS = CODIFICADOR(TEXT)

# Codificar por Hamming para el canal:
TEXT_CANAL = HAMMING(TEXT_CODIF)

# ---------------------------------------------------------
print("============================================================")
print("Mensaje de entrada   :\n", TEXT)
print("Mensaje Codif Huffman:\n", TEXT_CODIF)
print("Codigos:\n", CODIGOS)
print("Mensaje Codif Hamming:\n", TEXT_CANAL)
print("============================================================")
# ---------------------------------------------------------
# =========================================================
