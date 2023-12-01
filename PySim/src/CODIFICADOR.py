# ---------------------------------------------------------
# Estructuras de datos:
class NODO:
    '''Clase diseñada para contener el nodo de los simbolos del arbol
    de Huffman, almacenamos el caracter(simbolo), su frecuencia y la 
    doreccion a donde apuntan las ramas del nodo (izquierda y direcha).'''
    def __init__(self, simbolo, frecuencia):
        self.simbolo     = simbolo
        self.frecuencia  = frecuencia
        self.r_izquierda = None
        self.r_derecha   = None

diccionario_simbolos = {
    'a': '000000', 'b': '000001', 'c': '000010', 'd': '000011', 'e': '000100', 'f': '000101',
    'g': '000110', 'h': '000111', 'i': '001000', 'j': '001001', 'k': '001010', 'l': '001011',
    'm': '001100', 'n': '001101', 'o': '001110', 'p': '001111', 'q': '010000', 'r': '010001',
    's': '010010', 't': '010011', 'u': '010100', 'v': '010101', 'w': '010110', 'x': '010111',
    'y': '011000', 'z': '011001', ' ': '011010', ',': '011011', '.': '011100','\n': '011101',
    ':': '011110', ';': '011111', 'á': '100000', 'é': '100001', 'í': '100010', 'ó': '100011',
    'ú': '100100', 'ñ': '100101', 'A': '100110', 'B': '100111', 'C': '101000', 'D': '101001',
    'E': '101010', 'F': '101011', 'G': '101100', 'H': '101101', 'I': '101110', 'J': '101111',
    'K': '110000', 'L': '110001', 'M': '110010', 'N': '110011', 'O': '110100', 'P': '110101',
    'Q': '110110', 'R': '110111', 'S': '111000', 'T': '111001', 'U': '111010', 'V': '111011',
    'W': '111100', 'X': '111101', 'Y': '111110', 'Z': '111111'
}


# ---------------------------------------------------------
# ================ Codificador de fuente: =================
def SET_Huffman_ARBOL(TEXTO):
    # Iterara para buscar las frecuencias de aparicion de los simbolos (caracteres).
    F_SIMBOLO = {}
    for simbolo in TEXTO:
        F_SIMBOLO[simbolo] = F_SIMBOLO.get(simbolo,0)+1
    
    # Cargamos el arbol de Huffman, generando los nodos de los simbolos del mensaje.
    ARBOL = []
    for simbolo, frecuencia in F_SIMBOLO.items():
        nodo = NODO(simbolo, frecuencia)
        ARBOL.append(nodo)
    
    while len(ARBOL)>1:                                
        ''''Ordenamos los simbolos de forma ascendente, establecemos los 2 nodos
        menos significativos al inicio de la lisa, agregamos estos 2 nodos como 
        punteros Izquierda y derecha de un nuevo nodo(NEW_NODO), eliminamos los 
        2 nodos para volver a ordenar la lista y obtener los siguientes 2 nodos 
        menos signififcativos; terminamos al tener un solo nodo, ya que será la 
        raiz del arbol de Huffman.'''
        ARBOL.sort(key=lambda x: x.frecuencia)
        PATH_IZQ = ARBOL.pop(0)                                             # Copia de Arbol que gurda el path izquierdo.
        PATH_DER = ARBOL.pop(0)                                             # Copia de Arbol que gurda el path derecho.       
        
        NEW_NODO = NODO(None, PATH_IZQ.frecuencia + PATH_DER.frecuencia)
        NEW_NODO.r_izquierda = PATH_IZQ
        NEW_NODO.r_derecha   = PATH_DER
        
        ARBOL.append(NEW_NODO)

    return ARBOL[0]                                                         # Raiz del arbol de Huffman.
# ---------------------------------------------------------
def SET_Huffman_CODIGOS(RAIZ, SIMBOL_CODE = "" , CODIGOS = None):
    '''Esta funcion se necarga de generar los codigos especificos para cada
    simbolo, utiliza la raiz del arbol que se calcula con SET_Huffman_ARBOL()
    y los punteros de las ramas que completan el arbol, al recorrer las 
    ramas que salen desde la rais podemos determinar los codigos para los 
    simbolos, que están en los nodos que no son None.'''
    # Inicializar diccionario de codigos:
    if CODIGOS is None:
        CODIGOS = {}
    
    # Encontramos un simbolo, asginamos el código:
    if RAIZ.simbolo is not None:
        CODIGOS[RAIZ.simbolo] = SIMBOL_CODE

    # Revisar los puntreros, si no están vacíos revisar el Path:
    if RAIZ.r_izquierda is not None:
        SET_Huffman_CODIGOS(RAIZ.r_izquierda, SIMBOL_CODE + "0", CODIGOS)
    if RAIZ.r_derecha is not None:
        SET_Huffman_CODIGOS(RAIZ.r_derecha, SIMBOL_CODE + "1", CODIGOS)
    return CODIGOS
# ---------------------------------------------------------
def Huffman_CODING(TEXT):
    '''Funcion principal de la codificacion de canal, se debe llamar cuando
    se desea codificar texto de entra en el la fuente. Utiliza el metodo join()
    para generar el texto coficicado con los codigos de los simbolos.'''
    RAIZ_Huffman = SET_Huffman_ARBOL(TEXT)
    CODIGOS = SET_Huffman_CODIGOS(RAIZ_Huffman)
    
    TEXT_CODFIFICADO = "".join(CODIGOS[simbolo] for simbolo in TEXT)
    
    Arbol_CODE = ''
    
    # Código de bits para el árbol: 
    for sim, k in CODIGOS.items():
        Arbol_CODE += diccionario_simbolos[sim]
    
    # Cantidad de bits que definen el árbol:
    N_Bits  = len(Arbol_CODE)
    
    Bits_complete = N_Bits % 8 
    if Bits_complete != 0:
        Arbol_CODE += '0' * (8 - Bits_complete)
        
        N_Bits  = len(Arbol_CODE)
        N_Bytes = N_Bits // 8
    
    # Metadatos: tamaño del codigo del arbol(Bytes), codigo del arbol.
    N_Bytes = bin(N_Bytes).replace("0b", "").zfill(4)
    
    print(N_Bytes, Arbol_CODE)
    
    TEXT_CODFIFICADO = N_Bytes + Arbol_CODE + TEXT_CODFIFICADO
    
    return TEXT_CODFIFICADO, CODIGOS
# ---------------------------------------------------------
# =============== Decodificador de fuente: ================
def Huffman_DECODE(Codigo):
    
    return 0