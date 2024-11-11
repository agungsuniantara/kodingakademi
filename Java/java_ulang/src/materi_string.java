public class materi_string {
    public static void main(String[] args) {
        String kata = "hello";
        int test = 10;
        String kata2 = kata + "world" + test;
        String kata3 = kata.repeat(3);
        String s = kata.substring(0, 3);
        int jumlah = kata.length();
        String upper = kata.toUpperCase();
        String lower = kata.toLowerCase();
        int test10 = kata.indexOf("lo");

        StringBuilder builder = new StringBuilder();
        builder.append("a");
        builder.append("hello world");
        String complete = builder.toString();

        System.out.println(kata2);
        System.out.println(kata3);
        System.out.println(s);
        System.out.println(jumlah);
        System.out.println(((Object) jumlah).getClass().getSimpleName());
        System.out.println(upper);
        System.out.println(lower);
        System.out.println(test10);
        System.out.println(complete);
    }
}
