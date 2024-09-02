import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.sql.*;

public class create_assignment {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Data diri");
        frame.setSize(400, 450);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JLabel nama = new JLabel("Nama :");
        JLabel gender = new JLabel("Gender :");
        JLabel email = new JLabel("Email :");
        JLabel phone = new JLabel("Phone :");
        JLabel address = new JLabel("Address :");
        JLabel date = new JLabel("Date of birth :");
        JLabel username = new JLabel("Username :");
        JLabel passwords = new JLabel("Passwords :");

        JTextField text_nama = new JTextField(20);
        JTextField text_gender = new JTextField(20);
        JTextField text_email = new JTextField(20);
        JTextField text_phone = new JTextField(20);
        JTextField text_address = new JTextField(20);
        JTextField text_date = new JTextField(20);
        JTextField text_username = new JTextField(20);
        JTextField text_passwords = new JTextField(20);

        JButton submit = new JButton("Submit");

        JPanel panel = new JPanel(new GridBagLayout());

        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(10, 10, 10, 10);

        // Komponen di kolom pertama
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(nama, gbc);

        gbc.gridy = 1;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(gender, gbc);

        gbc.gridy = 2;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(email, gbc);

        gbc.gridy = 3;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(phone, gbc);

        gbc.gridy = 4;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(address, gbc);

        gbc.gridy = 5;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(date, gbc);

        gbc.gridy = 6;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(username, gbc);

        gbc.gridy = 7;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(passwords, gbc);

        // komponen kolom dua
        gbc.gridx = 1;
        gbc.gridy = 0;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(text_nama, gbc);

        gbc.gridy = 1;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(text_gender, gbc);

        gbc.gridy = 2;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(text_email, gbc);

        gbc.gridy = 3;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(text_phone, gbc);

        gbc.gridy = 4;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(text_address, gbc);

        gbc.gridy = 5;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(text_date, gbc);

        gbc.gridy = 6;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(text_username, gbc);

        gbc.gridy = 7;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(text_passwords, gbc);

        gbc.gridx = 0;
        gbc.gridy = 8;
        gbc.gridwidth = 2;
        gbc.fill = GridBagConstraints.HORIZONTAL;
        panel.add(submit, gbc);

        frame.add(panel);
        frame.setVisible(true);

        submit.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    String nama = text_nama.getText();
                    String gender = text_gender.getText();
                    String email = text_email.getText();
                    String phone = text_phone.getText();
                    String address = text_address.getText();
                    String date = text_date.getText();
                    String username = text_username.getText();
                    String passwords = text_passwords.getText();

                    Connection database = koneksi.connect();
                    String sql = "INSERT INTO users (Name_user, Gender, Email, Phone, Address, Date_of_birth, Username, Passwords) VALUES (?, ?, ?, ?, ?, ?, ?, ?)";
                    PreparedStatement pstmt = database.prepareStatement(sql);

                    pstmt.setString(1, nama); // Name_user
                    pstmt.setString(2, gender); // Gender
                    pstmt.setString(3, email); // Email
                    pstmt.setString(4, phone); // Phone
                    pstmt.setString(5, address); // Address
                    pstmt.setString(6, date); // Date_of_birth
                    pstmt.setString(7, username); // Username
                    pstmt.setString(8, passwords); // Passwords
                    pstmt.executeUpdate();
                    database.close();

                    JOptionPane.showMessageDialog(frame, "Data berhasil dimasukkan ke tabel users.");
                } catch (SQLException ex) {
                    JOptionPane.showMessageDialog(frame, "Kesalahan database: " + ex.getMessage());
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(frame, "Inputan salah");
                }
            }
        });
    }
}
