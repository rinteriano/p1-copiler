from graphviz import Digraph

def dibujar_arbol_completo(arbol, dot=None, parent=None):

    if dot is None:
        dot = Digraph(format='png')
        dot.attr(rankdir="TB")  # Dirección del árbol (de arriba hacia abajo)

    # Generar un identificador único para cada nodo
    current_node = f"{id(arbol)}_{len(dot.body)}"

    if isinstance(arbol, tuple):
        label = arbol[0]  # Primera parte de la tupla es la etiqueta
        dot.node(current_node, label)  # Crear nodo con la etiqueta principal

        if parent:
            dot.edge(parent, current_node)  # Conectar con el nodo padre

        for hijo in arbol[1:]:
            dibujar_arbol_completo(hijo, dot, current_node)  # Llamada recursiva para hijos

    elif isinstance(arbol, list):
        for elem in arbol:
            dibujar_arbol_completo(elem, dot, parent)

    elif isinstance(arbol, str):
        # Crear un nodo único para cada cadena
        node = f"{current_node}_{arbol}"  # Nodo único con identificador + valor
        dot.node(node, arbol)  # Crear nodo con el valor de la cadena completa
        if parent:
            dot.edge(parent, node)  # Conectar con el nodo padre

    else:
        # Crear nodos para valores atómicos (números, identificadores, etc.)
        dot.node(current_node, str(arbol))
        if parent:
            dot.edge(parent, current_node)

    return dot


def agregar_subdiagramas(dot, declaraciones):
    """
    Agrega subdiagramas para declaraciones y asignaciones al diagrama principal.
    """
    with dot.subgraph(name='cluster_declaraciones') as sub:
        sub.attr(label="Declaraciones y Asignaciones", style='filled', color='lightgrey')
        for declaracion in declaraciones:
            # Cada declaración también tiene un nodo único
            node = f"{id(declaracion)}_{len(dot.body)}"
            sub.node(node, declaracion)
    return dot
