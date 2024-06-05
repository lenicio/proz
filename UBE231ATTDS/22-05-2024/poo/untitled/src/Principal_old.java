import java.util.Scanner;

public class Principal {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    Carro carro1 = new Carro();

    carro1.modelo = "Byd";
    carro1.placa = "ELE-1010";
    carro1.torque = 5000;
    carro1.ano = 2024;

    carro1.ligaCarro();
    carro1.andar();


  }
}
