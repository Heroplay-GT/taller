from abc import ABC, abstractmethod

class Mediador(ABC):
    @abstractmethod
    def notificar(self, remitente, evento):
        pass

class MediadorDialogo(Mediador):
    def __init__(self):
        self.boton_ok = None
        self.boton_cancelar = None
        self.campo_texto = None
        self.checkbox = None
    
    def configurar_componentes(self, boton_ok, boton_cancelar, campo_texto, checkbox):
        self.boton_ok = boton_ok
        self.boton_cancelar = boton_cancelar
        self.campo_texto = campo_texto
        self.checkbox = checkbox
    
    def notificar(self, remitente, evento):
        if remitente == self.checkbox and evento == "check":
            if self.checkbox.marcado:
                self.campo_texto.habilitar()
                self.boton_ok.habilitar()
            else:
                self.campo_texto.deshabilitar()
                self.boton_ok.deshabilitar()
        
        elif remitente == self.campo_texto and evento == "change":
            if self.campo_texto.texto.strip():
                self.boton_ok.habilitar()
            else:
                self.boton_ok.deshabilitar()

class ComponenteBase:
    def __init__(self, mediador):
        self.mediador = mediador

class BotonOK(ComponenteBase):
    def __init__(self, mediador):
        super().__init__(mediador)
        self.habilitado = False
    
    def habilitar(self):
        self.habilitado = True
        print("Botón OK habilitado")
    
    def deshabilitar(self):
        self.habilitado = False
        print("Botón OK deshabilitado")
    
    def click(self):
        if self.habilitado:
            return "Formulario enviado"
        return "Botón deshabilitado"

class CampoTexto(ComponenteBase):
    def __init__(self, mediador):
        super().__init__(mediador)
        self.texto = ""
        self.habilitado = False
    
    def habilitar(self):
        self.habilitado = True
        print("Campo de texto habilitado")
    
    def deshabilitar(self):
        self.habilitado = False
        print("Campo de texto deshabilitado")
    
    def cambiar_texto(self, nuevo_texto):
        if self.habilitado:
            self.texto = nuevo_texto
            self.mediador.notificar(self, "change")

class Checkbox(ComponenteBase):
    def __init__(self, mediador):
        super().__init__(mediador)
        self.marcado = False
    
    def marcar(self):
        self.marcado = True
        print("Checkbox marcado")
        self.mediador.notificar(self, "check")
    
    def desmarcar(self):
        self.marcado = False
        print("Checkbox desmarcado")
        self.mediador.notificar(self, "check")

# Uso
mediador = MediadorDialogo()
boton_ok = BotonOK(mediador)
campo_texto = CampoTexto(mediador)
checkbox = Checkbox(mediador)

mediador.configurar_componentes(boton_ok, None, campo_texto, checkbox)

checkbox.marcar()
campo_texto.cambiar_texto("Hola")
print(boton_ok.click())