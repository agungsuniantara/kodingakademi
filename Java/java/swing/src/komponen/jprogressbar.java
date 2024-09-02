package komponen;
import javax.swing.*;

public class jprogressbar {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Contoh JProgressBar");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JProgressBar progressBar = new JProgressBar();
        progressBar.setStringPainted(true); 

        progressBar.setValue(50);

        JPanel panel = new JPanel();
        panel.add(progressBar);
        frame.add(panel);

        frame.setVisible(true);
    }
}
