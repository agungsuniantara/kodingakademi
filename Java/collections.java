import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

public class collections
{
	public static void main(String[] args){
		
		
		// Collection class
		
		// List interface : Menyimpan elemen berurutan.
		
		List<String> myList1 = new ArrayList<>();
		myList1.add("Item 1");
		myList1.add("Item 2");
		myList1.add("Item 3");
		
		List<Integer> myList2 = new ArrayList<>();
		myList2.add(1);
		myList2.add(2);
		myList2.add(3);
		
		System.out.println("List: " + myList1);
		System.out.println("List: " + myList2);
		
		System.out.println("data 1 = " + myList1.get(0));
		System.out.println("data 1 = " + myList2.get(0));
		
		// Set interface : Tidak menyimpan elemen duplikat.
		
		Set<Integer> mySet = new HashSet<>();
		mySet.add(1);
		mySet.add(2);
		mySet.add(3);
		mySet.add(2); // Duplikat, tidak akan disimpan

		System.out.println("Set: " + mySet);
		System.out.println("data 1 = " + mySet.get(0));
		
		// Map interface : Menyimpan pasangan kunci-nilai
		
		Map<String, Integer> myMap = new HashMap<>();
		myMap.put("One", 1);
		myMap.put("Two", 2);
		myMap.put("Three", 3);

		System.out.println("Map: " + myMap);
	}
}