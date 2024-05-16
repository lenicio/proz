import java.util.Scanner;

public class Revisao {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        double totalVendas = 0;
        int opcao;

        do {
            System.out.printf("Total Da Compra: $%.2f%n%n", totalVendas);
            System.out.print("Digite o código do item, ou 0 para sair: ");
            opcao = sc.nextInt();

            switch (opcao) {
                case 100:
                    totalVendas += 1.59;
                    System.out.printf("Detergente adicionado com sucesso.%n%n");
                    break;

                case 101:
                    totalVendas += 4.59;
                    System.out.printf("Esponja adicionado com sucesso.%n%n");
                    break;

                case 102:
                    totalVendas += 1.79;
                    System.out.printf("Lã de aço adicionado com sucesso.%n%n");
                    break;
            }

        } while (opcao != 0);

        System.out.printf("Total da Compra: $%.2f%n%n", totalVendas);
    }
}
