# ---------------------------------------------------------
# Bibliotecas:
import numpy as np
from scipy import signal
from sklearn import base
# ---------------------------------------------------------
# ====================== Modulador: =======================
def BPSK(CODIGO):
    # ---- Parametros de la portadora: ------
    Frecuencia = 1000
    Amplitud   = 1.0
    
    FASE_0 = 0
    FASE_1 = np.pi                                      # Desfase de 180°.
    
    PSK_SIGNAL = []
    # ---------------------------------------
    for i in CODIGO:
        if i == '0':
            Time     = np.linspace(0, 1, 1000)            # De 0 a 1 en 1000 pasos(Hz)
            B_SIGNAL = Amplitud * np.sin(2 * np.pi * Frecuencia * Time + FASE_0)
            
            PSK_SIGNAL.extend(B_SIGNAL)
            
        else:
            Time     = np.linspace(0, 1, 1000)            # De 0 a 1 en 1000 pasos(Hz)
            B_SIGNAL = Amplitud * np.sin(2 * np.pi * Frecuencia * Time + FASE_1)
            
            PSK_SIGNAL.extend(B_SIGNAL)
            
    return np.array(PSK_SIGNAL)
# ---------------------------------------------------------
# ===================== Demodulador: ======================
def DEMOD_BPSK(Signal, F):
    '''Recibimos señales con ruido que simula la transmición de
    datos en medios reales. Aproxymamos el valor real de la señal
    reduciendo el ruido y determinamos la secuencia de bitrs de 
    la señal demodulada.'''
    SIGNAL_BLOCKs = []
    Base = 0
    
    Time     = np.linspace(0, 1, 1000)
    BIT_0 = np.sin(2 * np.pi * F * Time + 0)
    BIT_1 = np.sin(2 * np.pi * F * Time + np.pi)
    
    SIGNAL_Bits  = len(Signal) / F

    for i in SIGNAL_Bits:
        # Generamos la lista con las señales de cada bit.
        SIGNAL_BLOCKs.append(Signal[Base : 1000])

              
    return 0
# ---------------------------------------------------------
