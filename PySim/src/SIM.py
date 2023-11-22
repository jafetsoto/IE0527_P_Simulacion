# =========================================================
# ---------------------------------------------------------
# Bibliotecas:
import numpy as np
from CODIFICADOR import *
# ---------------------------------------------------------
# =========================================================
# ----------------------- Main: ---------------------------
# Carga del mensaje que enviaremos:
def GET_MENSAJE():
    '''Se carga el archivo de texto, enviado desde la casa para simular.
        Outputs: TEXT (varible que contiene el archivo de texto.)'''
    with open('PySim/datasets/INPUT.txt', 'r') as file:
        TEXT = file.read()
    return TEXT

# Codificar el mensaje por el algoritmo de Huffman:
TEXT = GET_MENSAJE()
TEXT_CODIF, CODIGOS = CODIFICADOR(TEXT)

# ---------------------------------------------------------
print("============================================================")
print("Mensaje de entrada:\n", TEXT)
print("Mensaje Codificado:\n", TEXT_CODIF)
print("Codigos:\n", CODIGOS)
print("============================================================")
# ---------------------------------------------------------
# =========================================================
