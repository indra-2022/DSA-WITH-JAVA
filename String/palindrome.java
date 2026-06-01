public class palindrome {
    public static void main(String[] args) {
        String name="cow";
        StringBuilder builder = new StringBuilder(name);
       String rev = builder.reverse().toString();
       if (name.equals(rev)) {
            System.out.println("Palindrome word");
       }
       else{
        System.out.println("Not a palindrome word");
       }
    }
}
