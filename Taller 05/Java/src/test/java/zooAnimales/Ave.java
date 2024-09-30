package zooAnimales;

import java.util.ArrayList;
import java.util.List;

import gestion.Zona;

public class Ave extends Animal{
	private static List<Ave> listado = new ArrayList<>();
	public static int halcones;
	public static int aguilas;
	private String colorPlumas;
	
	public static int cantidadAves() {
		return 1;
	}
	
	public static void crearHalcon() {
		
	}
	
	public static void crearAguila() {
		
	}
	
	public String movimiento() {
		return "volar";
	}
	
	public Ave() {
		listado.add(this);
	}
	
	public Ave(String nombre, int edad, String habitat, String genero, String colorPlumas) {
		this.nombre = nombre;
		this.edad = edad;
		this.habitat = habitat;
		this.genero = genero;
		this.colorPlumas = colorPlumas;
		listado.add(this);
	}
	
	public String getColorPlumas() {
		return colorPlumas;
	}
}
