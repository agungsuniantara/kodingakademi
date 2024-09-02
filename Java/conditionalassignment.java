import java.util.Scanner;

public class conditionalassignment
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		int year = 0;
		
		System.out.println("how much money do you have : ");
		int balance = in.nextInt();
		
		System.out.println("how much you get pay : ");
		int salary = in.nextInt();
		
		System.out.println("how much money do you need to retire : ");
		int retire = in.nextInt();
		
		System.out.println("interest rate in % : ");
		int interest = in.nextInt();
		
		while (balance < retire){
			balance += salary;
			double bunga = balance * interest / 100;
			balance += bunga;
			year += 1;
		}
		
		System.out.println("you can retire in : " + year + " years");
	}
}