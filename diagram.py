from graphviz import Digraph

def dibujar_arbol(arbol, dot=None, parent=None):
    if dot is None:
        dot = Digraph()
    if isinstance(arbol, tuple):
        node = str(id(arbol))
        dot.node(node, arbol[0])
        if parent:
            dot.edge(parent, node)
        dibujar_arbol(arbol[1], dot, node)
        dibujar_arbol(arbol[2], dot, node)
    else:
        node = str(id(arbol))
        dot.node(node, str(arbol))
        if parent:
            dot.edge(parent, node)
    return dot
