package zooAnimales;

import gestion.Zona;

public class Reptil extends Animal{
	private static Reptil [] listado;
	public static int iguanas;
	public static int serpientes;
	private String colorEscamas;
	private int largoCola;
	
	public static int cantidadReptiles() {
		return 1;
	}
	
	public static void crearIguana() {
		
	}
	
	public static void crearSerpiente() {
		
	}
	
	public String movimiento() {
		return "reptar";
	}
	
	public Reptil() {
		
	}
	
	public Reptil(String nombre, int edad, String habitat, String genero, String colorEscamas, int largoCola) {
		this.nombre = nombre;
		this.edad = edad;
		this.habitat = habitat;
		this.genero = genero;
		this.colorEscamas = colorEscamas;
		this.largoCola = largoCola;
	}
	
	public String getColorEscamas() {
		return colorEscamas;
	}
	
	public int getLargoCola() {
		return largoCola;
	}
}
