from abc import ABC, abstractmethod

class Iterador(ABC):
    @abstractmethod
    def siguiente(self):
        pass
    
    @abstractmethod
    def tiene_siguiente(self):
        pass

class ColeccionLibros:
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def crear_iterador(self):
        return IteradorLibros(self.libros)

class IteradorLibros(Iterador):
    def __init__(self, libros):
        self.libros = libros
        self.indice = 0
    
    def siguiente(self):
        if self.tiene_siguiente():
            libro = self.libros[self.indice]
            self.indice += 1
            return libro
        return None
    
    def tiene_siguiente(self):
        return self.indice < len(self.libros)

class ColeccionCircular:
    def __init__(self, elementos):
        self.elementos = elementos
    
    def crear_iterador(self):
        return IteradorCircular(self.elementos)

class IteradorCircular(Iterador):
    def __init__(self, elementos):
        self.elementos = elementos
        self.indice = 0
        self.contador = 0
    
    def siguiente(self):
        if self.tiene_siguiente():
            elemento = self.elementos[self.indice]
            self.indice = (self.indice + 1) % len(self.elementos)
            self.contador += 1
            return elemento
        return None
    
    def tiene_siguiente(self):
        return self.contador < len(self.elementos) * 2  # Dar dos vueltas

# Uso
biblioteca = ColeccionLibros()
biblioteca.agregar_libro("El Quijote")
biblioteca.agregar_libro("Cien años de soledad")
biblioteca.agregar_libro("1984")

iterador = biblioteca.crear_iterador()
while iterador.tiene_siguiente():
    print(iterador.siguiente())

print("\nIterador circular:")
coleccion_circular = ColeccionCircular(["A", "B", "C"])
iterador_circular = coleccion_circular.crear_iterador()
for i in range(8):
    if iterador_circular.tiene_siguiente():
        print(iterador_circular.siguiente())