package komponen;
import javax.swing.*;

public class jpanel {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Contoh JPanel");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel();
        frame.add(panel);

        frame.setVisible(true);
    }
}
