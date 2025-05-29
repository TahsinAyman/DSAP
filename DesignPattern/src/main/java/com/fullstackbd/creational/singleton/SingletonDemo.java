package com.fullstackbd.creational.singleton;
public class SingletonDemo {

    public static void main(String[] args) {
        Settings settings = Settings.getInstance();
        settings.setCurrency("Tk");
        Settings settings1 = Settings.getInstance();
        settings1.setCurrency("$");
        System.out.println(settings.getCurrency());
        System.out.println(settings1);
        System.out.println(settings);
        

    }
}
