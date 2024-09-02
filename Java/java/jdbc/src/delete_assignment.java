import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.sql.*;
import javax.swing.table.*;

public class delete_assignment {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Delete assignment");
        frame.setSize(600, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null); // Menempatkan frame di tengah layar
        
        JButton create = new JButton("create");
        JButton view = new JButton("view");
        JButton update = new JButton("update");
        JButton delete = new JButton("delete");
        view.setBorderPainted(true); // Mengembalikan garis di sekitar tulisan pada button
        update.setBorderPainted(true);
        create.setBorderPainted(true);
        delete.setBorderPainted(true);

        // Membuat data untuk tabel
        String[] columnNames = {"ID user", "Nama", "Email"};
        DefaultTableModel model = new DefaultTableModel();
        model.setColumnIdentifiers(columnNames);

        // Membuat tabel dengan model tersebut
        JTable table = new JTable(model);

        // Menambahkan tabel ke dalam JScrollPane
        JScrollPane scrollPane = new JScrollPane(table);

        JPanel panel = new JPanel(new GridBagLayout());

        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(10, 30, 10, 30);

        // Komponen di kolom pertama
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.anchor = GridBagConstraints.NORTH;
        panel.add(create, gbc);

        // komponen kolom kedua
        gbc.gridx = 1;
        gbc.gridy = 0;
        gbc.anchor = GridBagConstraints.NORTH;
        panel.add(view, gbc);

        // komponen kolom ketiga
        gbc.gridx = 2;
        gbc.gridy = 0;
        gbc.anchor = GridBagConstraints.NORTH;
        panel.add(update, gbc);

        // komponen kolom keempat
        gbc.gridx = 3;
        gbc.gridy = 0;
        gbc.anchor = GridBagConstraints.NORTH;
        panel.add(delete, gbc);

        gbc.gridx = 0;
        gbc.gridy = 1;
        gbc.gridwidth = 4;
        gbc.fill = GridBagConstraints.HORIZONTAL;
        gbc.ipady = 100; 
        panel.add(scrollPane, gbc); 
        gbc.ipady = 0;

        frame.add(panel);
        frame.setVisible(true);

        create.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Membuat form untuk update data
                JTextField text_nama = new JTextField();
                JTextField text_gender = new JTextField();
                JTextField text_email = new JTextField();
                JTextField text_phone = new JTextField();
                JTextField text_address = new JTextField();
                JTextField text_date = new JTextField();
                JTextField text_username = new JTextField();
                JTextField text_passwords = new JTextField();

