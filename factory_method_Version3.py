from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass

class Coche(Vehiculo):
    def acelerar(self):
        return "El coche acelera en carretera"

class Motocicleta(Vehiculo):
    def acelerar(self):
        return "La moto acelera rápidamente"

class FabricaVehiculos(ABC):
    @abstractmethod
    def crear_vehiculo(self):
        pass

class FabricaCoches(FabricaVehiculos):
    def crear_vehiculo(self):
        return Coche()

class FabricaMotocicletas(FabricaVehiculos):
    def crear_vehiculo(self):
        return Motocicleta()

# Uso
fabrica_coches = FabricaCoches()
vehiculo = fabrica_coches.crear_vehiculo()
print(vehiculo.acelerar())