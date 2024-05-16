import java.util.Scanner;

public class Funcoes {

    public static int dobraNumero(int numero) {
        return numero * 2;
    }

    public static boolean statusAprovado(double nota01, double nota02, double nota03) {
        double media = (nota01 + nota02 + nota03) / 3;
        return media >= 6;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double nota01, nota02, nota03;

        System.out.print("Digite a 1ª nota: ");
        nota01 = sc.nextDouble();

        System.out.print("Digite a 2 nota: ");
        nota02 = sc.nextDouble();

        System.out.print("Digite a 3ª nota: ");
        nota03 = sc.nextDouble();

        System.out.println(statusAprovado(nota01, nota02, nota03));
    }
}
