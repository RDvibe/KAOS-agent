import ast
import astunparse
import random

class ChaosAgent:

    def __init__(self, functions):
        self.functions = functions

    def deconstruct(self, function):
        # Convertimos la función en un AST
        tree = ast.parse(inspect.getsource(function))
        return tree.body[0]  # Devolvemos solo el nodo de la función

    def reconstruct(self, nodes):
        # Tomamos aleatoriamente nodos de diferentes funciones y los unimos para formar una nueva función
        new_function = ast.FunctionDef(
            name="chaos_function",
            args=nodes[0].args,  # Tomamos los argumentos de la primera función
            body=[node.body[0] for node in nodes],  # Tomamos el primer nodo de cuerpo de cada función
            decorator_list=[],
            returns=None
        )
        return astunparse.unparse(new_function)

    def create_chaos_function(self):
        # Desconstruimos las funciones en nodos de AST
        nodes = [self.deconstruct(function) for function in self.functions]
        # Mezclamos los nodos
        random.shuffle(nodes)
        # Reconstruimos una nueva función a partir de los nodos mezclados
        chaos_function = self.reconstruct(nodes)
        return chaos_function

# Ejemplo de uso
chaos_agent = ChaosAgent([function1, function2])
chaos_function = chaos_agent.create_chaos_function()
print(chaos_function)
