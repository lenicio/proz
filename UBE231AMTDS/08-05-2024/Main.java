import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        double nota1, nota2, nota3, media;

        System.out.print("Informe a nota 01:");
        nota1 = scanner.nextDouble();

        System.out.print("Informe a nota 02:");
        nota2 = scanner.nextDouble();

        System.out.print("Informe a nota 03:");
        nota3 = scanner.nextDouble();

        media = (nota1 + nota2 + nota3) / 3;

        if (media >= 6) {
            System.out.println("Você está aprovado!");
        } else {
            System.out.println("Você está reprovado!");
        }

        System.out.println("A média final foi: " + media);


    }
}