package Abstruction;

import java.util.ArrayList;

// Hiidng unnecessary data from user,while working smoothly is abstruction

public class Introduction {
  public static void main(String[] args) {
                       // EXAMPLE 1
    System.out.println("Hello im using println Function to print me");
    //See here we are using the Println method but do we care about how it is
    //implemented internally in order to use that?? 
    // [NO]
    //Thats abstruction
                       // EXAMPLE 2
    ArrayList list = new ArrayList();
    list.add(12);
    System.out.println(list.toString());
    //Here we are using Arraylist but the internal implementation of it
    //is hidden to s, this is abstruction,thats why we called abstruct object,datatype


    /*public ArrayList(int initialCapacity) {
        if (initialCapacity > 0) {
            this.elementData = new Object[initialCapacity];
        } else if (initialCapacity == 0) {
            this.elementData = EMPTY_ELEMENTDATA;
        } else {
            throw new IllegalArgumentException("Illegal Capacity: "+
                                               initialCapacity);
        }
    } */ //-> This is the implementation of an Arraylist code internally
         //Which is hidden from us

  } 
}
