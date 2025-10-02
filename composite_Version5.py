from abc import ABC, abstractmethod

class ComponenteArchivo(ABC):
    @abstractmethod
    def mostrar(self, indentacion=0):
        pass
    
    @abstractmethod
    def obtener_tamaño(self):
        pass

class Archivo(ComponenteArchivo):
    def __init__(self, nombre, tamaño):
        self.nombre = nombre
        self.tamaño = tamaño
    
    def mostrar(self, indentacion=0):
        return " " * indentacion + f"Archivo: {self.nombre} ({self.tamaño}KB)"
    
    def obtener_tamaño(self):
        return self.tamaño

class Carpeta(ComponenteArchivo):
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []
    
    def agregar(self, elemento):
        self.elementos.append(elemento)
    
    def remover(self, elemento):
        self.elementos.remove(elemento)
    
    def mostrar(self, indentacion=0):
        resultado = " " * indentacion + f"Carpeta: {self.nombre}\n"
        for elemento in self.elementos:
            resultado += elemento.mostrar(indentacion + 2) + "\n"
        return resultado.rstrip()
    
    def obtener_tamaño(self):
        return sum(elemento.obtener_tamaño() for elemento in self.elementos)

# Uso
archivo1 = Archivo("documento.txt", 10)
archivo2 = Archivo("imagen.jpg", 500)

carpeta1 = Carpeta("Documentos")
carpeta1.agregar(archivo1)

carpeta_raiz = Carpeta("Mi PC")
carpeta_raiz.agregar(carpeta1)
carpeta_raiz.agregar(archivo2)

print(carpeta_raiz.mostrar())
print(f"Tamaño total: {carpeta_raiz.obtener_tamaño()}KB")