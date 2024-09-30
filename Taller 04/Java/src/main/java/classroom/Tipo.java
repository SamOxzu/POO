package classroom;

public enum Tipo {
    DISCIPLINAR(10, "Disciplinar"), FUNDAMENTACION(20, "Fundamentación"), ELECTIVA(30, "Electiva");

    public int codigo;
    public String nombre;

    Tipo(int codigo, String nombre) {
        this.codigo = codigo;
        this.nombre = nombre;
    }
}
