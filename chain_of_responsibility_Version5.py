from abc import ABC, abstractmethod

class ManejadorSoporte(ABC):
    def __init__(self):
        self.siguiente_manejador = None
    
    def establecer_siguiente(self, manejador):
        self.siguiente_manejador = manejador
        return manejador
    
    @abstractmethod
    def manejar(self, solicitud):
        if self.siguiente_manejador:
            return self.siguiente_manejador.manejar(solicitud)
        return None

class SoporteBasico(ManejadorSoporte):
    def manejar(self, solicitud):
        if solicitud["nivel"] == "basico":
            return f"Soporte Básico: Resolviendo {solicitud['problema']}"
        return super().manejar(solicitud)

class SoporteAvanzado(ManejadorSoporte):
    def manejar(self, solicitud):
        if solicitud["nivel"] == "avanzado":
            return f"Soporte Avanzado: Resolviendo {solicitud['problema']}"
        return super().manejar(solicitud)

class SoporteExperto(ManejadorSoporte):
    def manejar(self, solicitud):
        if solicitud["nivel"] == "experto":
            return f"Soporte Experto: Resolviendo {solicitud['problema']}"
        return super().manejar(solicitud)

# Uso
soporte_basico = SoporteBasico()
soporte_avanzado = SoporteAvanzado()
soporte_experto = SoporteExperto()

soporte_basico.establecer_siguiente(soporte_avanzado).establecer_siguiente(soporte_experto)

solicitudes = [
    {"nivel": "basico", "problema": "cambio de contraseña"},
    {"nivel": "avanzado", "problema": "problema de red"},
    {"nivel": "experto", "problema": "fallo del servidor"}
]

for solicitud in solicitudes:
    resultado = soporte_basico.manejar(solicitud)
    print(resultado)