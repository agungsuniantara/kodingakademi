package event_handler;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class focus_listener {
    public static void main(String[] args) {
        JFrame frame = new JFrame("focus listener");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JTextField textField1 = new JTextField(20);
        JLabel label = new JLabel("label java");
        JButton button = new JButton("Klik");

        JPanel panel = new JPanel(new GridBagLayout());

        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5, 5, 5, 5);

        gbc.gridx = 0;
        gbc.gridy = 0;
        panel.add(textField1, gbc);
        
        gbc.gridx = 0;
        gbc.gridy = 1;
        panel.add(label, gbc);

        gbc.gridx = 0;
        gbc.gridy = 2;
        panel.add(button, gbc);

        frame.add(panel);
        frame.setVisible(true);

        textField1.addFocusListener(new FocusAdapter() {
            @Override
            public void focusGained(FocusEvent e) {
                label.setVisible(false);
            }

            @Override
            public void focusLost(FocusEvent e) {
                label.setVisible(true);
            }
        });
    }
}
