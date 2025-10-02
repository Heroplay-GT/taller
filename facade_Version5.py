class SistemaAudio:
    def encender(self):
        return "Sistema de audio encendido"
    
    def configurar_volumen(self, volumen):
        return f"Volumen configurado a {volumen}"

class SistemaVideo:
    def encender(self):
        return "Sistema de video encendido"
    
    def configurar_resolucion(self, resolucion):
        return f"Resolución configurada a {resolucion}"

class SistemaLuces:
    def atenuar(self):
        return "Luces atenuadas"
    
    def encender(self):
        return "Luces encendidas"

class ReproductorDVD:
    def encender(self):
        return "Reproductor DVD encendido"
    
    def reproducir_pelicula(self, pelicula):
        return f"Reproduciendo: {pelicula}"

class FachadaCineCasa:
    def __init__(self):
        self.audio = SistemaAudio()
        self.video = SistemaVideo()
        self.luces = SistemaLuces()
        self.dvd = ReproductorDVD()
    
    def ver_pelicula(self, pelicula):
        resultados = []
        resultados.append(self.luces.atenuar())
        resultados.append(self.audio.encender())
        resultados.append(self.audio.configurar_volumen(70))
        resultados.append(self.video.encender())
        resultados.append(self.video.configurar_resolucion("1080p"))
        resultados.append(self.dvd.encender())
        resultados.append(self.dvd.reproducir_pelicula(pelicula))
        return "\n".join(resultados)
    
    def terminar_pelicula(self):
        resultados = []
        resultados.append("Terminando película...")
        resultados.append(self.luces.encender())
        return "\n".join(resultados)

# Uso
cine_casa = FachadaCineCasa()
print(cine_casa.ver_pelicula("Avengers"))