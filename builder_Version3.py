class Casa:
    def __init__(self):
        self.partes = []
    
    def agregar_parte(self, parte):
        self.partes.append(parte)
    
    def mostrar(self):
        return f"Casa con: {', '.join(self.partes)}"

class ConstructorCasa:
    def __init__(self):
        self.casa = Casa()
    
    def construir_cimientos(self):
        self.casa.agregar_parte("cimientos")
        return self
    
    def construir_paredes(self):
        self.casa.agregar_parte("paredes")
        return self
    
    def construir_techo(self):
        self.casa.agregar_parte("techo")
        return self
    
    def construir_jardin(self):
        self.casa.agregar_parte("jardín")
        return self
    
    def obtener_casa(self):
        return self.casa

class Director:
    def __init__(self, constructor):
        self.constructor = constructor
    
    def construir_casa_basica(self):
        return (self.constructor
                .construir_cimientos()
                .construir_paredes()
                .construir_techo()
                .obtener_casa())
    
    def construir_casa_completa(self):
        return (self.constructor
                .construir_cimientos()
                .construir_paredes()
                .construir_techo()
                .construir_jardin()
                .obtener_casa())

# Uso
constructor = ConstructorCasa()
director = Director(constructor)
casa = director.construir_casa_completa()
print(casa.mostrar())