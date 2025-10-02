import copy

class Documento:
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido
        self.imagenes = []
    
    def agregar_imagen(self, imagen):
        self.imagenes.append(imagen)
    
    def clonar(self):
        return copy.deepcopy(self)
    
    def mostrar(self):
        return f"Documento: {self.titulo}, Contenido: {self.contenido}, Imágenes: {len(self.imagenes)}"

class RegistroPrototipos:
    def __init__(self):
        self.prototipos = {}
    
    def registrar_prototipo(self, nombre, prototipo):
        self.prototipos[nombre] = prototipo
    
    def crear_documento(self, nombre):
        prototipo = self.prototipos.get(nombre)
        if prototipo:
            return prototipo.clonar()
        return None

# Uso
registro = RegistroPrototipos()

doc_plantilla = Documento("Plantilla", "Contenido base")
doc_plantilla.agregar_imagen("logo.png")
registro.registrar_prototipo("plantilla", doc_plantilla)

nuevo_doc = registro.crear_documento("plantilla")
nuevo_doc.titulo = "Nuevo Documento"
print(nuevo_doc.mostrar())