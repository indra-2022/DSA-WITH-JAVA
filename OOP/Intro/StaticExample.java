public class StaticExample {
    void greet(){
        System.out.println("Hlw"); // Non static mehod,need an obj
    }
    static int a=5;
    static int b;  //Static veriables no neeed to have obj
    static{
        b=a+5;
    }

    public static void main(String[] args) {
        StaticExample obj = new StaticExample();
        obj.greet();
        System.out.println(a+b);
        System.out.println(StaticExample.a);
    }
}

