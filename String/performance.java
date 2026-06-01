public class performance {
    public static void main(String[] args) {
        String series ="";
        for(int i=0;i<26;i++){
            char ch = (char)('A'+i);
            System.out.println(ch);
            series=series+" "+ch;
        }
        System.out.println(series);
    }

}
//Here this thing is adding new data in String,but Strings are immutable in java
//so its creating new object everytime,and so its consumint O(n^2) complexity
//also wasting memory
