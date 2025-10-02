from abc import ABC, abstractmethod

class EstadoReproductor(ABC):
    @abstractmethod
    def reproducir(self, contexto):
        pass
    
    @abstractmethod
    def pausar(self, contexto):
        pass
    
    @abstractmethod
    def parar(self, contexto):
        pass

class EstadoParado(EstadoReproductor):
    def reproducir(self, contexto):
        contexto.cambiar_estado(EstadoReproduciendo())
        return "Comenzando reproducción"
    
    def pausar(self, contexto):
        return "No se puede pausar, el reproductor está parado"
    
    def parar(self, contexto):
        return "Ya está parado"

class EstadoReproduciendo(EstadoReproductor):
    def reproducir(self, contexto):
        return "Ya está reproduciendo"
    
    def pausar(self, contexto):
        contexto.cambiar_estado(EstadoPausado())
        return "Reproducción pausada"
    
    def parar(self, contexto):
        contexto.cambiar_estado(EstadoParado())
        return "Reproducción detenida"

class EstadoPausado(EstadoReproductor):
    def reproducir(self, contexto):
        contexto.cambiar_estado(EstadoReproduciendo())
        return "Continuando reproducción"
    
    def pausar(self, contexto):
        return "Ya está pausado"
    
    def parar(self, contexto):
        contexto.cambiar_estado(EstadoParado())
        return "Reproducción detenida"

class ReproductorMusica:
    def __init__(self):
        self.estado = EstadoParado()
        self.cancion_actual = ""
    
    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
    
    def reproducir(self, cancion=None):
        if cancion:
            self.cancion_actual = cancion
        resultado = self.estado.reproducir(self)
        return f"{resultado} - {self.cancion_actual}"
    
    def pausar(self):
        return self.estado.pausar(self)
    
    def parar(self):
        return self.estado.parar(self)
    
    def obtener_estado(self):
        return type(self.estado).__name__

# Uso
reproductor = ReproductorMusica()
print(f"Estado inicial: {reproductor.obtener_estado()}")

print(reproductor.reproducir("Bohemian Rhapsody"))
print(f"Estado actual: {reproductor.obtener_estado()}")

print(reproductor.pausar())
print(f"Estado actual: {reproductor.obtener_estado()}")

print(reproductor.reproducir())
print(f"Estado actual: {reproductor.obtener_estado()}")

print(reproductor.parar())
print(f"Estado actual: {reproductor.obtener_estado()}")