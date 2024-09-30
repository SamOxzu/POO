package gestorAplicacion.paquete1;

import java.util.ArrayList;
import java.io.Serializable;

public class Computador extends Recurso implements Serializable{
	private static final long serialVersionUID = 1L;
	static private int totalPCs;
    private String marca;
    private String gama;
    

    // Constructor de la clase Computador
    public Computador(String nombre, int idRecurso, String marca, String gama) {
        super(nombre, idRecurso); // Llama al constructor de la clase base (Recurso)
        this.marca = marca;
        this.gama = gama;
        totalPCs++;
    }
    
    public Computador() {
    	this("Sin referencia", 0, "Sin marca", "Sin gama");
    }

    // Métodos para obtener y establecer la marca del computador
    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    // Métodos para obtener y establecer la gama del computador
    public String getGama() {
        return gama;
    }
    
    public static int getTotalPCs() {
		return totalPCs;
	}

    public void setGama(String gama) {
        this.gama = gama;
    }
    
    public String tipoRecurso() {
    	return "Computador";
    }
    
    public String toString() {
    	return this.getNombre();
    }
}


