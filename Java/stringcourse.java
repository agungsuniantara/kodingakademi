public class stringcourse
{
   public static void main(String[] args)
   {
      String kata = "Hello";
	  String kata2 = "Agar";
	  String kata3 = "Java".repeat(3);
	  String kata4 = "koko";
	  String kata5 = "aku dia mereka";
	  
	  String s = kata.substring(0, 3);
	  String plus = kata + kata2;
	  
	  System.out.println(s);
	  System.out.println(plus);
	  System.out.println(kata3);
	  System.out.println(kata4.length());
	  System.out.println(kata4.toUpperCase());
	  System.out.println(kata4.toLowerCase());
	  System.out.println(kata5.indexOf("dia"));
	  System.out.println(kata4 + "\n" + kata5);
	  
	  StringBuilder builder = new StringBuilder();
	  builder.append('a');
	  builder.append(" big tree is on my garden ");
	  String completedString = builder.toString();
	  
	  System.out.println(completedString);
	  
	  int Cek_length = kata4.length();
	  
	  if (Cek_length > 4){
		  System.out.println("Panjang string lebih dari 4");
	  }
	  else if(Cek_length < 4){
		  System.out.println("Panjang string kurang dari 4");
	  }
	  else{
		  System.out.println("Panjang string sama dengan 4");
	  }
   }
}