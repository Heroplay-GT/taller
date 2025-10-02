from abc import ABC, abstractmethod

class Observador(ABC):
    @abstractmethod
    def actualizar(self, temperatura, humedad, presion):
        pass

class SujetoClima:
    def __init__(self):
        self.observadores = []
        self.temperatura = 0
        self.humedad = 0
        self.presion = 0
    
    def agregar_observador(self, observador):
        self.observadores.append(observador)
    
    def remover_observador(self, observador):
        self.observadores.remove(observador)
    
    def notificar_observadores(self):
        for observador in self.observadores:
            observador.actualizar(self.temperatura, self.humedad, self.presion)
    
    def establecer_mediciones(self, temperatura, humedad, presion):
        self.temperatura = temperatura
        self.humedad = humedad
        self.presion = presion
        self.notificar_observadores()

class PantallaActual(Observador):
    def actualizar(self, temperatura, humedad, presion):
        print(f"Pantalla Actual: {temperatura}°C, {humedad}% humedad, {presion} hPa")

class PantallaEstadisticas(Observador):
    def __init__(self):
        self.temperaturas = []
    
    def actualizar(self, temperatura, humedad, presion):
        self.temperaturas.append(temperatura)
        promedio = sum(self.temperaturas) / len(self.temperaturas)
        print(f"Estadísticas: Temp. promedio: {promedio:.1f}°C")

class AlertaClima(Observador):
    def actualizar(self, temperatura, humedad, presion):
        if temperatura > 30:
            print("¡ALERTA! Temperatura muy alta")
        if temperatura < 0:
            print("¡ALERTA! Temperatura bajo cero")
        if humedad > 80:
            print("¡ALERTA! Humedad muy alta")

# Uso
estacion_clima = SujetoClima()

pantalla_actual = PantallaActual()
pantalla_stats = PantallaEstadisticas()
alerta = AlertaClima()

estacion_clima.agregar_observador(pantalla_actual)
estacion_clima.agregar_observador(pantalla_stats)
estacion_clima.agregar_observador(alerta)

estacion_clima.establecer_mediciones(25, 65, 1013)
print()
estacion_clima.establecer_mediciones(32, 85, 1008)