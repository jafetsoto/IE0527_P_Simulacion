# ---------------------------------------------------------
class NODO:
    '''Clase diseñada para contener el nodo de los simbolos del arbol
    de Huffman, almacenamos el caracter(simbolo), su frecuencia y la 
    doreccion a donde apuntan las ramas del nodo (izquierda y direcha).'''
    def __init__(self, simbolo, frecuencia):
        self.simbolo     = simbolo
        self.frecuencia  = frecuencia
        self.r_derecha   = None
        self.r_izquierda = None
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
        menos significativos al inicio de la lisa, agreagmos estos 2 nodos como 
        punteros Izquierda y derecha de un nuevo nodo(NEW_NODO), eliminamos los 
        2 nodos para volver a ordenar la lista y obtener los siguientes 2 nodos 
        menos signififcativos; terminamos al tener un solo nodo, ya que será la 
        raiz del arbol de Huffman.'''
        ARBOL.sort(key=lambda x: x.frcuencia)
        PATH_IZQ = ARBOL.pop(0)                                             # Copia de Arbol que gurda el path izquierdo.
        PATH_DER = ARBOL.pop(0)                                             # Copia de Arbol que gurda el path derecho.       
        
        NEW_NODO = NODO(None, PATH_IZQ.frecuencia + PATH_DER,frecuencia)
        NEW_NODO.r_izquierda = PATH_IZQ
        NEW_NODO.r_derecha   = PATH_DER
        
        ARBOL.append(NEW_NODO)

    return ARBOL[0]                                                         # Raiz del arbol de Huffman.
# ---------------------------------------------------------
