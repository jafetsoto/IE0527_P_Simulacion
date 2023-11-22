# ---------------------------------------------------------
class NODO:
    '''Clase diseñada para contener el nodo de los simbolos del arbol
    de Huffman, almacenamos el caracter(simbolo), su frecuencia y la 
    doreccion a donde apuntan las ramas del nodo (izquierda y direcha).'''
    def __init__(self, simbolo, frecuencia):
        self.simbolo     = simbolo
        self.frecuencia  = frecuencia
        self.r_izquierda = None
        self.r_derecha   = None
# ---------------------------------------------------------
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
def CODIFICADOR(TEXT):
    '''Funcion principal de la codificacion de canal, se debe llamar cuando
    se desea codificar texto de entra en el la fuente. Utiliza el metodo join()
    para generar el texto coficicado con los codigos de los simbolos.'''
    RAIZ_Huffman     = SET_Huffman_ARBOL(TEXT)
    CODIGOS = SET_Huffman_CODIGOS(RAIZ_Huffman)
    
    TEXT_CODFIFICADO = "".join(CODIGOS[simbolo] for simbolo in TEXT)
    
    return TEXT_CODFIFICADO, CODIGOS
# ---------------------------------------------------------
