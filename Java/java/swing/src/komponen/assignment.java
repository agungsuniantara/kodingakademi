package komponen;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class assignment {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Data diri");
        frame.setSize(205, 320);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JLabel label_nama = new JLabel("Nama : ");
        JTextField textField_nama = new JTextField(15);
        JLabel label_umur = new JLabel("Umur : ");
        JTextField textField_umur = new JTextField(15);
        JLabel label_alamat = new JLabel("Alamat : ");
        JTextArea textArea_alamat = new JTextArea(5, 18);
        textArea_alamat.setLineWrap(true); 
        textArea_alamat.setWrapStyleWord(true); 
        JScrollPane scrollPane = new JScrollPane(textArea_alamat);
        JLabel label_gender = new JLabel("Gender : ");
        JCheckBox checkBox_male = new JCheckBox("Male");
        JCheckBox checkBox_female = new JCheckBox("Female");
        JButton button = new JButton("Submit");
        button.setSize(200, 50);

        JPanel panel = new JPanel();
        panel.add(label_nama);
        panel.add(textField_nama);
        panel.add(label_umur);
        panel.add(textField_umur);
        panel.add(label_alamat);
        panel.add(scrollPane);
        panel.add(label_gender);
        panel.add(checkBox_male);
        panel.add(checkBox_female);
        panel.add(button);
        frame.add(panel);

        frame.setVisible(true);
    }
}
