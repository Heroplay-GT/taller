import java.util.HashMap;
import java.util.Map;

// Flyweight interface
interface TreeType {
    void render(int x, int y, String color);
}

// Flyweight concreto
class TreeTypeConcrete implements TreeType {
    private String name;
    private String sprite; // Estado intrínseco (compartido)
    
    public TreeTypeConcrete(String name, String sprite) {
        this.name = name;
        this.sprite = sprite;
    }
    
    @Override
    public void render(int x, int y, String color) {
        System.out.println("Rendering " + name + " tree at (" + x + "," + y + ") with " + color + " color using sprite: " + sprite);
    }
}

// Flyweight factory
class TreeTypeFactory {
    private static Map<String, TreeType> treeTypes = new HashMap<>();
    
    public static TreeType getTreeType(String name, String sprite) {
        TreeType treeType = treeTypes.get(name);
        if (treeType == null) {
            treeType = new TreeTypeConcrete(name, sprite);
            treeTypes.put(name, treeType);
            System.out.println("Creating new TreeType: " + name);
        }
        return treeType;
    }
    
    public static int getCreatedTreeTypesCount() {
        return treeTypes.size();
    }
}

// Context (contiene estado extrínseco)
class Tree {
    private int x, y;
    private String color;
    private TreeType treeType;
    
    public Tree(int x, int y, String color, TreeType treeType) {
        this.x = x;
        this.y = y;
        this.color = color;
        this.treeType = treeType;
    }
    
    public void render() {
        treeType.render(x, y, color);
    }
}

// Forest (cliente)
class Forest {
    private java.util.List<Tree> trees = new java.util.ArrayList<>();
    
    public void plantTree(int x, int y, String name, String color, String sprite) {
        TreeType type = TreeTypeFactory.getTreeType(name, sprite);
        Tree tree = new Tree(x, y, color, type);
        trees.add(tree);
    }
    
    public void render() {
        for (Tree tree : trees) {
            tree.render();
        }
    }
    
    public int getTreeCount() {
        return trees.size();
    }
}

// Cliente
public class Flyweight {
    public static void main(String[] args) {
        Forest forest = new Forest();
        
        // Plantar muchos árboles
        forest.plantTree(1, 1, "Oak", "Green", "oak_sprite.png");
        forest.plantTree(2, 2, "Pine", "Dark Green", "pine_sprite.png");
        forest.plantTree(3, 3, "Oak", "Brown", "oak_sprite.png");
        forest.plantTree(4, 4, "Pine", "Green", "pine_sprite.png");
        forest.plantTree(5, 5, "Oak", "Yellow", "oak_sprite.png");
        
        forest.render();
        
        System.out.println("\nTotal trees: " + forest.getTreeCount());
        System.out.println("Tree types created: " + TreeTypeFactory.getCreatedTreeTypesCount());
    }
}