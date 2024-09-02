package position;
import javax.swing.*;
import java.awt.*;

public class anchor {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Gridbaglayout");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JLabel name = new JLabel("Name : ");
        JLabel address = new JLabel("Address : ");
        JTextField text_name = new JTextField(10);
        JTextField text_address = new JTextField(10);
        JButton button = new JButton("Klik");

        JPanel panel = new JPanel(new GridBagLayout());

        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5, 5, 5, 5);

        // Komponen di kolom pertama
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(name, gbc);

        gbc.gridy = 1;
        gbc.anchor = GridBagConstraints.EAST;
        panel.add(address, gbc);

        // Komponen di kolom kedua
        gbc.gridx = 1;
        gbc.gridy = 0;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(text_name, gbc);

        gbc.gridy = 1;
        gbc.anchor = GridBagConstraints.EAST;
        panel.add(text_address, gbc);

         // Tombol memanjang dan mengambil 2 kolom
        gbc.gridx = 0;
        gbc.gridy = 2;
        gbc.gridwidth = 2;
        gbc.fill = GridBagConstraints.HORIZONTAL;
        panel.add(button, gbc);

        frame.add(panel);
        frame.setVisible(true);
    }
}
