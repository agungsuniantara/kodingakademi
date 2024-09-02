import java.sql.*;

public class koneksi {
    public static Connection connect() {
        String url = "jdbc:mysql://localhost:3306/data";
        String user = "root";
        String password = "";
        Connection conn = null;
        try {
            conn = DriverManager.getConnection(url, user, password);
        } catch (SQLException e) {
            System.out.println("SQLException: " + e.getMessage());
        }
        return conn;
    }
}

