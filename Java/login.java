import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class login extends JFrame implements ActionListener {

    // Komponen GUI
    Label lblJudul, lblUsername, lblPassword;
    TextField txtUsername, txtPassword;
    Button btnLogin, btnKeluar;

    public login() {
        // Pengaturan frame
        setTitle("Login");
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
        add(lblUsername = new Label("Nama Pengguna:"), c);
		
        c.gridx++;
        c.fill = GridBagConstraints.HORIZONTAL;
        add(txtUsername = new TextField(20), c);

        c.gridy++;
        c.gridx = 0;
        c.fill = GridBagConstraints.NONE;
        add(lblPassword = new Label("Password:"), c);
		
        c.gridx++;
        c.fill = GridBagConstraints.HORIZONTAL;
        add(txtPassword = new TextField(20), c);

        // Tombol login dan keluar
        c.gridy++;
		c.gridx = 1;
        add(btnLogin = new Button("Login"), c);
		
        c.gridy++;
		c.gridx = 1;
        add(btnKeluar = new Button("Keluar"), c);

        // Menambahkan ActionListener
        btnLogin.addActionListener(this);
        btnKeluar.addActionListener(this);
    }

    public void actionPerformed(ActionEvent e) {
        // Menangani aksi tombol
        if (e.getSource() == btnLogin) {
            // Validasi login
            if (txtUsername.getText().equals("admin") && txtPassword.getText().equals("admin")) {
                // Tampilkan pesan login berhasil
                JOptionPane.showMessageDialog(null, "Login berhasil!");
            } else {
                // Tampilkan pesan login gagal
                JOptionPane.showMessageDialog(null, "Login gagal!");
            }
        } else if (e.getSource() == btnKeluar) {
            // Keluar dari program
            System.exit(0);
        }
    }

    public static void main(String[] args) {
        // Menjalankan program
        login loginn = new login();
        loginn.setVisible(true);
    }
}
