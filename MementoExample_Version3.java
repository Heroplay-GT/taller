import java.util.ArrayList;
import java.util.List;

// Memento
class MementoTexto {
    private final String estado;
    
    public MementoTexto(String estado) {
        this.estado = estado;
    }
    
    public String getEstado() {
        return estado;
    }
}

// Originador
class EditorTexto {
    private String contenido;
    
    public void escribir(String texto) {
        this.contenido = texto;
    }
    
    public String getContenido() {
        return contenido;
    }
    
    public MementoTexto guardar() {
        return new MementoTexto(contenido);
    }
    
    public void restaurar(MementoTexto memento) {
        this.contenido = memento.getEstado();
    }
}

// Cuidador
class HistorialEditor {
    private List<MementoTexto> historial = new ArrayList<>();
    
    public void guardar(EditorTexto editor) {
        historial.add(editor.guardar());
    }
    
    public void deshacer(EditorTexto editor) {
        if (!historial.isEmpty()) {
            MementoTexto ultimoEstado = historial.remove(historial.size() - 1);
            editor.restaurar(ultimoEstado);
        }
    }
}

public class MementoExample {
    public static void main(String[] args) {
        EditorTexto editor = new EditorTexto();
        HistorialEditor historial = new HistorialEditor();
        
        editor.escribir("Primera línea");
        historial.guardar(editor);
        System.out.println("Estado 1: " + editor.getContenido());
        
        editor.escribir("Primera línea\nSegunda línea");
        historial.guardar(editor);
        System.out.println("Estado 2: " + editor.getContenido());
        
        editor.escribir("Primera línea\nSegunda línea\nTercera línea");
        System.out.println("Estado 3: " + editor.getContenido());
        
        historial.deshacer(editor);
        System.out.println("Después de deshacer: " + editor.getContenido());
        
        historial.deshacer(editor);
        System.out.println("Después de deshacer: " + editor.getContenido());
    }
}