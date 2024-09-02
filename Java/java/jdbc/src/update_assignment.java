import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.sql.*;
import javax.swing.table.*;

public class update_assignment {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Update assignment");
        frame.setSize(600, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null); // Menempatkan frame di tengah layar
        
        JButton view = new JButton("view");
        JButton update = new JButton("update");
        view.setBorderPainted(true); // Mengembalikan garis di sekitar tulisan pada button
        update.setBorderPainted(true);

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
        gbc.insets = new Insets(10, 140, 10, 140);

        // Komponen di kolom pertama
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.anchor = GridBagConstraints.NORTH;
        panel.add(view, gbc);

        // komponen kolom ketiga
        gbc.gridx = 1;
        gbc.gridy = 0;
        gbc.anchor = GridBagConstraints.NORTH;
        panel.add(update, gbc);

        gbc.gridx = 0;
        gbc.gridy = 1;
        gbc.gridwidth = 2;
        gbc.fill = GridBagConstraints.HORIZONTAL;
        gbc.ipady = 100; 
        panel.add(scrollPane, gbc); 
        gbc.ipady = 0;

        frame.add(panel);
        frame.setVisible(true);

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
    }
}

