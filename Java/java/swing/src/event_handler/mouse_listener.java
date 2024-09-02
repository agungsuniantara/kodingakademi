package event_handler;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class mouse_listener {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Mouse adapter");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JButton button = new JButton("Submit");

        JPanel panel = new JPanel(new GridBagLayout());
        
        panel.add(button);
        frame.add(panel);
        frame.setVisible(true);

        button.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseEntered(MouseEvent e) {
                button.setBackground(Color.RED);
            }

            @Override
            public void mouseExited(MouseEvent e) {
                button.setBackground(null);
            }
        });
    }
}
