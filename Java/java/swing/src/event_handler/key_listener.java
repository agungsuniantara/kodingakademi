package event_handler;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class key_listener {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Key adapter");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JTextField textField = new JTextField(10);

        JPanel panel = new JPanel(new GridBagLayout());
        panel.add(textField);
        frame.add(panel);

        frame.setVisible(true);

        textField.addKeyListener(new KeyAdapter() {
            @Override
            public void keyTyped(KeyEvent e) {
                if (e.getKeyChar() == 'R' || e.getKeyChar() == 'r'){
                    panel.setBackground(Color.RED);
                }
                else{
                    panel.setBackground(null);
                }
            }
        });
    }
}
