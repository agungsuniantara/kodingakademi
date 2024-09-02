import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SimpleGUIExample {

    public static void main(String[] args) {
        // Membuat objek JFrame (jendela)
        JFrame frame = new JFrame("Contoh GUI Java Swing");

        // Membuat objek JButton
        JButton button = new JButton("Klik Saya");

        // Membuat objek JTextField
        JTextField textField = new JTextField();
        textField.setColumns(20); // Set panjang kolom (jumlah karakter) untuk JTextField

        // Membuat objek JLabel
        JLabel label = new JLabel("Masukkan Nama:");

        // Membuat objek JComboBox
        String[] options = {"Pilihan 1", "Pilihan 2", "Pilihan 3"};
        JComboBox<String> comboBox = new JComboBox<>(options);

        // Membuat objek JTextArea
        JTextArea textArea = new JTextArea();
        JScrollPane scrollPane = new JScrollPane(textArea);
		
        textArea.setLineWrap(true); // Agar teks otomatis pindah ke baris berikutnya
        textArea.setWrapStyleWord(true); // Pindah ke kata berikutnya jika teks tidak muat

        scrollPane.setPreferredSize(textField.getPreferredSize()); // Set preferensi ukuran

        // Menambahkan event listener untuk tombol
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Mendapatkan teks dari JTextField dan pilihan dari JComboBox
                String inputText = textField.getText();
                String selectedOption = comboBox.getSelectedItem().toString();

                // Menampilkan dialog pesan dengan teks yang dimasukkan oleh pengguna dan pilihan dari JComboBox
                JOptionPane.showMessageDialog(frame, "Hello, " + inputText + "! Anda memilih: " + selectedOption);
            }
        });

        // Membuat panel dengan GridBagLayout dan menambahkan komponen-komponen ke dalamnya
        JPanel panel = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();

        gbc.anchor = GridBagConstraints.WEST;
        gbc.insets = new Insets(5, 5, 5, 5);

        gbc.gridx = 0;
        gbc.gridy = 0;
        panel.add(label, gbc);

        gbc.gridy = 1;
        panel.add(textField, gbc);

        gbc.gridy = 2;
        panel.add(comboBox, gbc);

        gbc.gridy = 3;
        gbc.gridheight = 2;
        panel.add(scrollPane, gbc);

        gbc.gridy = 5;
        gbc.gridheight = 1;
        panel.add(button, gbc);

        // Menambahkan panel ke dalam jendela
        frame.getContentPane().add(panel);

        // Mengatur properti jendela
        frame.setSize(400, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null); // Jendela akan muncul di tengah layar
        frame.setVisible(true);
    }
}
