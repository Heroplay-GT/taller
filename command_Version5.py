from abc import ABC, abstractmethod

class Comando(ABC):
    @abstractmethod
    def ejecutar(self):
        pass
    
    @abstractmethod
    def deshacer(self):
        pass

class Luz:
    def __init__(self):
        self.encendida = False
    
    def encender(self):
        self.encendida = True
        return "Luz encendida"
    
    def apagar(self):
        self.encendida = False
        return "Luz apagada"

class ComandoEncenderLuz(Comando):
    def __init__(self, luz):
        self.luz = luz
    
    def ejecutar(self):
        return self.luz.encender()
    
    def deshacer(self):
        return self.luz.apagar()

class ComandoApagarLuz(Comando):
    def __init__(self, luz):
        self.luz = luz
    
    def ejecutar(self):
        return self.luz.apagar()
    
    def deshacer(self):
        return self.luz.encender()

class ControlRemoto:
    def __init__(self):
        self.comandos = {}
        self.ultimo_comando = None
    
    def establecer_comando(self, slot, comando):
        self.comandos[slot] = comando
    
    def presionar_boton(self, slot):
        if slot in self.comandos:
            resultado = self.comandos[slot].ejecutar()
            self.ultimo_comando = self.comandos[slot]
            return resultado
        return "Comando no configurado"
    
    def presionar_deshacer(self):
        if self.ultimo_comando:
            return self.ultimo_comando.deshacer()
        return "No hay comando para deshacer"

# Uso
luz_sala = Luz()
comando_encender = ComandoEncenderLuz(luz_sala)
comando_apagar = ComandoApagarLuz(luz_sala)

control = ControlRemoto()
control.establecer_comando(1, comando_encender)
control.establecer_comando(2, comando_apagar)

print(control.presionar_boton(1))
print(control.presionar_boton(2))
print(control.presionar_deshacer())