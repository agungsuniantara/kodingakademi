import java.sql.*;

public class delete {
    public static void main(String[] args) {
        try {
            Connection database = koneksi.connect();
            String sql = "DELETE FROM users WHERE Username = ?";
            PreparedStatement pstmt = database.prepareStatement(sql);

            pstmt.setString(1, "budi");

            int affectedRows = pstmt.executeUpdate();

            if (affectedRows > 0) {
                System.out.println("Data berhasil dihapus dari tabel users.");
            } else {
                System.out.println("Tidak ada data yang dihapus.");
            }
            database.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
    
