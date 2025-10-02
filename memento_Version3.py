class MementoEditor:
    def __init__(self, contenido, cursor_x, cursor_y):
        self.contenido = contenido
        self.cursor_x = cursor_x
        self.cursor_y = cursor_y

class EditorTexto:
    def __init__(self):
        self.contenido = ""
        self.cursor_x = 0
        self.cursor_y = 0
    
    def escribir(self, texto):
        self.contenido += texto
        self.cursor_x += len(texto)
        return f"Escribiendo: {texto}"
    
    def mover_cursor(self, x, y):
        self.cursor_x = x
        self.cursor_y = y
        return f"Cursor movido a ({x}, {y})"
    
    def crear_memento(self):
        return MementoEditor(self.contenido, self.cursor_x, self.cursor_y)
    
    def restaurar_memento(self, memento):
        self.contenido = memento.contenido
        self.cursor_x = memento.cursor_x
        self.cursor_y = memento.cursor_y
        return "Estado restaurado"
    
    def mostrar_estado(self):
        return f"Contenido: '{self.contenido}', Cursor: ({self.cursor_x}, {self.cursor_y})"

class HistorialEditor:
    def __init__(self):
        self.mementos = []
    
    def guardar(self, memento):
        self.mementos.append(memento)
        print(f"Estado guardado. Total: {len(self.mementos)}")
    
    def deshacer(self):
        if self.mementos:
            return self.mementos.pop()
        return None

# Uso
editor = EditorTexto()
historial = HistorialEditor()

print(editor.mostrar_estado())

# Guardar estado inicial
historial.guardar(editor.crear_memento())

# Hacer cambios
editor.escribir("Hola ")
editor.mover_cursor(5, 0)
print(editor.mostrar_estado())

# Guardar estado
historial.guardar(editor.crear_memento())

# Más cambios
editor.escribir("Mundo")
print(editor.mostrar_estado())

# Restaurar estado anterior
memento_anterior = historial.deshacer()
if memento_anterior:
    editor.restaurar_memento(memento_anterior)
    print("Después de deshacer:")
    print(editor.mostrar_estado())