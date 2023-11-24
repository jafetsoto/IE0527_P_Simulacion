def HAMMING(TEXT):
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
    while 2**P < (m+P)+1:                                   # Encontrar Bits de Paridad necesarios.
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
        
        for j in range(P_POS, m + P, 2 * (P_POS + 1)):        # range(start, stop, step)
            for k in range(j, min(j + (P_POS + 1), m + P)):
                if TXT_PARIDAD[k] == '1':
                    COUNTER += 1
                    
        if COUNTER % 2 == 0:
            TXT_PARIDAD[P_POS] = '0'   
        else:
            TXT_PARIDAD[P_POS] = '1'      
    # --------------------------------------
    return ''.join(TXT_PARIDAD)