package event_handler;

import javax.swing.*;
import java.awt.event.*;

public class window_listener {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Window Listener");
        frame.setSize(300, 200);

        frame.setLocationRelativeTo(null);
        frame.setVisible(true);

        frame.addWindowListener(new WindowAdapter() {
            @Override
            public void windowOpened(WindowEvent e) {
                JOptionPane.showMessageDialog(frame, "Jendela dibuka");
            }

            @Override
            public void windowClosing(WindowEvent e) {
                int option = JOptionPane.showConfirmDialog(frame, "ingin menutup jendela?");
                if (option == JOptionPane.OK_OPTION) {
                    frame.dispose();
                } else if (option == JOptionPane.CANCEL_OPTION || option == JOptionPane.NO_OPTION) {
                    frame.setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
                }
            }
        });
    }
}
