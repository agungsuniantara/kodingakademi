package position;
import javax.swing.*;
import java.awt.*;

public class assignment {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Buku kas");
        frame.setSize(400, 550);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JLabel pendapatan = new JLabel("Pendapatan : ");
        JLabel pengeluaran = new JLabel("Pengeluaran : ");
        JLabel profit = new JLabel("Profit : ");
        JLabel nama_barang = new JLabel("Nama barang :");
        JLabel harga_barang = new JLabel("Harga barang :");
        JLabel list_barang = new JLabel("List barang :");
        JLabel search = new JLabel("Search :");

        JLabel hasil_pendapatan = new JLabel("Rp 0");
        JLabel hasil_pengeluaran = new JLabel("Rp 0");
        JLabel hasil_profit = new JLabel("Rp 0");

        JTextArea textArea = new JTextArea(5, 20);
        textArea.setLineWrap(true); 
        textArea.setWrapStyleWord(true);
        JScrollPane scrollPane = new JScrollPane(textArea); 

        JButton transaksi = new JButton("Transaksi");
        JButton pembayaran = new JButton("Pembayaran");
        JButton clear = new JButton("Clear");

        JTextField text_barang = new JTextField(20);
        JTextField text_harga = new JTextField(20);
        JTextField text_search = new JTextField(20);

        JPanel panel = new JPanel(new GridBagLayout());

        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(10, 10, 10, 10);

        // Komponen di kolom pertama
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(pendapatan, gbc);

        gbc.gridy = 1;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(pengeluaran, gbc);

        gbc.gridy = 2;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(profit, gbc);
        
        gbc.gridy = 3;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(nama_barang, gbc);

        gbc.gridy = 4;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(harga_barang, gbc);

        gbc.gridy = 7;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(list_barang, gbc);

        gbc.gridy = 8;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(search, gbc);

        // Komponen di kolom kedua
        gbc.gridx = 1;
        gbc.gridy = 0;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(hasil_pendapatan, gbc);

        gbc.gridx = 1;
        gbc.gridy = 1;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(hasil_pengeluaran, gbc);

        gbc.gridx = 1;
        gbc.gridy = 2;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(hasil_profit, gbc);

        gbc.gridx = 1;
        gbc.gridy = 3;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(text_barang, gbc);

        gbc.gridx = 1;
        gbc.gridy = 4;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(text_harga, gbc);

        gbc.gridx = 0;
        gbc.gridy = 5;
        gbc.gridwidth = 2;
        gbc.fill = GridBagConstraints.HORIZONTAL;
        panel.add(transaksi, gbc);

        gbc.gridx = 0;
        gbc.gridy = 6;
        gbc.gridwidth = 2;
        gbc.fill = GridBagConstraints.HORIZONTAL;
        panel.add(pembayaran, gbc);

        gbc.gridx = 1;
        gbc.gridy = 8;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(text_search, gbc);

        gbc.gridx = 0;
        gbc.gridy = 9;
        gbc.gridwidth = 2;
        gbc.fill = GridBagConstraints.HORIZONTAL;
        panel.add(scrollPane, gbc);

        gbc.gridx = 0;
        gbc.gridy = 10;
        gbc.gridwidth = 2;
        gbc.fill = GridBagConstraints.HORIZONTAL;
        panel.add(clear, gbc);

        frame.add(panel);
        frame.setVisible(true);
    }
}
