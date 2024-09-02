public class assignment_oop2 {
    private String id;
    private String name;
    private int balance = 0;

    public assignment_oop2(String id, String name, int balance) {
        this.id = id;
        this.name = name;
        this.balance = balance;
    }

    public String getID() {
        return this.id;
    }

    public String getName() {
        return this.name;
    }

    public int getBalance() {
        return this.balance;
    }

    public int credit(int amount) {
        this.balance += amount;
        return this.balance;
    }

    public int debit(int amount) {
        if (amount <= balance) {
            this.balance -= amount;
        } else {
            System.out.println("amount exceeded");
        }
        return this.balance;
    }

    public int transfer(int amount, assignment_oop2 targetAccount) {
        if (amount <= this.balance) {
            this.balance -= amount;
            targetAccount.credit(amount);
        } else {
            System.out.println("amount exceeded");
        }
        return this.balance;
    }

    public String toString() {
        return "Account: id = " + getID() + ", name = " + getName() + ", balance = " + getBalance();
    }

    public static void main(String[] args) {
        assignment_oop2 account1 = new assignment_oop2("1", "agung", 10000);
        assignment_oop2 account2 = new assignment_oop2("2", "dyland", 20000);

        account1.transfer(5000, account2); // Transfer 5000 from agung to dyland
		
        System.out.println(account1.toString());
        System.out.println(account2.toString());
    }
}
