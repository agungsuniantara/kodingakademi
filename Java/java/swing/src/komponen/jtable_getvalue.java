package komponen;

import javax.swing.*;
import javax.swing.table.*;
import java.awt.event.*;

public class jtable_getvalue {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Contoh JTable");
        frame.setSize(500, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JButton view = new JButton("view");

        String[] columnNames = {"Kolom 1", "Kolom 2", "Kolom 3"};
        DefaultTableModel model = new DefaultTableModel();
        model.setColumnIdentifiers(columnNames);
        model.setRowCount(0);
        model.addRow(new Object[]{"1", "john", "john@gmail.com"});
        model.addRow(new Object[]{"2", "daniel", "daniel@gmail.com"});

        JTable table = new JTable(model);
        JScrollPane scrollPane = new JScrollPane(table);

        JPanel panel = new JPanel();
        panel.add(view);
        panel.add(scrollPane);
        frame.add(panel);

        frame.setVisible(true);

        view.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Implementasi untuk update data
                int selectedRow = table.getSelectedRow();
                if (selectedRow >= 0) {
                    String id_user = (String) model.getValueAt(selectedRow, 0);
                    String name_user = (String) model.getValueAt(selectedRow, 1);
                    String email_user = (String) model.getValueAt(selectedRow, 2);
                    JOptionPane.showMessageDialog(frame, "ID: " + id_user + ", Nama: " + name_user + ", Email: " + email_user);
                } 
            }
        });
    }

}

