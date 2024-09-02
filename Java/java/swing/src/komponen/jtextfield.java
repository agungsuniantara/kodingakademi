package komponen;
import javax.swing.*;

public class jtextfield {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Contoh JTextField");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JTextField textField = new JTextField(10);

        JPanel panel = new JPanel();
        panel.add(textField);
        frame.add(panel);

        frame.setVisible(true);
    }
}
