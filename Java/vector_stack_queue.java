import java.util.Vector;
import java.util.Stack;
import java.util.LinkedList;
import java.util.Queue;

public class vector_stack_queue
{
	public static void main(String[] args){
		
		// vector
		Vector<String> vector = new Vector<>();

        // Menambahkan elemen
        vector.add("Elemen 1");
        vector.add("Elemen 2");

        // Mengakses elemen
        System.out.println("Elemen pertama: " + vector.get(0));

        // Iterasi melalui elemen
        for (String element : vector) {
            System.out.println(element);
        }
		
		
		// stack
		Stack<String> stack = new Stack<>();

        // Menambahkan elemen
        stack.push("Elemen 1");
        stack.push("Elemen 2");

        // Mengambil elemen
        System.out.println("Elemen teratas: " + stack.peek());

        // Menghapus elemen
        System.out.println("Elemen yang dihapus: " + stack.pop());
		
		
		// queue
		 Queue<String> queue = new LinkedList<>();

        // Menambahkan elemen
        queue.offer("Elemen 1");
        queue.offer("Elemen 2");

        // Mengambil elemen
        System.out.println("Elemen pertama: " + queue.peek());

        // Menghapus elemen
        System.out.println("Elemen yang dihapus: " + queue.poll());
	}
}