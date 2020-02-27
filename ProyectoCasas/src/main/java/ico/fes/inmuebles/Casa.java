/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ico.fes.inmuebles;

import ico.fes.habitaciones.Baño;
import ico.fes.habitaciones.Dormitorio;
import ico.fes.habitaciones.Sala;

/**
 *
 * @author 2im3q
 */
public class Casa {
    private Baño baño;
    private Dormitorio dormitorio;
    private Sala principal;

    public Casa() {
    }

    public Casa(Baño baño, Dormitorio dormitorio, Sala principal) {
        this.baño = baño;
        this.dormitorio = dormitorio;
        this.principal = principal;
    }

    public Sala getPrincipal() {
        return principal;
    }

    public void setPrincipal(Sala principal) {
        this.principal = principal;
    }

    public Baño getBaño() {
        return baño;
    }

    public void setBaño(Baño baño) {
        this.baño = baño;
    }

    public Dormitorio getDormitorio() {
        return dormitorio;
    }

    public void setDormitorio(Dormitorio dormitorio) {
        this.dormitorio = dormitorio;
    }
    
    public void descripcionCasa(){
        System.out.println("Descripcion del dormitorio");
        dormitorio.descripcionDormitorio();
        System.out.println("Descripcion de la sala");
        principal.descripcionSala();
        System.out.println("Descripcion del baño");
        baño.descripcionBaño();
    } 
    
    
}
