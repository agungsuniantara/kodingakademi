import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

public class SimpleJavaFXExample extends Application {

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        // Membuat objek Button
        Button button = new Button("Klik Saya");

        // Menambahkan event handler untuk tombol
        button.setOnAction(e -> {
            // Menampilkan pesan ke konsol saat tombol diklik
            System.out.println("Hello, World!");
        });

        // Membuat objek StackPane sebagai kontainer
        StackPane root = new StackPane();
        root.getChildren().add(button);

        // Membuat objek Scene
        Scene scene = new Scene(root, 300, 200);

        // Mengatur properti jendela
        primaryStage.setTitle("Contoh GUI JavaFX");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
}
