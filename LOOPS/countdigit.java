public class countdigit {
    public static void main(String[] args) {
        int digit=23459871;
        System.out.println((int)Math.log10(digit)+1);
    }
}

//This is a very good and effective method to get the number of digits without
        //having any loop and doing much more calculations
        //Math.log10->Gives us the value in decimal like 3.987 this
        //+1 for converting upper bound of that
        //(int) is type casting the decimal value to int
