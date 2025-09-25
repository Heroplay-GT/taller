import java.util.ArrayList;
import java.util.List;

// Iterator interface
interface Iterator<T> {
    boolean hasNext();
    T next();
}

// Aggregate interface
interface BookCollection {
    Iterator<Book> createIterator();
}

// Item
class Book {
    private String title;
    private String author;
    
    public Book(String title, String author) {
        this.title = title;
        this.author = author;
    }
    
    public String getTitle() { return title; }
    public String getAuthor() { return author; }
    
    @Override
    public String toString() {
        return "'" + title + "' by " + author;
    }
}

// Concrete Iterator
class BookIterator implements Iterator<Book> {
    private List<Book> books;
    private int position = 0;
    
    public BookIterator(List<Book> books) {
        this.books = books;
    }
    
    @Override
    public boolean hasNext() {
        return position < books.size();
    }
    
    @Override
    public Book next() {
        if (hasNext()) {
            return books.get(position++);
        }
        return null;
    }
}

// Concrete Aggregate
class Library implements BookCollection {
    private List<Book> books;
    
    public Library() {
        books = new ArrayList<>();
    }
    
    public void addBook(Book book) {
        books.add(book);
    }
    
    public void removeBook(Book book) {
        books.remove(book);
    }
    
    @Override
    public Iterator<Book> createIterator() {
        return new BookIterator(books);
    }
    
    public int getBookCount() {
        return books.size();
    }
}

// Cliente
public class Iterator {
    public static void main(String[] args) {
        Library library = new Library();
        
        // Agregar libros
        library.addBook(new Book("Design Patterns", "Gang of Four"));
        library.addBook(new Book("Clean Code", "Robert Martin"));
        library.addBook(new Book("Effective Java", "Joshua Bloch"));
        library.addBook(new Book("Java: The Complete Reference", "Herbert Schildt"));
        
        System.out.println("Library contains " + library.getBookCount() + " books:");
        System.out.println("=== Iterating through books ===");
        
        // Usar iterator para recorrer los libros
        Iterator<Book> iterator = library.createIterator();
        while (iterator.hasNext()) {
            Book book = iterator.next();
            System.out.println("- " + book);
        }
        
        System.out.println("\n=== Iterating again (fresh iterator) ===");
        Iterator<Book> newIterator = library.createIterator();
        while (newIterator.hasNext()) {
            Book book = newIterator.next();
            System.out.println("Reading: " + book.getTitle());
        }
    }
}