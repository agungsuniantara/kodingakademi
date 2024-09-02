import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class tesGUI {
    private static double hasil;
    private static double angka1;
    private static double angka2;
    private static JTextField persegiText1;
    private static JTextField persegiText2;
    private static JTextField persegipanjangText1;
    private static JTextField persegipanjangText2;

    public static void main(String[] args) {
        JFrame frame = new JFrame("Kalkulator");
        JLabel pesan = new JLabel("Pilih bangun datar : ");
        String[] options = {"persegi", "persegi panjang"};
        JComboBox<String> comboBox = new JComboBox<>(options);
        JButton button = new JButton("Submit");

        JPanel panel = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();

        gbc.anchor = GridBagConstraints.WEST;
        gbc.insets = new Insets(5, 5, 5, 5);

        gbc.gridy = 0;
        panel.add(pesan, gbc);

        gbc.gridy = 1;
        panel.add(comboBox, gbc);

        gbc.gridy = 2;
        panel.add(button, gbc);

        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (!isCalculating) {
                    isCalculating = true;
                    button.setVisible(false);

                    String select = comboBox.getSelectedItem().toString();

                    if (select.equals("persegi")) {
                        JLabel persegiLabel1 = new JLabel("Masukkan sisi:");
						// Remove JTextField data type
						persegiText1 = new JTextField();
						persegiText1.setColumns(20);

						JLabel persegiLabel2 = new JLabel("Masukkan sisi:");
						// Remove JTextField data type
						persegiText2 = new JTextField();
						persegiText2.setColumns(20);

						gbc.gridy = 3;
						panel.add(persegiLabel1, gbc);

						gbc.gridy = 4;
						panel.add(persegiText1, gbc);

						gbc.gridy = 5;
						panel.add(persegiLabel2, gbc);

						gbc.gridy = 6;
						panel.add(persegiText2, gbc);
                    } 
					else if (select.equals("persegi panjang")) {
                        JLabel persegipanjangLabel1 = new JLabel("Masukkan panjang:");
                    
						persegipanjangText1 = new JTextField();
						persegipanjangText1.setColumns(20);

						JLabel persegipanjangLabel2 = new JLabel("Masukkan lebar:");
                    
						persegipanjangText2 = new JTextField();
						persegipanjangText2.setColumns(20);

						gbc.gridy = 3;
						panel.add(persegipanjangLabel1, gbc);

						gbc.gridy = 4;
						panel.add(persegipanjangText1, gbc);

						gbc.gridy = 5;
						panel.add(persegipanjangLabel2, gbc);

						gbc.gridy = 6;
						panel.add(persegipanjangText2, gbc);
                    }

                    JButton calculateButton = new JButton("Calculate");
                    JButton backButton = new JButton("Back");
                    gbc.gridy++;
                    panel.add(calculateButton, gbc);
                    gbc.gridy++;
                    panel.add(backButton, gbc);

                    calculateButton.addActionListener(new ActionListener() {
                        @Override
                        public void actionPerformed(ActionEvent e) {
                            String select = comboBox.getSelectedItem().toString();

                            if (select.equals("persegi")) {
                                angka1 = Double.parseDouble(persegiText1.getText());
                                angka2 = Double.parseDouble(persegiText2.getText());
                                hasil = angka1 * angka2;
                                JOptionPane.showMessageDialog(frame, "Luas persegi = " + hasil);
                            } else if (select.equals("persegi panjang")) {
                                angka1 = Double.parseDouble(persegipanjangText1.getText());
                                angka2 = Double.parseDouble(persegipanjangText2.getText());
                                hasil = angka1 * angka2;
                                JOptionPane.showMessageDialog(frame, "Luas persegi panjang = " + hasil);
                            }

                            isCalculating = false;
                            button.setVisible(true);
                            calculateButton.setVisible(false);
                            backButton.setVisible(false);
                        }
                    });

                    backButton.addActionListener(new ActionListener() {
                        @Override
                        public void actionPerformed(ActionEvent e) {
                            isCalculating = false;
                            button.setVisible(true);
                            calculateButton.setVisible(false);
                            backButton.setVisible(false);
                        }
                    });

                    calculateButton.setVisible(true);
                    backButton.setVisible(true);

                    frame.validate();
                    frame.repaint();
                }
            }
        });

        frame.getContentPane().add(panel);

        frame.setSize(400, 500);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}
