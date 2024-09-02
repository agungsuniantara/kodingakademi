package event_handler;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class assignment {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Calculator");
        frame.setSize(300, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null);

        JLabel label_angka1 = new JLabel("Angka 1 : ");
        JLabel label_angka2 = new JLabel("Angka 2 : ");
        JLabel operator = new JLabel("Operator : ");
        JTextField text_angka1 = new JTextField(10);
        JTextField text_angka2 = new JTextField(10);

        String[] options = {"","Tambah", "Kurang", "Bagi", "Kali"};
        JComboBox<String> comboBox = new JComboBox<>(options);
        comboBox.setSelectedIndex(0);

        JButton submit = new JButton("Hitung");

        JPanel panel = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5, 5, 10, 5);
        
        // kolom 1

        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(label_angka1, gbc);

        gbc.gridy = 1;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(label_angka2, gbc);

        gbc.gridy = 2;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(operator, gbc);

        // kolom 2

        gbc.gridx = 1;
        gbc.gridy = 0;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(text_angka1, gbc);

        gbc.gridy = 1;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(text_angka2, gbc);

        gbc.gridy = 2;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(comboBox, gbc);

        gbc.gridx = 0;
        gbc.gridy = 3;
        gbc.gridwidth = 2;
        gbc.fill = GridBagConstraints.HORIZONTAL;
        panel.add(submit, gbc);

        frame.add(panel);
        frame.setVisible(true);

        submit.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try{
                    int angka1 = Integer.parseInt(text_angka1.getText());
                    int angka2 = Integer.parseInt(text_angka2.getText());
                    String op = String.valueOf(comboBox.getSelectedItem());

                    if(op.equals("Tambah")){
                        int hasil = angka1 + angka2;
                        JOptionPane.showMessageDialog(frame, "Hasil : " + hasil);
                    }
                    else if(op.equals("Kurang")){
                        int hasil = angka1 - angka2;
                        JOptionPane.showMessageDialog(frame, "Hasil : " + hasil);
                    }
                    else if(op.equals("Bagi")){
                        Double hasil = Double.valueOf(angka1) / Double.valueOf(angka2);
                        JOptionPane.showMessageDialog(frame, "Hasil : " + hasil);
                    }
                    else if(op.equals("Kali")){
                        int hasil = angka1 * angka2;
                        JOptionPane.showMessageDialog(frame, "Hasil : " + hasil);
                    }
                }
                catch (NumberFormatException ex){
                    JOptionPane.showMessageDialog(frame, "Inputan salah");
                }
            }
        });
    }
}
