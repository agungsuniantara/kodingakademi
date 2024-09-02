package komponen;
import javax.swing.*;

public class jtextarea {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Contoh JTextArea");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JTextArea textArea = new JTextArea(5, 20);
        textArea.setLineWrap(true); 
        textArea.setWrapStyleWord(true); 

        JScrollPane scrollPane = new JScrollPane(textArea);

        JPanel panel = new JPanel();
        panel.add(scrollPane);
        frame.add(panel);

        frame.setVisible(true);
    }
}
