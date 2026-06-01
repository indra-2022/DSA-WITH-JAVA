public class mazediagonal {
    public static void main(String[] args) {
        pathfinder("", 3, 3);
    }
    static void pathfinder(String p,int r,int c){
        if (r==1 && c==1) {
            System.out.println(p);
            return;
        }
        if (r>1) {
            pathfinder(p+"Down->", r-1, c);
        }
        if (c>1) {
            pathfinder(p+"Right->", r, c-1);
        }
        if (r>1 && c>1) {
            pathfinder(p+"Diagonal->", r-1, c-1); // Easy asf
        }
    }
}
