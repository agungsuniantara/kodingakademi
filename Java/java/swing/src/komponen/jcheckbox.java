package komponen;
import javax.swing.*;

public class jcheckbox {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Contoh JCheckBox");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JCheckBox checkBox = new JCheckBox("Checkbox");

        JPanel panel = new JPanel();
        panel.add(checkBox);
        frame.add(panel);

        frame.setVisible(true);
    }
}
