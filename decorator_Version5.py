from abc import ABC, abstractmethod

class ComponenteTexto(ABC):
    @abstractmethod
    def obtener_texto(self):
        pass

class TextoSimple(ComponenteTexto):
    def __init__(self, texto):
        self.texto = texto
    
    def obtener_texto(self):
        return self.texto

class DecoradorTexto(ComponenteTexto):
    def __init__(self, componente):
        self.componente = componente

class TextoNegrita(DecoradorTexto):
    def obtener_texto(self):
        return f"**{self.componente.obtener_texto()}**"

class TextoCursiva(DecoradorTexto):
    def obtener_texto(self):
        return f"*{self.componente.obtener_texto()}*"

class TextoSubrayado(DecoradorTexto):
    def obtener_texto(self):
        return f"__{self.componente.obtener_texto()}__"

# Uso
texto_base = TextoSimple("Hola Mundo")
print(texto_base.obtener_texto())

texto_negrita = TextoNegrita(texto_base)
print(texto_negrita.obtener_texto())

texto_completo = TextoSubrayado(TextoCursiva(TextoNegrita(texto_base)))
print(texto_completo.obtener_texto())