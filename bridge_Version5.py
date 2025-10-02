from abc import ABC, abstractmethod

class ImplementacionDibujado(ABC):
    @abstractmethod
    def dibujar_circulo(self, x, y, radio):
        pass

class DibujadoWindows(ImplementacionDibujado):
    def dibujar_circulo(self, x, y, radio):
        return f"Dibujando círculo en Windows en ({x}, {y}) con radio {radio}"

class DibujadoLinux(ImplementacionDibujado):
    def dibujar_circulo(self, x, y, radio):
        return f"Dibujando círculo en Linux en ({x}, {y}) con radio {radio}"

class Forma:
    def __init__(self, implementacion):
        self.implementacion = implementacion

class Circulo(Forma):
    def __init__(self, x, y, radio, implementacion):
        super().__init__(implementacion)
        self.x = x
        self.y = y
        self.radio = radio
    
    def dibujar(self):
        return self.implementacion.dibujar_circulo(self.x, self.y, self.radio)
    
    def redimensionar(self, factor):
        self.radio *= factor

# Uso
dibujado_windows = DibujadoWindows()
circulo = Circulo(10, 10, 5, dibujado_windows)
print(circulo.dibujar())

dibujado_linux = DibujadoLinux()
circulo.implementacion = dibujado_linux
print(circulo.dibujar())