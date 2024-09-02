import java.util.LinkedList;
import java.util.Iterator;

public class latihan2
{
	public static void main(String[] args){
		
		LinkedList<String> data = new LinkedList<>();
		
		// metode add
		
		data.add("apple");
		data.add("pisang");
		data.add("pepaya");
		
		System.out.println(data);
		
		// metode add first
		
		data.addFirst("kangkung");
		
		System.out.println(data);
		
		// metode add last
		
		data.addLast("jeruk");
		
		System.out.println(data);
		
		// metode add index
		
		data.add(2, "bayam");
		
		System.out.println(data);
		
		// metode remove first
		
		String first = data.removeFirst();
		
		System.out.println(first);
		System.out.println(data);
		
		// metode remove last
		
		String last = data.removeLast();
		
		System.out.println(last);
		System.out.println(data);
		
		// metode remove value
		
		data.remove("pisang");
		
		System.out.println(data);
		
		// metode remove index
		
		data.remove(0);
		
		System.out.println(data);
		
		// metode get
		
		String bayam = data.get(0);
		
		System.out.println(bayam);
		
		// metode set
		
		data.set(1, "manggis");
		
		System.out.println(data);
		
		// metode iterator 
		
		Iterator<String> iterator = data.iterator();
        while (iterator.hasNext()) {
            String forwardElement = iterator.next();
            System.out.println("Forward Iteration: " + forwardElement);
        }
		
		// metode iterator descending
		
		Iterator<String> descendingIterator = data.descendingIterator();
        while (descendingIterator.hasNext()) {
            String backwardElement = descendingIterator.next();
            System.out.println("Backward Iteration: " + backwardElement);
        }
	}
}