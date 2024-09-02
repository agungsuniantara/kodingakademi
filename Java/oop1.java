public class oop1
{
	String brands = "honda";
	double price = 200000;
	String nama;
	
	public static void main(String[] args)
	{
		oop1 car = new oop1();
		System.out.println(car.brands);
		System.out.println(car.price);
		car.nama = "agung";
		System.out.println(car.nama);
		
		oop1 motor = new oop1();
		motor.nama = "wahyu";
		System.out.println(motor.nama);
	}
}