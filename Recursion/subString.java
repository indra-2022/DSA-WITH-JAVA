public class subString {
    public static void main(String[] args) {
           sub("", "abcde");
    }
    static void sub(String p, String up) {
        if (up.isEmpty()) { // Base condition to stop recursive call
            System.out.print(" "+p);
            return;
        }
        char ch = up.charAt(0);
        sub(p + ch, up.substring(1));
        sub(p, up.substring(1));

    }
}
// This program will print all the possible sub set of "abc",we can have any other
// example also.
//Logic and the explaination is in the physical note.