package position;
import javax.swing.*;
import java.awt.*;

public class gridbaglayout {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Contoh Label");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            
        JLabel label = new JLabel("Ini adalah label");

        JPanel panel = new JPanel(new GridBagLayout());
        panel.add(label);
        frame.add(panel);

        frame.setVisible(true);
    }
}
