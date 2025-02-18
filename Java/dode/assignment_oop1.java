class employee {
    String name;
    double salary;

    public employee(String name, double salary){
        this.name = name;
        this.salary = salary;
    }

    public String get_name(){
        return this.name;
    }

    public double get_salary(){
        return this.salary;
    }

    public double raiseSalary(double rate){
        double plus = this.salary + (this.salary * rate);
        this.salary = plus;
        return plus;
    }

    public static double tripleSalary(double salary){
        return salary * 3;
    }
}

public class assignment_oop1 {
    public static void main(String[] args) {
        employee E1 = new employee("Ali", 1000000);
        System.out.println(E1.get_salary());
        E1.raiseSalary(0.1);
        System.out.println(E1.get_salary());
        System.out.println(employee.tripleSalary(E1.get_salary()));

        for (int i = 0; i < 5; i++){
            for (int z = 0; z < 5; z++){
                if (i >= z){
                    System.out.print("*");
                }
            }
            System.out.println("");
        }
    }
}
