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
    F_A = 0
    F_B = F
    
    Time     = np.linspace(0, 1, 1000)
    BIT_0 = np.sin(2 * np.pi * F * Time + 0)
    BIT_1 = np.sin(2 * np.pi * F * Time + np.pi)
    
    SIGNAL_Bits  = len(Signal) / F
    
    while SIGNAL_Bits != 0:
        # Generamos la lista con las señales de cada bit.
        SIGNAL_BLOCKs.append(Signal[F_A : F_B])
        F_A  = F_B + 1
        F_B += 2
        
        SIGNAL_Bits += -1

    SEÑAL_BLOQUE_1 = SIGNAL_BLOCKs[0]                           # Bloque de la señal del primer bit
    
    CORRELACION    = np.correlate(BIT_1, SEÑAL_BLOQUE_1)           # Correlacion entre la mascara y la señal del bit 1.
    
    SIGNAL_ERROR   = np.abs(CORRELACION) / np.linalg.norm(BIT_1)*np.linalg.norm(SEÑAL_BLOQUE_1)
    
    if  SIGNAL_ERROR > 0.8:
        plt.figure(figsize=(10, 4))
        plt.plot(BIT_1, label='Señal 1')
        plt.plot(SEÑAL_BLOQUE_1, label='Señal 2')
        plt.title('Comparación de Señales')
        plt.xlabel('Tiempo')
        plt.ylabel('Amplitud')
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print("Las señales no son lo suficientemente similares para graficarlas juntas.")

              
    return 0
# ---------------------------------------------------------
