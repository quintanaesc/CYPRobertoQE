/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ico.fes.habitaciones;

/**
 *
 * @author 2im3q
 */
public class Dormitorio {
    private boolean puertaAbierta;  
    private boolean luzEncendida;
    private String habitante;
    private String tipoDeCama;

    public Dormitorio() {
    }

    public Dormitorio(boolean puertaAbierta, boolean luzEncendida, String habitante, String tipoDeCama) {
        this.puertaAbierta = puertaAbierta;
        this.luzEncendida = luzEncendida;
        this.habitante = habitante;
        this.tipoDeCama = tipoDeCama;
    }

    public String getTipoDeCama() {
        return tipoDeCama;
    }

    public void setTipoDeCama(String tipoDeCama) {
        this.tipoDeCama = tipoDeCama;
    }

    public boolean isPuertaAbierta() {
        return puertaAbierta;
    }

    public void setPuertaAbierta(boolean puertaAbierta) {
        this.puertaAbierta = puertaAbierta;
    }

    public boolean isLuzEncendida() {
        return luzEncendida;
    }

    public void setLuzEncendida(boolean luzEncendida) {
        this.luzEncendida = luzEncendida;
    }

    public String getHabitante() {
        return habitante;
    }

    public void setHabitante(String habitante) {
        this.habitante = habitante;
    }
    
    public String toString(){
        String res="Habitacion de: "+this.habitante;
        res=res+"Luz encendida: " +this.luzEncendida;
        res=res+"Puerta abierta: "+this.puertaAbierta;
        res=res+"Tipo de cama"+this.tipoDeCama;
        return res;
    }
    
    public String encenderLuz(){
        if(this.luzEncendida==false){
            this.luzEncendida=true;
        }
        String encendida="Luz encendida";
        return encendida;
    }
    
    public String apagarLuz(){
        if(this.luzEncendida==true){
            this.luzEncendida=false;
        }
        String apagada="Apagar luz";
        return apagada;
    }
    
    public void descripcionDormitorio(){
        System.out.println("Este dormitorio: \nEs de: "+this.habitante+"\nLuz encendida: "+this.luzEncendida+"\nPuerta abierta"+this.puertaAbierta);
        
    }
}
