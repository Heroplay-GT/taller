// Subject interface
interface Image {
    void display();
}

// Real subject
class RealImage implements Image {
    private String filename;
    
    public RealImage(String filename) {
        this.filename = filename;
        loadFromDisk();
    }
    
    private void loadFromDisk() {
        System.out.println("Loading image: " + filename + " from disk...");
        // Simular carga costosa
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        System.out.println("Image loaded: " + filename);
    }
    
    @Override
    public void display() {
        System.out.println("Displaying image: " + filename);
    }
}

// Proxy
class ProxyImage implements Image {
    private RealImage realImage;
    private String filename;
    private boolean hasAccess;
    
    public ProxyImage(String filename, boolean hasAccess) {
        this.filename = filename;
        this.hasAccess = hasAccess;
    }
    
    @Override
    public void display() {
        if (!hasAccess) {
            System.out.println("Access denied: You don't have permission to view " + filename);
            return;
        }
        
        if (realImage == null) {
            realImage = new RealImage(filename);
        }
        realImage.display();
    }
}

// Cliente
public class Proxy {
    public static void main(String[] args) {
        System.out.println("=== Testing with access ===");
        Image image1 = new ProxyImage("photo1.jpg", true);
        image1.display(); // Carga la imagen
        image1.display(); // No vuelve a cargar
        
        System.out.println("\n=== Testing without access ===");
        Image image2 = new ProxyImage("secret.jpg", false);
        image2.display(); // Acceso denegado
        
        System.out.println("\n=== Testing lazy loading ===");
        Image image3 = new ProxyImage("photo2.jpg", true);
        System.out.println("Proxy created, but image not loaded yet");
        image3.display(); // Ahora se carga la imagen
    }
}