                Object[] message = {
                    "Nama:", text_nama,
                    "Gender:", text_gender,
                    "Email:", text_email,
                    "Phone:", text_phone,
                    "Address:", text_address,
                    "Date:", text_date,
                    "Username:", text_username,
                    "Passwords:", text_passwords
                };
                int option = JOptionPane.showConfirmDialog(frame, message, "Create Data", JOptionPane.OK_CANCEL_OPTION);
                if (option == JOptionPane.OK_OPTION) {
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

                        JOptionPane.showMessageDialog(frame, "Data berhasil dimasukkan ke tabel users.");

                        // Statement stmt = database.createStatement();
                        // String sql_stmt = "SELECT ID_user, Name_user, Email FROM users";
                        // ResultSet rs = stmt.executeQuery(sql_stmt);

                        // // Membersihkan tabel sebelum menampilkan data baru
                        // model.setRowCount(0);

                        // while (rs.next()) {
                        //     int id_user = rs.getInt("ID_user");
                        //     String name_user = rs.getString("Name_user");
                        //     String email_user = rs.getString("Email");

                        //     // Menambahkan baris ke dalam model tabel
                        //     model.addRow(new Object[]{id_user, name_user, email_user});
                        // }

                        database.close();
                    } catch (SQLException ex) {
                        JOptionPane.showMessageDialog(frame, "Kesalahan database: " + ex.getMessage());
                    } catch (NumberFormatException ex) {
                        JOptionPane.showMessageDialog(frame, "Inputan salah");
                    }
                }
            }
        });

        view.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    Connection conn = koneksi.connect();
                    Statement stmt = conn.createStatement();
                    String sql = "SELECT ID_user, Name_user, Email FROM users";
                    ResultSet rs = stmt.executeQuery(sql);

                    // Membersihkan tabel sebelum menampilkan data baru
                    model.setRowCount(0);

                    while (rs.next()) {
                        int id_user = rs.getInt("ID_user");
                        String name_user = rs.getString("Name_user");
                        String email_user = rs.getString("Email");

                        // Menambahkan baris ke dalam model tabel
                        model.addRow(new Object[]{id_user, name_user, email_user});
                    }
                    conn.close();
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
            }
        });

        update.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Implementasi untuk update data
                int selectedRow = table.getSelectedRow();
                if (selectedRow >= 0) {
                    int id_user = (int) model.getValueAt(selectedRow, 0);
                    String name_user = (String) model.getValueAt(selectedRow, 1);
                    String email_user = (String) model.getValueAt(selectedRow, 2);

                    // Membuat form untuk update data
                    JTextField newNameField = new JTextField(name_user);
                    JTextField newEmailField = new JTextField(email_user);
                    Object[] message = {
                        "Nama:", newNameField,
                        "Email:", newEmailField
                    };

                    int option = JOptionPane.showConfirmDialog(frame, message, "Update Data", JOptionPane.OK_CANCEL_OPTION);
                    if (option == JOptionPane.OK_OPTION) {
                        String newName = newNameField.getText();
                        String newEmail = newEmailField.getText();

                        // Update data di database
                        try {
                            Connection conn = koneksi.connect();
                            String sql = "UPDATE users SET Name_user = ?, Email = ? WHERE ID_user = ?";
                            PreparedStatement pstmt = conn.prepareStatement(sql);
                            pstmt.setString(1, newName);
                            pstmt.setString(2, newEmail);
                            pstmt.setInt(3, id_user);
                            pstmt.executeUpdate();
                            conn.close();

                            // Update data di tabel
                            model.setValueAt(newName, selectedRow, 1);
                            model.setValueAt(newEmail, selectedRow, 2);

                            JOptionPane.showMessageDialog(frame, "Data berhasil diupdate.");
                        } catch (SQLException ex) {
                            JOptionPane.showMessageDialog(frame, "Error saat update data: " + ex.getMessage());
                        }
                    }
                } else {
                    JOptionPane.showMessageDialog(frame, "Pilih baris yang ingin diupdate!");
                }
            }
        });

        delete.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Implementasi untuk hapus data
                int selectedRow = table.getSelectedRow();
                if (selectedRow >= 0) {
                    int option = JOptionPane.showConfirmDialog(frame, "Apakah ingin menghapus data ?", "Delete Data", JOptionPane.OK_CANCEL_OPTION);
                    if (option == JOptionPane.OK_OPTION){
                        int id_user = (int) model.getValueAt(selectedRow, 0);
                        try {
                            Connection database = koneksi.connect();
                            String sql = "DELETE FROM users WHERE ID_user = ?";
                            PreparedStatement pstmt = database.prepareStatement(sql);

                            pstmt.setInt(1, id_user);

                            pstmt.executeUpdate();
                            database.close();

                            JOptionPane.showMessageDialog(frame, "Data berhasil dihapus.");
                            model.removeRow(selectedRow); // Menghapus baris dari tabel
                        } catch (SQLException ex) {
                            JOptionPane.showMessageDialog(frame, "Error saat hapus data: " + ex.getMessage());
                        }
                    }
                } else {
                    JOptionPane.showMessageDialog(frame, "Pilih baris yang ingin dihapus!");
                }
            }
        });
    }
}
