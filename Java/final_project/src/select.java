import java.sql.*;

public class select {
    public static void main(String[] args) {
        try {
            Connection conn = koneksi.connect();
            Statement stmt = conn.createStatement();
            String sql = "SELECT * FROM users";
            ResultSet rs = stmt.executeQuery(sql);

            while (rs.next()) {
                int id_user = rs.getInt("ID_user");
                String name_user = rs.getString("Name_user");
                String email_user = rs.getString("Email");

                System.out.println("ID user: " + id_user + ", Name user: " + name_user + ", Email: " + email_user);
            }
            conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
