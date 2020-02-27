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
public class Baño {
    private int nDePiso;
    private boolean luzEncendida;
    private boolean regaderaAbierta;

    public Baño() {
    }

    public Baño(int nDePiso, boolean luzEncendida, boolean regaderaAbierta) {
        this.nDePiso = nDePiso;
        this.luzEncendida = luzEncendida;
        this.regaderaAbierta = regaderaAbierta;
    }

    public boolean isRegaderaAbierta() {
        return regaderaAbierta;
    }

    public void setRegaderaAbierta(boolean regaderaAbierta) {
        this.regaderaAbierta = regaderaAbierta;
    }

    public int getnDePiso() {
        return nDePiso;
    }

    public void setnDePiso(int nDePiso) {
        this.nDePiso = nDePiso;
    }

    public boolean isLuzEncendida() {
        return luzEncendida;
    }

    public void setLuzEncendida(boolean luzEncendida) {
        this.luzEncendida = luzEncendida;
    }
    
    public String toString(){
        String res="Numero de piso: "+this.nDePiso;
        res=res+"Luz encendida: "+this.luzEncendida;
        res=res+"Regadera abierta: "+this.regaderaAbierta;
        return res;
    }
    public String abrirRegadera(){
        if (this.regaderaAbierta==false){
            this.regaderaAbierta=true;
        }
        String abierta="La regadera esta abierta";
        return abierta;
    }
    public String cerrarRegadera(){
        if(this.regaderaAbierta=true){
            this.regaderaAbierta=false;
        }
        String cerrada="La regadera esta cerrada";
        return cerrada;
    }
    
    public void descripcionBaño(){
        System.out.println("ESte baño:\n"+"Se encuentra en: "+this.nDePiso+"\nLuz encendida: "+this.luzEncendida+"\nRegadera abierta:"+this.regaderaAbierta);
    }
    
}
