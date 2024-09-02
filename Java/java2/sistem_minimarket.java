import java.util.ArrayList;

// Kelas untuk merepresentasikan barang
class Product {
    private String name;
    private double price;
    private int quantity;

    public Product(String name, double price, int quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
}

// Kelas untuk merepresentasikan transaksi
class Transaction {
    private ArrayList<Product> products;

    public Transaction() {
        products = new ArrayList<>();
    }

    public void addProduct(Product product) {
        products.add(product);
    }

    public double calculateTotal() {
        double total = 0;
        for (Product product : products) {
            total += product.getPrice() * product.getQuantity();
        }
        return total;
    }
}

// Kelas untuk merepresentasikan minimarket
class Minimarket {
    private ArrayList<Product> inventory;

    public Minimarket() {
        inventory = new ArrayList<>();
    }

    public void addProductToInventory(Product product) {
        inventory.add(product);
    }

    public void sellProduct(String productName, int quantity, Transaction transaction) {
        for (Product product : inventory) {
            if (product.getName().equals(productName) && product.getQuantity() >= quantity) {
                Product soldProduct = new Product(product.getName(), product.getPrice(), quantity);
                transaction.addProduct(soldProduct);
                product.setQuantity(product.getQuantity() - quantity);
                System.out.println(quantity + " " + productName + "(s) sold.");
                return;
            }
        }
        System.out.println("Sorry, " + productName + " is out of stock.");
    }
}

public class sistem_minimarket {
    public static void main(String[] args) {
        // Membuat instance minimarket
        Minimarket minimarket = new Minimarket();

        // Menambahkan beberapa produk ke inventaris minimarket
        minimarket.addProductToInventory(new Product("Mie Instan", 2500, 100));
        minimarket.addProductToInventory(new Product("Sabun Mandi", 5000, 50));
        minimarket.addProductToInventory(new Product("Gula", 10000, 30));

        // Membuat transaksi baru
        Transaction transaction = new Transaction();

        // Menjual beberapa barang
        minimarket.sellProduct("Mie Instan", 5, transaction);
        minimarket.sellProduct("Gula", 2, transaction);
        minimarket.sellProduct("Sabun Mandi", 10, transaction);

        // Menampilkan total pembelian
        System.out.println("Total pembelian: Rp " + transaction.calculateTotal());
    }
}
