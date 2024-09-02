package concurrency;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class executor_java implements Runnable {
     private String taskName;

    public executor_java(String taskName) {
        this.taskName = taskName;
    }

    public void run() {
        System.out.println("Executing task: " + taskName);
    }

    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(3); // Maksimum 3 thread
        for (int i = 0; i < 5; i++) {
            executor_java task = new executor_java("Task-" + i);
            executor.submit(task);
        }
        executor.shutdown(); // Menutup executor setelah selesai
    }
}
