from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if self.nombre == other.nombre:
            return True
        else:
            return False


class Conjunto:

    contador = 0

    def __init__(self, nombre_del_conjunto: str):
        self.lista_de_objetos: [Elemento] = []
        self.nombre: str = nombre_del_conjunto
        self.__class__.contador += 1
        self.

elemento_1 = Elemento("Emanuel")


elemento_2 = Elemento("emanuel")

comparacion: bool = elemento_1 == elemento_2

print(comparacion)

conjunto_1 = Conjunto("Emanuel")
conjunto_2 = Conjunto("Emanuel")
conjunto_3 = Conjunto("Emanuel")
conjunto_4 = Conjunto("Emanuel")

print(conjunto_4.contador)