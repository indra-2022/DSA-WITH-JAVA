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