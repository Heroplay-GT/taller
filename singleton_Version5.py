class BaseDatos:
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.conexion = "Conectado a la base de datos"
        return cls._instancia
    
    def consultar(self, sql):
        return f"Ejecutando: {sql}"

class ConfiguracionApp:
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.configuraciones = {"tema": "oscuro", "idioma": "español"}
        return cls._instancia
    
    def obtener_config(self, clave):
        return self.configuraciones.get(clave)
    
    def establecer_config(self, clave, valor):
        self.configuraciones[clave] = valor

# Uso
db1 = BaseDatos()
db2 = BaseDatos()
print(db1 is db2)  # True

config1 = ConfiguracionApp()
config2 = ConfiguracionApp()
print(config1 is config2)  # True
print(config1.obtener_config("tema"))