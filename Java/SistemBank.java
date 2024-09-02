import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class SistemBank extends JFrame implements ActionListener {

    // Komponen GUI
    Label lblJudul, lblUsername, lblPassword;
    TextField txtUsername, txtPassword;
    Button btnLogin, btnKeluar;
    JPanel pnlMenu;

    public SistemBank() {
        // Pengaturan frame
        setTitle("Sistem Bank");
        setSize(400, 300);
        setLayout(new FlowLayout());

        // Menambahkan komponen GUI
        lblJudul = new Label("Sistem Bank Sederhana");
        lblUsername = new Label("Nama Pengguna:");
        lblPassword = new Label("Password:");
        txtUsername = new TextField(20);
        txtPassword = new TextField(20);
        btnLogin = new Button("Login");
        btnKeluar = new Button("Keluar");
        pnlMenu = new JPanel();

        add(lblJudul);
        add(lblUsername);
        add(txtUsername);
        add(lblPassword);
        add(txtPassword);
        add(btnLogin);
        add(btnKeluar);
        add(pnlMenu);

        // Menambahkan ActionListener
        btnLogin.addActionListener(this);
        btnKeluar.addActionListener(this);

        // Menambahkan panel menu
        pnlMenu.setVisible(false);
    }

    public void actionPerformed(ActionEvent e) {
        // Menangani aksi tombol
        if (e.getSource() == btnLogin) {
            // Validasi login
            if (txtUsername.getText().equals("admin") && txtPassword.getText().equals("admin")) {
                // Tampilkan menu utama
                pnlMenu.setVisible(true);
            } else {
                // Tampilkan pesan error
                System.out.println("Login gagal!");
            }
        } else if (e.getSource() == btnKeluar) {
            // Keluar dari program
            System.exit(0);
        }
    }

    public static void main(String[] args) {
        // Menjalankan program
        SistemBank sb = new SistemBank();
        sb.setVisible(true);
    }
}
