import java.util.Arrays;

public class methods {
    public static void main(String[] args) {
        String name = "Indranil ganguly";
        System.out.println(name.charAt(4));
        System.out.println(name.concat(" Lord"));
        System.out.println(name.indexOf("l"));
        System.out.println(name.isBlank());
        System.out.println(Arrays.toString(name.split(" ")));
        //Split method returns an array so need to use [Arrays.toString()]
    }
}
