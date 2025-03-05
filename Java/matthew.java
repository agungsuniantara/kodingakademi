class employee{
    String nama;
    double salary;

    public employee(String a, double b){
        this.nama = a;
        this.salary = b;
    }
    public String get_nama(){
        return this.nama;
    }
    public double get_salary(){
        return this.salary;
    }
    public static double triple(double salary){
        double hasil = salary * 3;
        return hasil;
    }

    public static void tukar(employee account1, employee account2){
        account1.nama = account2.nama;
    }
}

public class matthew {
    public static void main(String[] args) {
        employee data1 = new employee("matthew", 1000000);
        employee data2 = new employee("agung", 2000000);

        employee.tukar(data1, data2);
        System.out.println(data1.get_nama());
    }
}
