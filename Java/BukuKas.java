import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import javax.swing.table.Table;

class Transaksi {

    private String tanggal;
    private String jenis;
    private int nominal;
    private String keterangan;

    public Transaksi(String tanggal, String jenis, int nominal, String keterangan) {
        this.tanggal = tanggal;
        this.jenis = jenis;
        this.nominal = nominal;
        this.keterangan = keterangan;
    }

    public String getTanggal() {
        return tanggal;
    }

    public void setTanggal(String tanggal) {
        this.tanggal = tanggal;
    }

    public String getJenis() {
        return jenis;
    }

    public void setJenis(String jenis) {
        this.jenis = jenis;
    }

    public int getNominal() {
        return nominal;
    }

    public void setNominal(int nominal) {
        this.nominal = nominal;
    }

    public String getKeterangan() {
        return keterangan;
    }

    public void setKeterangan(String keterangan) {
        this.keterangan = keterangan;
    }
}

public class BukuKas extends Frame implements ActionListener {

    // Komponen GUI
    Label lblJudul, lblTanggal, lblJenis, lblNominal, lblKeterangan;
    TextField txtTanggal, txtJenis, txtNominal, txtKeterangan;
    Button btnAdd, btnList, btnExit;
    Table tblTransaksi;

    // Data transaksi
    ArrayList<Transaksi> listTransaksi = new ArrayList<>();

    public BukuKas() {
        // Pengaturan frame
        setTitle("Buku Kas Sederhana");
        setSize(400, 300);
        setLayout(new FlowLayout());

        // Menambahkan komponen GUI
        lblJudul = new Label("Buku Kas Sederhana");
        lblTanggal = new Label("Tanggal:");
        lblJenis = new Label("Jenis:");
        lblNominal = new Label("Nominal:");
        lblKeterangan = new Label("Keterangan:");
        txtTanggal = new TextField(10);
        txtJenis = new TextField(10);
        txtNominal = new TextField(10);
        txtKeterangan = new TextField(20);
        btnAdd = new Button("Tambah");
        btnList = new Button("Daftar");
        btnExit = new Button("Keluar");
        tblTransaksi = new Table();

        add(lblJudul);
        add(lblTanggal);
        add(txtTanggal);
        add(lblJenis);
        add(txtJenis);
        add(lblNominal);
        add(txtNominal);
        add(lblKeterangan);
        add(txtKeterangan);
        add(btnAdd);
        add(btnList);
        add(btnExit);
        add(tblTransaksi);

        // Menambahkan ActionListener
        btnAdd.addActionListener(this);
        btnList.addActionListener(this);
        btnExit.addActionListener(this);

        // Menambahkan kolom ke tabel
        tblTransaksi.addColumn("Tanggal");
        tblTransaksi.addColumn("Jenis");
        tblTransaksi.addColumn("Nominal");
        tblTransaksi.addColumn("Keterangan");
    }

    public void actionPerformed(ActionEvent e) {
        // Menangani aksi tombol
        if (e.getSource() == btnAdd) {
            // Menambahkan transaksi baru
            String tanggal = txtTanggal.getText();
            String jenis = txtJenis.getText();
            int nominal = Integer.parseInt(txtNominal.getText());
            String keterangan = txtKeterangan.getText();

            Transaksi transaksi = new Transaksi(tanggal, jenis, nominal, keterangan);
            listTransaksi.add(transaksi);

            // Menampilkan pesan
            System.out.println("Transaksi berhasil ditambahkan!");
        } else if (e.getSource() == btnList) {
            // Menampilkan daftar transaksi
            for (Transaksi transaksi : listTransaksi) {
                System.out.println(transaksi.getTanggal() + " - " + transaksi.getJenis() + " - " + transaksi.getNominal() + " - " + transaksi.getKeterangan());
            }
        } else if (e.getSource() == btnExit) {
            // Keluar dari program
            System.exit(0);
        }
    }

    public static void main(String[] args) {
        // Menjalankan program
        BukuKas bk = new BukuKas();
        bk.setVisible(true);
    }
}

