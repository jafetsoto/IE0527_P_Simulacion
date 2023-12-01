def Hamming_CODING(TEXT):
    '''Cargamos la cantidad de bits que tiene nuestro mensaje de entrada
    y determinamos los bits de paridad necesarios para la transmisión, creamos 
    una lista que toma en cuneta la cantidad de bits de texto y bits de paridad 
    indicamos en la posición correcta para tener paridad par colocando 'P',
    segidamente ingresamos los bits del texto manteniendo las posiciones 'P';
    finalmente calculamos los bits de paridad y devolvemos el codigo completo.
    Paridad(0 par, 1 impar)'''
    # --------------------------------------
    m = len(TEXT)                                           # Cantidad de Bits.
    P = 1                                                   # ParitiBits.
    
    j = 0                                                   # Contador para completar TXT_PARIDAD. 
    # --------------------------------------
    # Preparar el codigo con los bit de paridad:
    while 2**P < (m + P) + 1:                               # Encontrar Bits de Paridad necesarios.
        P += 1
        
    TXT_PARIDAD = [None] * (m + P)                          # (m+r) cantidad de bits; un espacio en lista para cada bit.
    
    for i in range(P):                                      # Ingresamos los bits de paridad par en el codigo del texto. 
        TXT_PARIDAD[2**i - 1] = 'P'
    
    for i in range(m + P):                                  # Recorremos todos los bits. ¿No es P?->Es bit de texto.
        if TXT_PARIDAD[i] != 'P':
            TXT_PARIDAD[i] = TEXT[j]
            
            j += 1
    # --------------------------------------
    # Determinar los bit de paridad:
    for i in range (P):                                     # Buscar las posiciones de los bits de paridad.
        P_POS   = 2**i -1
        COUNTER = 0
        
        for j in range(P_POS, m + P, 2 * (P_POS + 1)):      # range(start, stop, step)
            for k in range(j, min(j + (P_POS + 1), m + P)):
                if TXT_PARIDAD[k] == '1':
                    COUNTER += 1
                    
        if COUNTER % 2 == 0:
            TXT_PARIDAD[P_POS] = '0'   
        else:
            TXT_PARIDAD[P_POS] = '1'      
    # --------------------------------------
    return ''.join(TXT_PARIDAD)
# ---------------------------------------------------------
def Hamming_DECODE(Signal, BITS_REG):
    '''Función para decodificar código Hamming. Calculamos los bitr de 
    paridad y creamos una lista con espacio para los bits de texto del 
    mensaje (sin P bits); buscamos la posicoón de los P bits i guardamos 
    los bits de texto del codigo; '''
    m = len(BITS_REG)
    P = 1
    
    j = 0
    
    Parity_BITS = []
    B_ERROR = 0
    # --------------------
    while 2**P < (m + P) + 1:
        P += 1

    DECODE_Hamming = [None] * (m - P)
    
    for p_i in range(P):
        Parity_BITS.append(2**p_i)
    
    for i in range(m):                                      # Separamos los bits de texto
        if (i + 1) not in Parity_BITS:
            DECODE_Hamming[j] = BITS_REG[i]
            j+=1
    # --------------------------------------
    # Determinar los bit de paridad:
    for i in range (P):                                     # Buscar las posiciones de los bits de paridad.
        P_POS   = 2**i -1
        COUNTER = 0
        
        for j in range(P_POS, m, 2 * (P_POS + 1)):
            for k in range(j, min(j + (P_POS + 1), m)):
                if BITS_REG[k] == '1':
                    COUNTER += 1
        
        # Verificar errores:
        if COUNTER % 2 != 0:
            B_ERROR = 1
            error_POS = P_POS
            # Corregir error:
            DECODE_Hamming[error_POS] = '1' if DECODE_Hamming[error_POS] == '0' else '0'
    
    if B_ERROR: 
        print("Error en:", error_POS)
    else:
        print("No se detectaron errores.")
    
    return ''.join(DECODE_Hamming)
    