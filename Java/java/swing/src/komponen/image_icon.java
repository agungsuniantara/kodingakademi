package komponen;

import javax.swing.*;
import java.awt.*;

public class image_icon {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Image icon");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        ImageIcon original_icon = new ImageIcon("swing/src/komponen/logo-koding.png");
        Image image = original_icon.getImage().getScaledInstance(150, 50, Image.SCALE_SMOOTH);
        ImageIcon edit_icon = new ImageIcon(image);

        JLabel label = new JLabel(edit_icon);

        JPanel panel = new JPanel();
        panel.add(label);
        frame.add(panel);

        frame.setVisible(true);
    }
}
