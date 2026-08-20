public class RomantoInteger {
    public static void main(String[] args) {
        String s = "xi";
        int a = s.length();
        if (a == 0) {
            System.out.println("eneter valid statement");

        } else {
            int count = 0;
            for (int i = 0; i < a; i++) {
                char ch = s.charAt(i);
                if (ch == 'i') {
                    count += 1;
                }
                if (ch == 'v') {
                    count += 5;
                }
                if (ch == 'x') {
                    count += 10;
                }
            }
            System.out.println(count);

        }
      // As of now not optimal for iv=4 and more than i/v/x char like m...
    }
}
