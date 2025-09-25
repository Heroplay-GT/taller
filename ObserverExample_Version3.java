import java.util.ArrayList;
import java.util.List;

// Observer
interface Observer {
    void actualizar(String mensaje);
}

// Subject
interface Subject {
    void agregarObserver(Observer observer);
    void removerObserver(Observer observer);
    void notificar();
}

// Subject concreto
class CanalNoticias implements Subject {
    private List<Observer> observers;
    private String ultimaNoticia;
    
    public CanalNoticias() {
        this.observers = new ArrayList<>();
    }
    
    @Override
    public void agregarObserver(Observer observer) {
        observers.add(observer);
    }
    
    @Override
    public void removerObserver(Observer observer) {
        observers.remove(observer);
    }
    
    @Override
    public void notificar() {
        for (Observer observer : observers) {
            observer.actualizar(ultimaNoticia);
        }
    }
    
    public void setNoticia(String noticia) {
        this.ultimaNoticia = noticia;
        notificar();
    }
}

// Observer concreto
class Suscriptor implements Observer {
    private String nombre;
    
    public Suscriptor(String nombre) {
        this.nombre = nombre;
    }
    
    @Override
    public void actualizar(String mensaje) {
        System.out.println(nombre + " recibió noticia: " + mensaje);
    }
}

public class ObserverExample {
    public static void main(String[] args) {
        CanalNoticias canal = new CanalNoticias();
        
        Suscriptor suscriptor1 = new Suscriptor("Juan");
        Suscriptor suscriptor2 = new Suscriptor("María");
        Suscriptor suscriptor3 = new Suscriptor("Pedro");
        
        canal.agregarObserver(suscriptor1);
        canal.agregarObserver(suscriptor2);
        canal.agregarObserver(suscriptor3);
        
        canal.setNoticia("¡Nueva tecnología lanzada!");
        System.out.println();
        
        canal.removerObserver(suscriptor2);
        canal.setNoticia("¡Actualización importante!");
    }
}