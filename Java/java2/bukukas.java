import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.io.*;

public class bukukas extends JFrame implements ActionListener {

    // Komponen GUI
    Label lblJudul, txtPengeluaran, txtPendapatan, hasilPendapatan, hasilPengeluaran, txtBarang, txtHarga, txtList, txtProfit, txtHasilProfit, txtSearch;
    TextField barang, harga, search;
    Button btnTransaksi, btnPembayaran, clearButton;
    JTextArea listArea;
    
    Transaksi transaksi = new Transaksi();
	int previousProfit = 0;
	int total_pendapatan = 0;

    public bukukas() {
        // Pengaturan frame
        setTitle("buku kas");
        setSize(400, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Menambahkan komponen ke frame menggunakan GridBagLayout
        setLayout(new GridBagLayout());
        GridBagConstraints c = new GridBagConstraints();
        
        // Mengatur tampilan di sebelah kiri
        c.anchor = GridBagConstraints.WEST;
        
        c.insets = new Insets(5, 5, 5, 5);
        
        c.gridy++;
        c.gridx = 0;
        c.gridwidth = 1;
        c.fill = GridBagConstraints.NONE;
        add(txtPendapatan = new Label("Pendapatan : "), c);
        
        c.gridx++;
        c.fill = GridBagConstraints.HORIZONTAL;
        add(hasilPendapatan = new Label("Rp 0"), c);
        
        c.gridy++;
        c.gridx = 0;
        c.fill = GridBagConstraints.NONE;
        add(txtPengeluaran = new Label("Pengeluaran : "), c);
        
        c.gridx++;
        c.fill = GridBagConstraints.HORIZONTAL;
        add(hasilPengeluaran = new Label("Rp 0"), c);
        
        c.gridy++;
        c.gridx = 0;
        c.fill = GridBagConstraints.NONE;
        add(txtProfit = new Label("Profit : "), c);
        
        c.gridx++;
        c.fill = GridBagConstraints.HORIZONTAL;
        add(txtHasilProfit = new Label("Rp 0"), c);
        
        c.gridy++;
        c.gridx = 0;
        c.fill = GridBagConstraints.NONE;
        add(txtBarang = new Label("Nama barang : "), c);
        
        c.gridx++;
        c.fill = GridBagConstraints.HORIZONTAL;
        add(barang = new TextField(20), c);
        
        c.gridy++;
        c.gridx = 0;
        c.fill = GridBagConstraints.NONE;
        add(txtHarga = new Label("Harga barang : "), c);
        
        c.gridx++;
        c.fill = GridBagConstraints.HORIZONTAL;
        add(harga = new TextField(20), c);
        
        // Tombol login dan keluar
        c.gridy++;
        c.gridx = 1;
        add(btnTransaksi = new Button("Transaksi"), c);
        
        c.gridy++;
        c.gridx = 1;
        add(btnPembayaran = new Button("Pembayaran"), c);
        
        c.gridy++;
        c.gridx = 0;
        add(txtList = new Label("List barang : "), c);
        
        c.gridy++;
        c.gridx = 0;
        c.fill = GridBagConstraints.NONE;
        add(txtSearch = new Label("Search : "), c);
        
        c.gridx++;
        c.fill = GridBagConstraints.HORIZONTAL;
        add(search = new TextField(20), c);
        
        c.gridy++;
        c.gridx = 0;
        c.gridwidth = 10;
        listArea = new JTextArea(10, 20);
        listArea.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(listArea);
        add(scrollPane, c);
		
		c.gridy++;
        c.gridx = 0;
        add(clearButton = new Button("Clear"), c);

        // Menambahkan ActionListener
        btnTransaksi.addActionListener(this);
        btnPembayaran.addActionListener(this);
		clearButton.addActionListener(this);
        
        // Memuat data dari file transaksi.txt saat aplikasi dimulai
        loadDataFromFile();
        loadProfitFromFile();
		loadPendapatanFromFile();
        
        // Menambahkan ActionListener untuk pencarian
        search.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Memanggil metode pencarian saat pengguna menekan tombol enter pada TextField pencarian
                String keyword = search.getText();
                searchInList(keyword);
            }
        });
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == btnTransaksi) {
            String namaBarang = barang.getText();
        int hargaBarang = Integer.parseInt(harga.getText());
        
        // Melakukan transaksi
        transaksi.tambahTransaksi(namaBarang, hargaBarang);
        
        // Menampilkan daftar transaksi dan hasil pendapatan
        listArea.setText(transaksi.getListTransaksi());
        hasilPendapatan.setText("Rp " + String.valueOf(transaksi.getTotalPendapatan()));

        // Menghitung profit
        int profit = transaksi.getProfit() + previousProfit;
        txtHasilProfit.setText("Rp " + String.valueOf(profit));
        
        // Menyimpan profit sebelumnya
        previousProfit = profit;

        int pendapatan = transaksi.getTotalPendapatan();
        hasilPendapatan.setText("Rp " + String.valueOf(pendapatan));
        
        total_pendapatan = pendapatan;
        
        saveDataToFile();
        saveProfitToFile(); // Menyimpan profit ke file
        savePendapatanToFile(); 
            
        } else if (e.getSource() == btnPembayaran) {
            String namaBarang = barang.getText();
        int hargaBarang = Integer.parseInt(harga.getText());
        
        // Melakukan pembayaran
        transaksi.tambahPembayaran(namaBarang, hargaBarang);
        
        // Menampilkan daftar transaksi dan hasil pendapatan
        listArea.setText(transaksi.getListTransaksi());
        hasilPengeluaran.setText("Rp " + String.valueOf(transaksi.getTotalPengeluaran()));
        
        // Menghitung profit
        int profit = transaksi.getProfit() + previousProfit;
        txtHasilProfit.setText("Rp " + String.valueOf(profit));

        // Menyimpan profit sebelumnya
        previousProfit = profit;

        int pendapatan = transaksi.getTotalPendapatan();
        hasilPendapatan.setText("Rp " + String.valueOf(pendapatan));
        
        total_pendapatan = pendapatan;
        
        saveDataToFile();
        saveProfitToFile(); // Menyimpan profit ke file
        savePendapatanToFile();
			
        } else if (e.getSource() == clearButton) {
           // Menghapus semua data dari list transaksi
        transaksi.clearTransaksi();

        // Menampilkan daftar transaksi yang sudah dikosongkan
        listArea.setText("");

        // Mengatur ulang total pendapatan dan pengeluaran menjadi 0
        hasilPendapatan.setText("Rp 0");
        hasilPengeluaran.setText("Rp 0");

        // Mengatur ulang nilai profit menjadi 0
        txtHasilProfit.setText("Rp 0");
        previousProfit = 0; // Menyimpan profit sebelumnya menjadi 0
        total_pendapatan = 0;

        // Menyimpan data terkini setelah membersihkan list
        saveDataToFile();
        saveProfitToFile(); // Menyimpan profit ke file
        savePendapatanToFile();
		}
    }

     public static void main(String[] args) {
        // Menjalankan program
        bukukas buku = new bukukas();
        buku.loadProfitFromFile(); // Memuat profit sebelumnya saat program dimulai
        buku.setVisible(true);
    }
    
    private void saveDataToFile() {
        File file = new File("transaksi.txt");
		try (PrintWriter writer = new PrintWriter(new FileWriter(file))) {
			String listTransaksi = transaksi.getListTransaksi();
			if (!listTransaksi.isEmpty()) {
				writer.print(listTransaksi);
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
    }
    
    // Metode untuk memuat data dari file teks saat aplikasi dimulai
    private void loadDataFromFile() {
        try (BufferedReader reader = new BufferedReader(new FileReader("transaksi.txt"))) {
            String line;
            StringBuilder content = new StringBuilder();
            while ((line = reader.readLine()) != null) {
                content.append(line).append("\n");
            }
            listArea.setText(content.toString());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
	
	// Metode untuk menyimpan profit ke file teks
    private void saveProfitToFile() {
        File file = new File("profit.txt");
        try (PrintWriter writer = new PrintWriter(new FileWriter(file))) {
            writer.print(previousProfit);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
	
	private void savePendapatanToFile() {
        File file = new File("pendapatan.txt");
		try (PrintWriter writer = new PrintWriter(new FileWriter(file))) {
			writer.print(total_pendapatan);
		} catch (IOException e) {
			e.printStackTrace();
		}
    }
	
	
	// Metode untuk memuat profit dari file teks saat aplikasi dimulai
    private void loadProfitFromFile() {
        try (BufferedReader reader = new BufferedReader(new FileReader("profit.txt"))) {
            String line;
            if ((line = reader.readLine()) != null) {
                previousProfit = Integer.parseInt(line);
                txtHasilProfit.setText("Rp " + String.valueOf(previousProfit)); // Menampilkan profit sebelumnya
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
	
	private void loadPendapatanFromFile() {
        try (BufferedReader reader = new BufferedReader(new FileReader("pendapatan.txt"))) {
            String line;
            if ((line = reader.readLine()) != null) {
                total_pendapatan = Integer.parseInt(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
    private void searchInList(String keyword) {
        // Jika kata kunci pencarian kosong, tampilkan data dari file transaksi.txt
        if (keyword.isEmpty()) {
            loadDataFromFile(); // Memuat data dari file transaksi.txt
            return;
        }
        
        // Mendapatkan teks dari listArea
        String text = listArea.getText(); 
        
        // Membagi teks menjadi baris-baris
        String[] lines = text.split("\n"); // [[ddsadasdasdsa], [dasdasdsa]]
        
        // Membuat string builder untuk menampung hasil pencarian
        StringBuilder result = new StringBuilder();
        
        // Mencari kata kunci dalam setiap baris
        for (String line : lines) {
            if (line.toLowerCase().contains(keyword.toLowerCase())) {
                result.append(line).append("\n");
            }
        }
        
        // Memperbarui listArea dengan hasil pencarian
        listArea.setText(result.toString());
    }
}

class Transaksi {
    private ArrayList<String> daftarBarang = new ArrayList<>();
    private ArrayList<Integer> daftarHarga = new ArrayList<>();
    private int totalPendapatan = 0;
    private int totalPengeluaran = 0;

    public void tambahTransaksi(String namaBarang, int hargaBarang) {
        daftarBarang.add(namaBarang);
        daftarHarga.add(hargaBarang);
        totalPendapatan += hargaBarang;
    }

    public void tambahPembayaran(String namaBarang, int hargaBarang) {
        daftarBarang.add(namaBarang);
        daftarHarga.add(-hargaBarang); // Harga negatif untuk pembayaran
        totalPengeluaran += hargaBarang;
    }

    public String getListTransaksi() {
        StringBuilder listBarang = new StringBuilder();
        for (int i = 0; i < daftarBarang.size(); i++) {
            listBarang.append(daftarBarang.get(i)).append(" - Rp ").append(daftarHarga.get(i)).append("\n");
        }
        return listBarang.toString();
    }

    public int getTotalPendapatan() {
        return totalPendapatan;
    }

    public int getTotalPengeluaran() {
        return totalPengeluaran;
    }

    public int getProfit() {
        return totalPendapatan - totalPengeluaran;
    }
	
	public void clearTransaksi() {
        daftarBarang.clear();
        daftarHarga.clear();
        totalPendapatan = 0;
        totalPengeluaran = 0;
    }
}