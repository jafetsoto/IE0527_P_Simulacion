# ---------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
# ---------------------------------------------------------
# ===================== Transmisor: ======================
def Transmision(MOD_SIGNAL):
    SNR_dB = 10
    SIGNAL = MOD_SIGNAL * 0.5                                   # Atenuar la señal 50%
    
    RUIDO = np.random.randn(len(SIGNAL))                        # Ruido aleatorep
    
    P_SIGNAL = np.sum(SIGNAL ** 2) / len(SIGNAL)                # Potencia de la señal.
    P_RUIDO  = P_SIGNAL / (10**(SNR_dB/10))                     # Potencia del ruido.
    
    FACTOR_SNR =  np.sqrt(P_RUIDO / np.var(RUIDO))
    
    SIGNAL += RUIDO * FACTOR_SNR
    
    return SIGNAL