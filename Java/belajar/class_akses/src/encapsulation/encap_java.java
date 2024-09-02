package encapsulation;

class Person {
    private String name;
    private int age;

    public void setName(String name) { // setters (menggunakan fungsi void)
        this.name = name;
    }

    public String getName() { // getters (menggunakan fungsi return)
        return name;
    }

    public void setAge(int age) { // setters (menggunakan fungsi void)
        if (age > 0) {
            this.age = age;
        } else {
            System.out.println("Invalid age!");
        }
    }

    public int getAge() { // getters (menggunakan fungsi return)
        return age;
    }
}

public class encap_java {
    public static void main(String[] args) {
        Person data = new Person();

        data.setName("john");
        String nama = data.getName();
        System.out.println(nama);
    }
}
