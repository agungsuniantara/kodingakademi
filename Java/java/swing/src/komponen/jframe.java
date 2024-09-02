package komponen;
import javax.swing.*;

public class jframe {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Contoh JFrame");
        frame.setSize(400, 300);
        frame.setLocationRelativeTo(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}
