from abc import ABC, abstractmethod

class Boton(ABC):
    @abstractmethod
    def pintar(self):
        pass

class Ventana(ABC):
    @abstractmethod
    def mostrar(self):
        pass

class BotonWindows(Boton):
    def pintar(self):
        return "Botón estilo Windows"

class VentanaWindows(Ventana):
    def mostrar(self):
        return "Ventana estilo Windows"

class BotonMac(Boton):
    def pintar(self):
        return "Botón estilo Mac"

class VentanaMac(Ventana):
    def mostrar(self):
        return "Ventana estilo Mac"

class FabricaGUI(ABC):
    @abstractmethod
    def crear_boton(self):
        pass
    
    @abstractmethod
    def crear_ventana(self):
        pass

class FabricaWindows(FabricaGUI):
    def crear_boton(self):
        return BotonWindows()
    
    def crear_ventana(self):
        return VentanaWindows()

class FabricaMac(FabricaGUI):
    def crear_boton(self):
        return BotonMac()
    
    def crear_ventana(self):
        return VentanaMac()

# Uso
fabrica = FabricaWindows()
boton = fabrica.crear_boton()
ventana = fabrica.crear_ventana()
print(boton.pintar())
print(ventana.mostrar())