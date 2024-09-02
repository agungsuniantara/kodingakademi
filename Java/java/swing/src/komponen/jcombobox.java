package komponen;
import javax.swing.*;

public class jcombobox {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Contoh JComboBox");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        String[] options = {"Pilihan 1", "Pilihan 2", "Pilihan 3"};

        JComboBox<String> comboBox = new JComboBox<>(options);
        comboBox.setSelectedIndex(0);

        JPanel panel = new JPanel();
        panel.add(comboBox);
        frame.add(panel);

        frame.setVisible(true);
    }
}
