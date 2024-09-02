package komponen;
import javax.swing.*;

public class jlist {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Contoh JList");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        String[] options = {"Item 1", "Item 2", "Item 3"};

        JList<String> list = new JList<>(options);

        JPanel panel = new JPanel();
        panel.add(list);
        frame.add(panel);

        frame.setVisible(true);
    }
}
