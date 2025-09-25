// Productos abstractos
interface Button {
    void click();
}

interface TextField {
    void type(String text);
}

// Productos concretos para Windows
class WindowsButton implements Button {
    @Override
    public void click() {
        System.out.println("Windows button clicked");
    }
}

class WindowsTextField implements TextField {
    @Override
    public void type(String text) {
        System.out.println("Typing in Windows text field: " + text);
    }
}

// Productos concretos para Mac
class MacButton implements Button {
    @Override
    public void click() {
        System.out.println("Mac button clicked");
    }
}

class MacTextField implements TextField {
    @Override
    public void type(String text) {
        System.out.println("Typing in Mac text field: " + text);
    }
}

// Factory abstracta
interface UIFactory {
    Button createButton();
    TextField createTextField();
}

// Factories concretas
class WindowsFactory implements UIFactory {
    @Override
    public Button createButton() {
        return new WindowsButton();
    }
    
    @Override
    public TextField createTextField() {
        return new WindowsTextField();
    }
}

class MacFactory implements UIFactory {
    @Override
    public Button createButton() {
        return new MacButton();
    }
    
    @Override
    public TextField createTextField() {
        return new MacTextField();
    }
}

// Cliente
public class AbstractFactory {
    public static void main(String[] args) {
        UIFactory factory = new WindowsFactory();
        Button button = factory.createButton();
        TextField textField = factory.createTextField();
        
        button.click();
        textField.type("Hello World");
    }
}