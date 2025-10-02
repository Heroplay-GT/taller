class ReproductorMusica:
    def reproducir_mp3(self, archivo):
        return f"Reproduciendo MP3: {archivo}"

class ReproductorVideo:
    def reproducir_mp4(self, archivo):
        return f"Reproduciendo MP4: {archivo}"
    
    def reproducir_avi(self, archivo):
        return f"Reproduciendo AVI: {archivo}"

class AdaptadorReproductor:
    def __init__(self, reproductor_video):
        self.reproductor_video = reproductor_video
    
    def reproducir(self, tipo_archivo, archivo):
        if tipo_archivo == "mp4":
            return self.reproductor_video.reproducir_mp4(archivo)
        elif tipo_archivo == "avi":
            return self.reproductor_video.reproducir_avi(archivo)

class ReproductorUniversal:
    def __init__(self):
        self.reproductor_musica = ReproductorMusica()
        self.adaptador = AdaptadorReproductor(ReproductorVideo())
    
    def reproducir(self, tipo_archivo, archivo):
        if tipo_archivo == "mp3":
            return self.reproductor_musica.reproducir_mp3(archivo)
        else:
            return self.adaptador.reproducir(tipo_archivo, archivo)

# Uso
reproductor = ReproductorUniversal()
print(reproductor.reproducir("mp3", "cancion.mp3"))
print(reproductor.reproducir("mp4", "video.mp4"))