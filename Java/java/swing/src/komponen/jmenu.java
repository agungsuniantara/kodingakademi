package komponen;
import javax.swing.*;

public class jmenu {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Contoh JMenu");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JMenuBar menuBar = new JMenuBar();
        JMenu menu = new JMenu("File");
        JMenuItem item1 = new JMenuItem("New");
        JMenuItem item2 = new JMenuItem("Open");
        JMenuItem item3 = new JMenuItem("Save");

        menu.add(item1);
        menu.add(item2);
        menu.add(item3);
        menuBar.add(menu);

        JPanel panel = new JPanel();
        panel.add(menuBar);
        frame.add(panel);

        frame.setVisible(true);
    }
}
