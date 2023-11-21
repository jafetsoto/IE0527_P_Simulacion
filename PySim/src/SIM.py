# =========================================================
# ---------------------------------------------------------
# Biblioteca:
import numpy as np
# ---------------------------------------------------------
# =========================================================
# ----------------------- Main: ---------------------------
def GET_MENSAJE():
    '''Se carga el archivo de texto, enviado desde la casa para simular.
        Outputs: TEXT (varible que contiene el archivo de texto.)'''
    with open('PySim/datasets/INPUT.txt', 'r') as file:
        TEXT = file.read()
    return TEXT

def SET_CODIFICADOR(MENSAJE):
    MENSAJE_CODIF = MENSAJE.encode()
    return MENSAJE_CODIF

MENSAJE = SET_CODIFICADOR(GET_MENSAJE())
# ---------------------------------------------------------
print("============================================================")
print(MENSAJE)
print("============================================================")
# ---------------------------------------------------------
# =========================================================
