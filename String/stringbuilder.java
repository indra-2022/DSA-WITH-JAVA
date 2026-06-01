public class stringbuilder {
    public static void main(String[] args) {
        StringBuilder series = new StringBuilder();
         for(int i=0;i<26;i++){
            char ch = (char)('A'+i);
            //System.out.println(ch);
            series.append(ch);
        }
        String builder=series.toString();
        System.out.println(builder);//Converting the StringBuilder to String
    }
}
//This is the same program as [performance.java] but here we are using StringBuilder
//so its not creating new obj every time,so the time complexity is better than String.
