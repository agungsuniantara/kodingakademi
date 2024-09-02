import javax.swing.*;
import java.awt.*;

public class gridbag {
    public static void main(String[] args) throws Exception {
        // Membuat jendela JFrame
        JFrame frame = new JFrame("Contoh Komponen Java Swing");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Membuat JPanel untuk menempatkan komponen lainnya dengan GridBagLayout
        JPanel panel = new JPanel(new GridBagLayout());
 
        // Menambahkan komponen-komponen ke dalam JPanel dengan GridBagLayout
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5, 5, 5, 5); // Memberikan jarak antara komponen

        // Komponen-komponen di kolom pertama
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(new JLabel("Label:"), gbc);

        gbc.gridy = 1;
        panel.add(new JLabel("Text Field:"), gbc);

        gbc.gridy = 2;
        panel.add(new JLabel("Text Area:"), gbc);

        gbc.gridy = 3;
        panel.add(new JLabel("Check Box:"), gbc);

        gbc.gridy = 4;
        panel.add(new JLabel("Radio Button 1:"), gbc);

        gbc.gridy = 5;
        panel.add(new JLabel("Radio Button 2:"), gbc);

        // Komponen-komponen di kolom kedua
        gbc.gridx = 1;
        gbc.gridy = 0;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(new JButton("Klik Saya"), gbc);

        gbc.gridy = 1;
        panel.add(new JTextField(20), gbc);

        gbc.gridy = 2;
        JTextArea textArea = new JTextArea(2, 20);
        JScrollPane scrollPane = new JScrollPane(textArea);
        panel.add(scrollPane, gbc);

        gbc.gridy = 3;
        panel.add(new JCheckBox("Pilih Saya"), gbc);

        gbc.gridy = 4;
        panel.add(new JRadioButton("Pilihan 1"), gbc);

        gbc.gridy = 5;
        panel.add(new JRadioButton("Pilihan 2"), gbc);

        // Menambahkan JPanel ke dalam jendela JFrame
        frame.add(panel);

        // Menampilkan jendela JFrame
        frame.pack();
        frame.setVisible(true);
    }
}
