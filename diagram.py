from graphviz import Digraph

def dibujar_arbol(arbol, dot=None, parent=None):
    """
    Dibuja el árbol sintáctico de manera jerárquica sin reutilizar nodos
    """
    if dot is None:
        dot = Digraph(format='png')

    if isinstance(arbol, tuple):
        # Crear un nodo único para el elemento actual
        node = f"{parent or 'root'}_{arbol[0]}_{id(arbol)}"
        dot.node(node, arbol[0])  # Etiqueta del nodo (arbol[0])
        if parent:
            dot.edge(parent, node)  # Conectar con el nodo padre

        # Dibujar los hijos recursivamente si existen
        for hijo in arbol[1:]:
            dibujar_arbol(hijo, dot, node)
    elif isinstance(arbol, list):
        # Iterar por la lista y dibujar cada elemento
        for index, elem in enumerate(arbol):
            child_name = f"{parent}_list_{index}"
            dibujar_arbol(elem, dot, parent)
    else:
        # Dibujar nodos hoja
        node = f"{parent or 'root'}_leaf_{id(arbol)}"
        dot.node(node, str(arbol))
        if parent:
            dot.edge(parent, node)

    return dot