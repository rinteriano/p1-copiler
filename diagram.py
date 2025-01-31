from graphviz import Digraph

def dibujar_arbol(arbol, dot=None, parent=None):
    """
    Dibuja el árbol sintáctico de manera jerárquica.
    """
    if dot is None:
        dot = Digraph(format='png')
        dot.attr(rankdir="TB")  # Dirección del árbol (de arriba hacia abajo)

    if isinstance(arbol, tuple):
        node = f"{id(arbol)}"  # Identificador único para el nodo
        label = arbol[0]  # Primera parte de la tupla es la etiqueta
        dot.node(node, label)  # Crear nodo con la etiqueta

        if parent:
            dot.edge(parent, node)  # Conectar con el nodo padre

        for hijo in arbol[1:]:
            dibujar_arbol(hijo, dot, node)
    elif isinstance(arbol, list):
        for elem in arbol:
            dibujar_arbol(elem, dot, parent)
    else:
        node = f"{id(arbol)}"
        dot.node(node, str(arbol))  # Nodos hoja
        if parent:
            dot.edge(parent, node)

    return dot
