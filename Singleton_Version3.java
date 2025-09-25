// Singleton thread-safe
class DatabaseConnection {
    private static volatile DatabaseConnection instance;
    private String connectionString;
    
    private DatabaseConnection() {
        // Constructor privado para prevenir instanciación
        connectionString = "Database connected";
        System.out.println("Database connection created");
    }
    
    public static DatabaseConnection getInstance() {
        if (instance == null) {
            synchronized (DatabaseConnection.class) {
                if (instance == null) {
                    instance = new DatabaseConnection();
                }
            }
        }
        return instance;
    }
    
    public void query(String sql) {
        System.out.println("Executing query: " + sql);
    }
    
    public String getConnectionString() {
        return connectionString;
    }
}

// Cliente
public class Singleton {
    public static void main(String[] args) {
        // Obtener la instancia del singleton
        DatabaseConnection db1 = DatabaseConnection.getInstance();
        DatabaseConnection db2 = DatabaseConnection.getInstance();
        
        // Verificar que son la misma instancia
        System.out.println("Same instance? " + (db1 == db2));
        
        db1.query("SELECT * FROM users");
        db2.query("SELECT * FROM products");
        
        System.out.println("Connection 1: " + db1.getConnectionString());
        System.out.println("Connection 2: " + db2.getConnectionString());
    }
}