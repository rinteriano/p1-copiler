from graphviz import Digraph


def dibujar_arbol(arbol, dot=None, parent=None):
    if dot is None:
        dot = Digraph()

    if isinstance(arbol, tuple):
        # Crear un nodo para el elemento actual
        node = str(id(arbol))
        dot.node(node, arbol[0])  # Etiqueta del nodo (arbol[0])
        if parent:
            dot.edge(parent, node)  # Conectar con el nodo padre

        # Dibujar los hijos recursivamente si existen
        for hijo in arbol[1:]:
            dibujar_arbol(hijo, dot, node)
    elif isinstance(arbol, list):
        # Iterar por la lista y dibujar cada elemento
        for elem in arbol:
            dibujar_arbol(elem, dot, parent)
    else:
        # Dibujar nodos hoja
        node = str(id(arbol))
        dot.node(node, str(arbol))
        if parent:
            dot.edge(parent, node)

    return dot
