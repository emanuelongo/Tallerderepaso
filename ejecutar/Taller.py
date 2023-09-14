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

    conjuntos_intersectados = None
    contador = 0

    def __init__(self, nombre_del_conjunto: str):
        self.lista_de_objetos: [Elemento] = []
        self.nombre_del_conjunto: str = nombre_del_conjunto
        self.__class__.contador += 1
        self.__id = self.__class__.contador

    @property
    def id(self):
        return self.__id

    def contiene(self, objeto) -> bool:
        if objeto in self.lista_de_objetos:
            return True
        else:
            return False

    def agregar_elemento(self, objeto: Elemento):
        if objeto not in self.lista_de_objetos:
            self.lista_de_objetos.append(objeto)
        else:
            pass

    def unir(self, conjunto):
        self.lista_de_objetos.append(conjunto)

    def __add__(self, other):
        self.lista_de_objetos += other.conjunto


    @classmethod
    def intersectar(cls, conjunto_1, conjunto_2):
        conjuntos_intersectados = conjunto_1.intersection(conjunto_2)
        return conjuntos_intersectados

    def __str__(self):
        pass


elemento_1 = Elemento("Emanuel")


elemento_2 = Elemento("emanuel")

comparacion: bool = elemento_1 == elemento_2

print(comparacion)

conjunto_1 = Conjunto("Emanuel")
conjunto_2 = Conjunto("Emanuel")
conjunto_3 = Conjunto("Emanuel")
conjunto_4 = Conjunto("Emanuel")

print(conjunto_4.intersectar({"Hola", "Hola"}, {"Bolis", "Hola"}))
print(conjunto_4.id)