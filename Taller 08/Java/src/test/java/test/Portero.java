package test;

public class Portero extends Futbolista{
	public short golesRecibidos;
	public byte dorsal;
	
	public Portero(String nombre, int edad, short golesRecibidos, byte dorsal) {
		super(nombre,edad,"Portero");
		this.golesRecibidos = golesRecibidos;
		this.dorsal = dorsal;
	}
	
	public boolean jugarConLasManos() {
		return true;
	}
	
	public String toString() {
		return "El futbolista "+getNombre()+" tiene "+getEdad()+", y juega de "+getPosicion()+" con el dorsal "+dorsal+". Le han marcado "+golesRecibidos;
	}
	
	public int getGolesRecibidos() {
		return golesRecibidos;
	}
	
	@Override
    public int compareTo(Futbolista otroPortero) {
        return Math.abs(this.golesRecibidos - ((Portero)otroPortero).getGolesRecibidos());
    }
}
