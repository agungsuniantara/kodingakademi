import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class latihan
{
	public static void main(String[] args){
		
		// List interface : Menyimpan elemen berurutan.
		
		List<String> data_list = new ArrayList<>();
		
		System.out.println(data_list);
		
		// metode add
		
		data_list.add("apple");
		data_list.add("pisang");
		
		System.out.println(data_list);
		
		// metode add index
		
		data_list.add(1,"pepaya");
		
		System.out.println(data_list);
		
		// metode get
		
		String data_apel = data_list.get(0);
		
		System.out.println(data_apel);
		
		// metode size
		
		int ukuran = data_list.size();
		
		System.out.println(ukuran);
		
		// metode remove
		
		data_list.remove(0);
		
		System.out.println(data_list);
		
		// metode contains
		
		boolean ada = data_list.contains("pisang");
		
		System.out.println(ada);
		
		// metode isEmpty
		
		boolean kosong = data_list.isEmpty();
		
		System.out.println(kosong);
		
		// metode indexOf
		
		int index_pisang = data_list.indexOf("pisang");
		
		System.out.println(index_pisang);
		
		// metode clear
		
		data_list.clear();
		
		System.out.println(data_list);
		
		// metode toArray
		
		data_list.add("apple");
		data_list.add("pisang");
		
		String[] array_data = data_list.toArray(new String[0]);
		
		// iterasi untuk data array 
		for(int i = 0; i < array_data.length; i++){
			System.out.println(array_data[i]);
		}
		
		// iterasi untuk data list
		for(String tampil : data_list){
			System.out.println(tampil);
		}
	}
}