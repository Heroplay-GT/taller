from abc import ABC, abstractmethod
import time

class ServicioInternet(ABC):
    @abstractmethod
    def conectar(self, sitio_web):
        pass

class ServicioInternetReal(ServicioInternet):
    def conectar(self, sitio_web):
        time.sleep(0.1)  # Simula latencia
        return f"Conectando a {sitio_web}..."

class ProxyInternet(ServicioInternet):
    def __init__(self):
        self.servicio_real = ServicioInternetReal()
        self.sitios_bloqueados = ["facebook.com", "instagram.com"]
        self.cache = {}
    
    def conectar(self, sitio_web):
        if sitio_web in self.sitios_bloqueados:
            return f"Acceso denegado a {sitio_web}"
        
        if sitio_web in self.cache:
            return f"Cache: Conectando a {sitio_web}..."
        
        resultado = self.servicio_real.conectar(sitio_web)
        self.cache[sitio_web] = resultado
        return resultado

class ProxyBanco:
    def __init__(self, cuenta_real):
        self.cuenta_real = cuenta_real
        self.intentos_fallidos = 0
        self.bloqueado = False
    
    def verificar_acceso(self, pin):
        if self.bloqueado:
            return False
        
        if pin == "1234":
            self.intentos_fallidos = 0
            return True
        else:
            self.intentos_fallidos += 1
            if self.intentos_fallidos >= 3:
                self.bloqueado = True
            return False
    
    def consultar_saldo(self, pin):
        if self.verificar_acceso(pin):
            return self.cuenta_real.consultar_saldo()
        return "Acceso denegado"

class CuentaBanco:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def consultar_saldo(self):
        return f"Saldo: ${self.saldo}"

# Uso
proxy_internet = ProxyInternet()
print(proxy_internet.conectar("google.com"))
print(proxy_internet.conectar("facebook.com"))
print(proxy_internet.conectar("google.com"))  # Desde cache

cuenta = CuentaBanco(1000)
proxy_banco = ProxyBanco(cuenta)
print(proxy_banco.consultar_saldo("1234"))
print(proxy_banco.consultar_saldo("0000"))