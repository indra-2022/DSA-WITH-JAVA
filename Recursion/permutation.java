public class permutation {
    public static void main(String[] args) {
        perm("","abc");
    }
    static void perm(String p,String up){
        if (up.isEmpty()) {
            System.out.println(p);
            return;
        }
        char ch = up.charAt(0);//loop will run two more times than the size of process
                                      // p=1,loop=3/p=2,loop=5.
        for(int i=0;i<=p.length();i++){
            String f=p.substring(0,i);
            String s =p.substring(i,p.length());
            perm(f+ch+s, up.substring(1));
        }
    }
}
//Explaination is in physical note.
