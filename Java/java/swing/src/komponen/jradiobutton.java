package komponen;
import javax.swing.*;

public class jradiobutton {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Contoh JRadioButton");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JRadioButton radioButton = new JRadioButton("Pilihan");

        JPanel panel = new JPanel();
        panel.add(radioButton);
        frame.add(panel);

        frame.setVisible(true);
    }
}
