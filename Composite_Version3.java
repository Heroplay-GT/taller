import java.util.ArrayList;
import java.util.List;

// Componente
abstract class FileSystemComponent {
    protected String name;
    
    public FileSystemComponent(String name) {
        this.name = name;
    }
    
    public abstract void display(int depth);
    public abstract int getSize();
    
    // Métodos por defecto para operaciones de composite
    public void add(FileSystemComponent component) {
        throw new UnsupportedOperationException();
    }
    
    public void remove(FileSystemComponent component) {
        throw new UnsupportedOperationException();
    }
}

// Hoja
class File extends FileSystemComponent {
    private int size;
    
    public File(String name, int size) {
        super(name);
        this.size = size;
    }
    
    @Override
    public void display(int depth) {
        StringBuilder indent = new StringBuilder();
        for (int i = 0; i < depth; i++) {
            indent.append("  ");
        }
        System.out.println(indent + "- " + name + " (" + size + " KB)");
    }
    
    @Override
    public int getSize() {
        return size;
    }
}

// Composite
class Directory extends FileSystemComponent {
    private List<FileSystemComponent> children = new ArrayList<>();
    
    public Directory(String name) {
        super(name);
    }
    
    @Override
    public void add(FileSystemComponent component) {
        children.add(component);
    }
    
    @Override
    public void remove(FileSystemComponent component) {
        children.remove(component);
    }
    
    @Override
    public void display(int depth) {
        StringBuilder indent = new StringBuilder();
        for (int i = 0; i < depth; i++) {
            indent.append("  ");
        }
        System.out.println(indent + "+ " + name + "/");
        
        for (FileSystemComponent child : children) {
            child.display(depth + 1);
        }
    }
    
    @Override
    public int getSize() {
        int totalSize = 0;
        for (FileSystemComponent child : children) {
            totalSize += child.getSize();
        }
        return totalSize;
    }
}

// Cliente
public class Composite {
    public static void main(String[] args) {
        // Crear estructura de archivos
        Directory root = new Directory("root");
        Directory documents = new Directory("documents");
        Directory pictures = new Directory("pictures");
        
        File file1 = new File("document1.txt", 10);
        File file2 = new File("document2.pdf", 25);
        File file3 = new File("photo1.jpg", 300);
        File file4 = new File("photo2.png", 450);
        
        // Construir jerarquía
        root.add(documents);
        root.add(pictures);
        documents.add(file1);
        documents.add(file2);
        pictures.add(file3);
        pictures.add(file4);
        
        // Mostrar estructura
        root.display(0);
        System.out.println("Total size: " + root.getSize() + " KB");
    }
}