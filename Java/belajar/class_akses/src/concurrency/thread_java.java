package concurrency;

public class thread_java extends Thread{
    private int durationSeconds;

    public thread_java(int durationSeconds) {
        this.durationSeconds = durationSeconds;
    }

    public void run() {
        for (int i = 1; i <= durationSeconds; i++) {
            System.out.println("Elapsed time: " + i + " second(s)");
            try {
                Thread.sleep(2000); // Menunggu 1 detik
            } catch (InterruptedException e) {
                System.out.println("Thread interrupted");
                return;
            }
        }
        System.out.println("Task completed");
    }
    public static void main(String[] args) {
        int duration = 5; // Durasi dalam detik
        thread_java thread = new thread_java(duration);
        thread.start();
    }
}
