package event_handler;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class action_listener {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Action listener");
        frame.setSize(400, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JLabel label = new JLabel("Input: ");
        JButton button1 = new JButton("Klik");
        JButton button2 = new JButton("Reset");
        JTextField textField = new JTextField(10);

        JPanel panel = new JPanel(new GridBagLayout());

        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5, 5, 5, 5);

        gbc.gridx = 0;
        gbc.gridy = 0;
        panel.add(label, gbc);

        gbc.gridx = 1;
        gbc.gridy = 0;
        panel.add(textField, gbc);

        gbc.gridx = 2;
        gbc.gridy = 0;
        panel.add(button1, gbc);
        
        gbc.gridx = 3;
        gbc.gridy = 0;
        panel.add(button2, gbc);

        frame.add(panel);
        frame.setVisible(true);

        button1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String input = textField.getText();
                JOptionPane.showMessageDialog(frame, "Input : " + input);
            }
        });

        button2.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                textField.setText("");
            }
        });
    }
}
