/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package proyectoCasas;

import ico.fes.habitaciones.Baño;
import ico.fes.habitaciones.Dormitorio;
import ico.fes.habitaciones.Sala;
import ico.fes.inmuebles.Casa;

/**
 *
 * @author 2im3q
 */
public class ProyectoCasas {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        Baño baño1=new Baño(1, true, true);
        Dormitorio dormitorio1=new Dormitorio(true, true, "Dueño", "Individual");
        Sala principal1=new Sala(true, true, true);
        
        Casa casa1=new Casa(baño1, dormitorio1, principal1);
                
        casa1.descripcionCasa();
        
        System.out.println("\n\n\n");
        principal1.apagarTelevisor();
        
        casa1.descripcionCasa();
    }
    
}
