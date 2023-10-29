package com.fullstackbd.creational.singleton;
public class Settings {

    private static Settings instance;
    private String currency;

    private Settings() {
    }

    public static Settings getInstance(){
        if(Settings.instance == null){
            Settings.instance = new Settings();
        }
        return Settings.instance;
    }

    public String getCurrency() {
        return currency;
    }

    public void setCurrency(String currency) {
        this.currency = currency;
    }
}
