public class abstractmain
{
	public static void main(String[] args){
		abstract2 data1 = new abstract2("agung", 20, 5);
		abstract3 data2 = new abstract3("wahyu", 30, 10);
		
		data1.tampil();
		data2.tampil();
		
		data1.suara();
		data2.suara();
	}
}