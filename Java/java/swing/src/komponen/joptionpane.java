package komponen;

import javax.swing.*;

public class joptionpane {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Contoh JOptionPane");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel();
        frame.add(panel);

        frame.setVisible(true);

        JTextField text_nama = new JTextField();
        Object[] message = {
            "Nama:", text_nama
        };
        int angka = JOptionPane.showConfirmDialog(frame, message, "data", JOptionPane.OK_CANCEL_OPTION, JOptionPane.INFORMATION_MESSAGE);
        
        if (angka == 0){
            System.out.println("klik ok");
        }
        else if(angka == 2){
            System.out.println("klik cancel");
        }
    }
}

