import javax.swing.JButton;
import javax.swing.JFrame;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

class MyFrame extends JFrame {
    private JButton myButton;

    public MyFrame(String title) {
        super(title);

        // Membuat objek tombol
        myButton = new JButton("Klik Saya");

        // Menambahkan listener untuk menangani kejadian klik pada tombol
        myButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.out.println("Tombol diklik!");
            }
        });

        // Menambahkan tombol ke frame
        add(myButton);

        // Mengatur operasi standar ketika frame ditutup
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Mengatur layout manager menjadi FlowLayout agar komponen ditempatkan secara otomatis
        setLayout(new FlowLayout());

        // Mengatur ukuran frame
        setSize(300, 200);

        // Mengatur frame agar ditampilkan di tengah layar
        setLocationRelativeTo(null);

        // Menampilkan frame
        setVisible(true);
    }
}

public class GUI_OOP {
    public static void main(String[] args) {
        // Membuat objek frame
        MyFrame myFrame = new MyFrame("Contoh Swing OOP");

        // Menutup frame saat tombol ditutup
        myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
