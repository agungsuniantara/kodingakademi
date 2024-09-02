import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class tambah extends JFrame implements ActionListener {

    // Komponen GUI
    Label lblJudul, lblAngka1, lblAngka2;
    TextField txtAngka1, txtAngka2;
    Button btnTambah, btnKeluar;
	double angka1, angka2, hasil;

    public tambah() {
        // Pengaturan frame
        setTitle("tambah");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Menambahkan komponen ke frame menggunakan GridBagLayout
        setLayout(new GridBagLayout());
        GridBagConstraints c = new GridBagConstraints();

        // Grid untuk judul
        c.gridx = 0;
        c.gridy = 0;
        c.gridwidth = 2;
        c.fill = GridBagConstraints.HORIZONTAL;
        add(lblJudul = new Label("Sistem Login"), c);

        // Label dan text field untuk username dan password
        c.gridy++;
        c.gridwidth = 1;
        c.fill = GridBagConstraints.NONE;
        add(lblAngka1 = new Label("angka 1: "), c);
		
        c.gridx++;
        c.fill = GridBagConstraints.HORIZONTAL;
        add(txtAngka1 = new TextField(20), c);

        c.gridy++;
        c.gridx = 0;
        c.fill = GridBagConstraints.NONE;
        add(lblAngka2 = new Label("Password:"), c);
		
        c.gridx++;
        c.fill = GridBagConstraints.HORIZONTAL;
        add(txtAngka2 = new TextField(20), c);

        // Tombol tambah dan keluar
        c.gridy++;
		c.gridx = 1;
        add(btnTambah = new Button("Tambah"), c);
		
        c.gridy++;
		c.gridx = 1;
        add(btnKeluar = new Button("Keluar"), c);

        // Menambahkan ActionListener
        btnTambah.addActionListener(this);
        btnKeluar.addActionListener(this);
    }

    public void actionPerformed(ActionEvent e) {
        // Menangani aksi tombol
        if (e.getSource() == btnTambah) {
            angka1 = Double.parseDouble(txtAngka1.getText());
			angka2 = Double.parseDouble(txtAngka2.getText());
			hasil = angka1 + angka2;
			
			JOptionPane.showMessageDialog(null, "hasil = " + hasil);
        } else if (e.getSource() == btnKeluar) {
            // Keluar dari program
            System.exit(0);
        }
    }

    public static void main(String[] args) {
        // Menjalankan program
        tambah pertambahan = new tambah();
        pertambahan.setVisible(true);
    }
}
