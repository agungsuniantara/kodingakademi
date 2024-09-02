package komponen;
import javax.swing.*;

public class jbutton {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Contoh JButton");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JButton button = new JButton("Klik");

        JPanel panel = new JPanel();
        panel.add(button);
        frame.add(panel);

        frame.setVisible(true);
    }
}
