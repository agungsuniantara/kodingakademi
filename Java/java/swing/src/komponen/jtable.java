package komponen;

import javax.swing.*;
import javax.swing.table.*;

public class jtable {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Contoh JTable");
        frame.setSize(500, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        String[] columnNames = {"Kolom 1", "Kolom 2", "Kolom 3"};
        DefaultTableModel model = new DefaultTableModel();
        model.setColumnIdentifiers(columnNames);
        model.setRowCount(0);
        model.addRow(new Object[]{"Data 1-1", "Data 1-2", "Data 1-3"});
        model.addRow(new Object[]{"Data 2-1", "Data 2-2", "Data 2-3"});

        JTable table = new JTable(model);
        JScrollPane scrollPane = new JScrollPane(table);

        JPanel panel = new JPanel();
        panel.add(scrollPane);
        frame.add(panel);

        frame.setVisible(true);
    }
}

