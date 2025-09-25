// Producto
class Pizza {
    private String dough;
    private String sauce;
    private String topping;
    
    public void setDough(String dough) { this.dough = dough; }
    public void setSauce(String sauce) { this.sauce = sauce; }
    public void setTopping(String topping) { this.topping = topping; }
    
    @Override
    public String toString() {
        return "Pizza with " + dough + " dough, " + sauce + " sauce, and " + topping + " topping";
    }
}

// Builder abstracto
abstract class PizzaBuilder {
    protected Pizza pizza;
    
    public Pizza getPizza() { return pizza; }
    public void createNewPizza() { pizza = new Pizza(); }
    
    public abstract void buildDough();
    public abstract void buildSauce();
    public abstract void buildTopping();
}

// Builder concreto
class MargheritaPizzaBuilder extends PizzaBuilder {
    @Override
    public void buildDough() {
        pizza.setDough("thin");
    }
    
    @Override
    public void buildSauce() {
        pizza.setSauce("tomato");
    }
    
    @Override
    public void buildTopping() {
        pizza.setTopping("mozzarella");
    }
}

class PepperoniPizzaBuilder extends PizzaBuilder {
    @Override
    public void buildDough() {
        pizza.setDough("thick");
    }
    
    @Override
    public void buildSauce() {
        pizza.setSauce("spicy tomato");
    }
    
    @Override
    public void buildTopping() {
        pizza.setTopping("pepperoni and cheese");
    }
}

// Director
class PizzaDirector {
    private PizzaBuilder pizzaBuilder;
    
    public void setPizzaBuilder(PizzaBuilder pizzaBuilder) {
        this.pizzaBuilder = pizzaBuilder;
    }
    
    public Pizza getPizza() {
        return pizzaBuilder.getPizza();
    }
    
    public void constructPizza() {
        pizzaBuilder.createNewPizza();
        pizzaBuilder.buildDough();
        pizzaBuilder.buildSauce();
        pizzaBuilder.buildTopping();
    }
}

// Cliente
public class Builder {
    public static void main(String[] args) {
        PizzaDirector director = new PizzaDirector();
        PizzaBuilder margheritaBuilder = new MargheritaPizzaBuilder();
        
        director.setPizzaBuilder(margheritaBuilder);
        director.constructPizza();
        
        Pizza pizza = director.getPizza();
        System.out.println(pizza);
    }
}