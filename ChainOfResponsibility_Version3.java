// Handler abstracto
abstract class SupportHandler {
    protected SupportHandler nextHandler;
    
    public void setNext(SupportHandler nextHandler) {
        this.nextHandler = nextHandler;
    }
    
    public abstract void handleRequest(String issue, int priority);
}

// Handlers concretos
class Level1Support extends SupportHandler {
    @Override
    public void handleRequest(String issue, int priority) {
        if (priority <= 1) {
            System.out.println("Level 1 Support: Handling issue - " + issue);
        } else if (nextHandler != null) {
            System.out.println("Level 1 Support: Escalating issue - " + issue);
            nextHandler.handleRequest(issue, priority);
        }
    }
}

class Level2Support extends SupportHandler {
    @Override
    public void handleRequest(String issue, int priority) {
        if (priority <= 2) {
            System.out.println("Level 2 Support: Handling issue - " + issue);
        } else if (nextHandler != null) {
            System.out.println("Level 2 Support: Escalating issue - " + issue);
            nextHandler.handleRequest(issue, priority);
        }
    }
}

class Level3Support extends SupportHandler {
    @Override
    public void handleRequest(String issue, int priority) {
        if (priority <= 3) {
            System.out.println("Level 3 Support: Handling issue - " + issue);
        } else {
            System.out.println("Level 3 Support: Cannot handle issue - " + issue + ". Needs management attention.");
        }
    }
}

// Cliente
public class ChainOfResponsibility {
    public static void main(String[] args) {
        // Crear la cadena
        SupportHandler level1 = new Level1Support();
        SupportHandler level2 = new Level2Support();
        SupportHandler level3 = new Level3Support();
        
        level1.setNext(level2);
        level2.setNext(level3);
        
        // Procesar diferentes tipos de issues
        System.out.println("=== Issue 1 (Priority 1) ===");
        level1.handleRequest("Password reset", 1);
        
        System.out.println("\n=== Issue 2 (Priority 2) ===");
        level1.handleRequest("Software installation", 2);
        
        System.out.println("\n=== Issue 3 (Priority 3) ===");
        level1.handleRequest("Server crash", 3);
        
        System.out.println("\n=== Issue 4 (Priority 4) ===");
        level1.handleRequest("Data center fire", 4);
    }
}