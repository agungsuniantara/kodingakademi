package event_handler;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class item_listener {
    public static void main(String[] args) {
        JFrame frame = new JFrame("item listener");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        String[] options = {"", "Pilihan 1", "Pilihan 2", "Pilihan 3"};
        JComboBox<String> comboBox = new JComboBox<>(options);

        JLabel label = new JLabel("Opsi pilihan : ");

        JPanel panel = new JPanel(new GridBagLayout());

        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5, 5, 5, 5);

        gbc.gridx = 0;
        gbc.gridy = 0;
        panel.add(comboBox, gbc);
        
        gbc.gridx = 0;
        gbc.gridy = 1;
        panel.add(label, gbc);

        frame.add(panel);
        frame.setVisible(true);

        comboBox.addItemListener(new ItemListener() {
            @Override
            public void itemStateChanged(ItemEvent e) {
                if (e.getStateChange() == ItemEvent.SELECTED) {
                    String selectedOption = (String) comboBox.getSelectedItem();
                    label.setText("Opsi pilihan : " + selectedOption);
                }
            }
        });
    }
}
