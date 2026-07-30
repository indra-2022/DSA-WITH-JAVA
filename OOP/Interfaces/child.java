package Interfaces;

public class child extends Introduction {
   // Abstruct classs so child must override it
    @Override
    void age(int num) {
     System.out.println("My age is "+ num);
    //  num=num + 1000;
    //  System.out.println(num);
    }

    @Override
    void name(String name) {
         System.out.println("My name is " + name);
    }

}
