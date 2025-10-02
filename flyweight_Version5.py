class TipoCaracter:
    def __init__(self, letra, fuente, tamaño):
        self.letra = letra
        self.fuente = fuente
        self.tamaño = tamaño
    
    def mostrar(self, posicion_x, posicion_y):
        return f"'{self.letra}' ({self.fuente}, {self.tamaño}pt) en ({posicion_x}, {posicion_y})"

class FabricaTiposCaracter:
    _tipos_caracter = {}
    
    @classmethod
    def obtener_tipo_caracter(cls, letra, fuente, tamaño):
        clave = f"{letra}_{fuente}_{tamaño}"
        if clave not in cls._tipos_caracter:
            cls._tipos_caracter[clave] = TipoCaracter(letra, fuente, tamaño)
            print(f"Creando nuevo tipo de carácter: {clave}")
        return cls._tipos_caracter[clave]
    
    @classmethod
    def obtener_total_tipos(cls):
        return len(cls._tipos_caracter)

class Caracter:
    def __init__(self, letra, fuente, tamaño, posicion_x, posicion_y):
        self.tipo_caracter = FabricaTiposCaracter.obtener_tipo_caracter(letra, fuente, tamaño)
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
    
    def mostrar(self):
        return self.tipo_caracter.mostrar(self.posicion_x, self.posicion_y)

class EditorTexto:
    def __init__(self):
        self.caracteres = []
    
    def escribir_texto(self, texto, fuente="Arial", tamaño=12):
        x, y = 0, 0
        for letra in texto:
            if letra == ' ':
                x += 10
            else:
                caracter = Caracter(letra, fuente, tamaño, x, y)
                self.caracteres.append(caracter)
                x += 10
    
    def mostrar_documento(self):
        resultado = []
        for caracter in self.caracteres:
            resultado.append(caracter.mostrar())
        return "\n".join(resultado)

# Uso
editor = EditorTexto()
editor.escribir_texto("Hola", "Arial", 12)
editor.escribir_texto("Mundo", "Arial", 12)
print(editor.mostrar_documento())
print(f"Tipos de carácter creados: {FabricaTiposCaracter.obtener_total_tipos()}")