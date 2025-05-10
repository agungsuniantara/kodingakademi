import java.io.File;
import java.io.PrintWriter;
import java.util.Scanner;

public class file_processing {
    public static void main(String[] args) {
        try {
            // 1. List all files in mydata directory
            File mydataDir = new File("mydata");
            System.out.println("Isi folder mydata:");
            for (File file : mydataDir.listFiles()) {
                System.out.println(file.getName());
            }

            // 2. List all .txt files in each subfolder of 2019
            File year2019Dir = new File("mydata/2019");
            String[] subFolders = {"januari", "februari", "maret"};
            
            for (String folder : subFolders) {
                File subFolder = new File(year2019Dir, folder);
                System.out.println("\nFile .txt di folder " + folder + ":");
                
                if (subFolder.exists() && subFolder.isDirectory()) {
                    boolean foundTxt = false;
                    for (File file : subFolder.listFiles()) {
                        if (file.getName().endsWith(".txt")) {
                            System.out.println(file.getName());
                            foundTxt = true;
                        }
                    }
                    if (!foundTxt) {
                        System.out.println("Tidak ada file .txt");
                    }
                } else {
                    System.out.println("Folder " + folder + " tidak ditemukan");
                }
            }

            // 3. Create mynumber.txt and copy numbers from all subfolders
            File outputFile = new File("mydata/mynumber.txt");
            PrintWriter writer = new PrintWriter(outputFile);

            for (String folder : subFolders) {
                File subFolder = new File(year2019Dir, folder);
                if (subFolder.exists() && subFolder.isDirectory()) {
                    for (File file : subFolder.listFiles()) {
                        if (file.getName().endsWith(".txt")) {
                            Scanner scanner = new Scanner(file);
                            while (scanner.hasNext()) {
                                String word = scanner.next();
                                if (word.matches("\\d+")) {
                                    writer.println(word);
                                }
                            }
                            scanner.close();
                        }
                    }
                }
            }
            writer.close();
            
            System.out.println("\nAngka-angka telah disalin ke mynumber.txt");

        } catch (Exception e) {
            System.out.println("Terjadi kesalahan: " + e.getMessage());
        }
    }
}
