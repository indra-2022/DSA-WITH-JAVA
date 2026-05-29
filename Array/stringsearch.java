public class stringsearch {
    public static void main(String[] args) {
        String str="indranil";
        char target='r';
        System.out.println(search(str,target));
    }
    static boolean search(String str,char target){
        for(int i=0;i<str.length();i++){
            if(target==str.charAt(i)){
              return true;
            }
        }
        return false;
    }
}
