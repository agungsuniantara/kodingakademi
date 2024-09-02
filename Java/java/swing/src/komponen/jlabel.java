package komponen;
import javax.swing.*;

public class jlabel {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Contoh JLabel");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JLabel label = new JLabel("Ini adalah label");

        JPanel panel = new JPanel();
        panel.add(label);
        frame.add(panel);

        frame.setVisible(true);
    }
}
