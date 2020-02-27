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
public class Sala {
    private boolean luzEncendida;
    private boolean televisorEncendido;
    private boolean estereoEncendido;

    public Sala() {
    }

    public Sala(boolean luzEncendida, boolean televisorEncendido, boolean estereoEncendido) {
        this.luzEncendida = luzEncendida;
        this.televisorEncendido = televisorEncendido;
        this.estereoEncendido = estereoEncendido;
    }

    public boolean isEstereoEncendido() {
        return estereoEncendido;
    }

    public void setEstereoEncendido(boolean estereoEncendido) {
        this.estereoEncendido = estereoEncendido;
    }

    public boolean isLuzEncendida() {
        return luzEncendida;
    }

    public void setLuzEncendida(boolean luzEncendida) {
        this.luzEncendida = luzEncendida;
    }

    public boolean isTelevisorEncendido() {
        return televisorEncendido;
    }

    public void setTelevisorEncendido(boolean televisorEncendido) {
        this.televisorEncendido = televisorEncendido;
    }
    
    public String toString(){
        String res="Luz encendida: "+this.luzEncendida;
        res=res+"Televisor encendido: "+this.televisorEncendido;
        res=res+"Estereo encendido: "+this.estereoEncendido;
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
    
    public String encenderTelevisor(){
        if(this.televisorEncendido==false){
            this.televisorEncendido=true;
        }
        String encendido="El televisor esta encendido";
        return encendido;
    }
    public String apagarTelevisor(){
        if(this.televisorEncendido==true){
            this.televisorEncendido=false;
        }
    String apagado="El televisor esta apagado";
    return apagado;
    }
    public String encenderEstereo(){
        if(this.estereoEncendido==false){
            this.estereoEncendido=true;
        }
        String encendido="Estereo encendido";
        return encendido;
    }
    public String apagarEstereo(){
        if(this.estereoEncendido==true){
            this.estereoEncendido=false;
        }
        String apagado="Estereo apagado";
        return apagado;
    }
    public void descripcionSala(){
        System.out.println("ESta sala: \nLuz encendida:"+this.luzEncendida+"\nEstereo encendido: "+this.estereoEncendido+"\nTelevisor encendido:"+this.estereoEncendido);
    }
}
