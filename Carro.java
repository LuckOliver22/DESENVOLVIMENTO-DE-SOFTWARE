public class Carro{
    public String cor;
    public String modelo;
    public String marca;
    private int quilometragem;
    private int ano;
    private int chassi;
    private int potencia;
    
    public Carro(String cor, String modelo,String marca,int quilometragem, int ano,int chassi,int potencia){
        this.cor = cor;
        this.modelo = modelo;
        this.marca = marca;
        this.ano = ano;
        this.chassi = chassi;
        this.potencia = potencia;
    }
    
    public void print(){
    System.out.println("-------------------");    
    System.out.println("Cor:" + cor);
    System.out.println("Modelo: " + modelo);
    System.out.println("Marca: " + marca);
    System.out.println("Quilometragem: " + quilometragem);
    System.out.println("Ano: " + ano);
    System.out.println("Chassi " + chassi);
    System.out.println("Potencia: " + potencia);
    System.out.println("-------------------");
    }
    
    public static void main (String[] args) {
        Carro carro1 = new Carro("Preto", "Ghost", "Bentley", 2500, 2020, 123456789, 400);
        
        carro1.print();
    }
}
