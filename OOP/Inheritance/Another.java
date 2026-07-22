package Inheritance;

public class Another extends Introtwo {
    Another() {
        System.out.println("Hi i am an example of multiple Inheritance");
        System.out.println("I will also call oter classes");
    }

    Another(int a) {
        System.out.println(a + "<--This is value of a");
        System.out.println("I will also call oter classes");

    }

    void display() {
        System.out.println("Hi i am another class i will not print other classes");
    }
}
