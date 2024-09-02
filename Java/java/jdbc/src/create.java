import java.sql.*;

public class create {
    public static void main(String[] args) {
        try {
            Connection database = koneksi.connect();
            String sql = "INSERT INTO users (Name_user, Gender, Email, Phone, Address, Date_of_birth, Username, Passwords) VALUES (?, ?, ?, ?, ?, ?, ?, ?)";
            PreparedStatement pstmt = database.prepareStatement(sql);

            pstmt.setString(1, "Jono"); // Name_user
            pstmt.setString(2, "laki-laki"); // Gender
            pstmt.setString(3, "jono@gmail.com"); // Email
            pstmt.setString(4, "78674556"); // Phone
            pstmt.setString(5, "ubud"); // Address
            pstmt.setString(6, "1997-05-05"); // Date_of_birth
            pstmt.setString(7, "jono"); // Username
            pstmt.setString(8, "jono"); // Passwords

            pstmt.executeUpdate();

            System.out.println("Data berhasil dimasukkan ke tabel users.");
            database.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
