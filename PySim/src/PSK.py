import numpy as np
import matplotlib.pyplot as plt

def PSK(CODIGO):
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
            
    return PSK_SIGNAL

'''
# Prueba
codigo = "110101011101"                     # Ejemplo de código.
senal_PSK = PSK(codigo)

# Tiempo de la señal:
tiempo_total = np.linspace(0, len(senal_PSK) / 1000, len(senal_PSK))

# Graficar la señal:
plt.figure(figsize=(10, 4))
plt.plot(tiempo_total, senal_PSK)
plt.title('Señal Modulada PSK')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()
'''