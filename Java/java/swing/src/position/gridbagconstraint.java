package position;
import javax.swing.*;
import java.awt.*;

public class gridbagconstraint {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Gridbaglayout");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JLabel name = new JLabel("Name : ");
        JLabel address = new JLabel("Address : ");
        JTextField text_name = new JTextField(10);
        JTextField text_address = new JTextField(10);
        JButton submit = new JButton("Klik");

        JPanel panel = new JPanel(new GridBagLayout());

        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5, 5, 5, 5);

        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.ipadx = 10;
        gbc.ipady = 10;
        panel.add(name, gbc);

        gbc.gridy = 1;
        panel.add(address, gbc);

        gbc.gridx = 1;
        gbc.gridy = 0;
        panel.add(text_name, gbc);

        gbc.gridy = 1;
        panel.add(text_address, gbc);

        gbc.gridx = 0;
        gbc.gridy = 2;
        gbc.gridwidth = 2;
        gbc.fill = GridBagConstraints.BOTH;
        panel.add(submit, gbc);

        frame.add(panel);
        frame.setVisible(true);
    }
}
