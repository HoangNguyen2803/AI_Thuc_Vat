import java.io.*;
import java.util.*;

public class FlowerList {
    
    // Hàm căn trái thủ công cho String
    public static String padLeft(String str, int width) {
        if (str.length() >= width) return str.substring(0, width);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < (width - str.length()); i++) {
            sb.append(' ');
        }
        sb.append(str);
        return sb.toString();
    }

    public static void main(String[] args) {
        // Mở file "database.txt" và đọc dữ liệu
        File file = new File("database.txt");
        if (!file.exists()) {
            System.out.println("❌ Không thể mở file 'database.txt'");
            return;
        }

        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line;
            boolean hasData = false;

            System.out.println("🌸 Danh sách hoa đã dạy cho AI:");
            System.out.println("---------------------------------------------------------------------");
            System.out.printf("| %-15s | %-20s | %-15s |\n", "Tên (EN)", "Tên tiếng Việt", "Thông số (4)");
            System.out.println("---------------------------------------------------------------------");

            // Đọc từng dòng trong file
            while ((line = br.readLine()) != null) {
                if (line.isEmpty()) continue;

                String[] parts = line.split(",");
                if (parts.length == 6) {
                    String tenHoa = parts[0].trim();
                    String tenTViet = parts[1].trim();
                    String sl = parts[2].trim();
                    String sw = parts[3].trim();
                    String pl = parts[4].trim();
                    String pw = parts[5].trim();

                    String thongso = sl + ", " + sw + ", " + pl + ", " + pw;

                    // In thông tin từng dòng
                    System.out.printf("| %-15s | %-20s | %-15s |\n", padLeft(tenHoa, 15), padLeft(tenTViet, 20), padLeft(thongso, 15));

                    hasData = true;
                }
            }

            if (!hasData) {
                System.out.println("|     (Không có dữ liệu hoa nào để hiển thị)                         |");
            }

            System.out.println("---------------------------------------------------------------------");
        } catch (IOException e) {
            System.out.println("❌ Lỗi khi đọc file: " + e.getMessage());
        }
    }
}