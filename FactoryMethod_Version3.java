// Producto abstracto
abstract class Animal {
    public abstract void makeSound();
}

// Productos concretos
class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Woof!");
    }
}

class Cat extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Meow!");
    }
}

// Creator abstracto
abstract class AnimalFactory {
    public abstract Animal createAnimal();
    
    public void playWithAnimal() {
        Animal animal = createAnimal();
        animal.makeSound();
    }
}

// Creators concretos
class DogFactory extends AnimalFactory {
    @Override
    public Animal createAnimal() {
        return new Dog();
    }
}

class CatFactory extends AnimalFactory {
    @Override
    public Animal createAnimal() {
        return new Cat();
    }
}

// Cliente
public class FactoryMethod {
    public static void main(String[] args) {
        AnimalFactory dogFactory = new DogFactory();
        AnimalFactory catFactory = new CatFactory();
        
        dogFactory.playWithAnimal(); // Output: Woof!
        catFactory.playWithAnimal(); // Output: Meow!
    }
}