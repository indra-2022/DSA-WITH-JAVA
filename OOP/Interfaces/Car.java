package Interfaces;

public class Car implements Engine,Media{

    @Override
    public void acc() {
        System.out.println("I accelerate the car");
        
    }

    @Override
    public void start() {
        System.out.println("I starts the car");
        
    }

    @Override
    public void stop() {
        System.out.println("I stop the car");
        
    }

    @Override
    public void startm() {
        System.out.println("I st the medcia player");
        
    }

    @Override
    public void stopm() {
        System.out.println("I stop the media player");
        
    }

}
