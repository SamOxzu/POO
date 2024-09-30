package zooAnimales;

import gestion.Zona;

public class Pez extends Animal{
	private static Pez [] listado;
	public static int salmones;
	public static int bacalaos;
	private String colorEscamas;
	private int cantidadAletas;
	
	public static int cantidadPeces() {
		return 1;
	}
	
	public static void crearSalmon() {
		
	}
	
	public static void crearBacalao() {
		
	}
	
	public String movimiento() {
		return "nadar";
	}
	
	public Pez() {
		
	}
	
	public Pez(String nombre, int edad, String habitat, String genero, String colorEscamas, int cantidadAletas) {
		this.nombre = nombre;
		this.edad = edad;
		this.habitat = habitat;
		this.genero = genero;
		this.colorEscamas = colorEscamas;
		this.cantidadAletas = cantidadAletas;
	}
	
	public String getColorEscamas() {
		return colorEscamas;
	}
	
	public int getCantidadAletas() {
		return cantidadAletas;
	}
}
