import numpy as np
import matplotlib.pyplot as plt

def Transmision(MOD_SIGNAL, fs):
    SNR_dB = 10
    SIGNAL = MOD_SIGNAL * 0.5                                   # Atenuar la señal 50%
    
    RUIDO = np.random.randn(len(SIGNAL))                        # Ruido aleatorep
    
    P_SIGNAL = np.sum(SIGNAL ** 2) / len(SIGNAL)                # Potencia de la señal.
    P_RUIDO  = P_SIGNAL / (10**(SNR_dB/10))                     # Potencia del ruido.
    
    FACTOR_SNR =  np.sqrt(P_RUIDO / np.var(RUIDO))
    
    SIGNAL += RUIDO * FACTOR_SNR
    
    return SIGNAL
'''
# Ejemplo para graficar la señal transmitida
codigo_ejemplo = "10101010"  # Ejemplo de código de PSK
senal_modulada_ejemplo = PSK(codigo_ejemplo)
fs = 1000  # Frecuencia de muestreo

# Simular transmisión de la señal modulada
senal_transmitida = Transmision(senal_modulada_ejemplo, fs)

# Crear vector de tiempo para graficar
tiempo = np.linspace(0, len(senal_transmitida) / fs, len(senal_transmitida))

# Graficar la señal transmitida
plt.figure(figsize=(10, 4))
plt.plot(tiempo, senal_transmitida)
plt.title('Señal Transmitida')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()
'''