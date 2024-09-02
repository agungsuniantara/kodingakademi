package komponen;

import javax.swing.*;
import javax.swing.table.*;

public class jtable_getvalue2 {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Contoh JTable");
        frame.setSize(500, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        String[] columnNames = {"Kolom 1", "Kolom 2", "Kolom 3"};
        DefaultTableModel model = new DefaultTableModel();
        model.setColumnIdentifiers(columnNames);
        model.setRowCount(0);
        model.addRow(new Object[]{"1", "john", "john@gmail.com"});
        model.addRow(new Object[]{"2", "daniel", "daniel@gmail.com"});

        model.setValueAt("10", 1, 0); 
        model.setValueAt("michael", 1, 1); 
        model.setValueAt("michael@gmail.com", 1, 2); 

        JTable table = new JTable(model);
        JScrollPane scrollPane = new JScrollPane(table);

        JPanel panel = new JPanel();
        panel.add(scrollPane);
        frame.add(panel);

        frame.setVisible(true);

        for (int i = 0; i < model.getRowCount(); i++) {
            String id_user = (String) model.getValueAt(i, 0);
            String name_user = (String) model.getValueAt(i, 1);
            String email_user = (String) model.getValueAt(i, 2);
            System.out.println("ID: " + id_user + ", Nama: " + name_user + ", Email: " + email_user);
        }
    }

}

