# ---------------------------------------------------------
# Bibliotecas:
import numpy as np
import matplotlib.pyplot as plt
# ---------------------------------------------------------
# ====================== Modulador: =======================
def BPSK(CODIGO):
    # ---- Parametros de la portadora: ------
    Frecuencia = 1000
    Amplitud   = 1.0
    
    FASE_0 = 0
    FASE_1 = np.pi                                              # Desfase de 180°.
    
    PSK_SIGNAL = []
    # ---------------------------------------
    for i in CODIGO:
        if i == '0':
            Time     = np.linspace(0, 1, 1000)                  # De 0 a 1 en 1000 pasos(Hz)
            B_SIGNAL = Amplitud * np.sin(2 * np.pi * Frecuencia * Time + FASE_0)
            
            PSK_SIGNAL.extend(B_SIGNAL)
            
        else:
            Time     = np.linspace(0, 1, 1000)                  # De 0 a 1 en 1000 pasos(Hz)
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
    DEMOD_SIGNAL  = []
    BITS_DEMOD    = ''     
    Time  = np.linspace(0, 1, 1000)
    BIT_0 = np.sin(2 * np.pi * F * Time + 0)
    BIT_1 = np.sin(2 * np.pi * F * Time + np.pi)
    
    SIGNAL_Bits  = len(Signal) / F
    
    for i in range(0, len(Signal), F):
        SIGNAL_BLOCKs.append(Signal[ i : i + F])

    for SIGNAL_i in SIGNAL_BLOCKs:
        '''Calcular correlacón y comparar con las mascaras, semejanza de mayor 
        valor indica si es 1 o 0.'''
        CORRELACION_1 = np.correlate(BIT_1, 0.5 * SIGNAL_i)           # Correlacion entre la mascara y la señal del bit 1.
        CORRELACION_0 = np.correlate(BIT_0, 0.5 * SIGNAL_i)
        
        if CORRELACION_1 > CORRELACION_0:
            DEMOD_SIGNAL.extend(BIT_1)
            BITS_DEMOD += '1'    
        else:
            DEMOD_SIGNAL.extend(BIT_0)
            BITS_DEMOD += '0' 
        
    return DEMOD_SIGNAL, BITS_DEMOD
# ---------------------------------------------------------
