package gestion;

import java.util.List;
import java.util.ArrayList;

public class Zoologico {
	private String nombre;
	private String ubicacion;
	private List<Zona> zonas;
	
	public void agregarZonas(Zona zona) {
		this.zonas.add(zona);
	}
	
	public int cantidadTotalAnimales() {
		int total = 0;
        for (Zona zona : this.zonas) {
            total += zona.cantidadAnimales();
        }
        return total;
	}
	
	public Zoologico() {
		this.zonas = new ArrayList<>();
	}
	
	public Zoologico(String nombre, String ubicacion) {
		this.nombre = nombre;
		this.ubicacion = ubicacion;
		this.zonas = new ArrayList<>();
	}
	
	public String getNombre(){
		return nombre;
	}
	
	public String getUbicacion() {
		return ubicacion;
	}
}
