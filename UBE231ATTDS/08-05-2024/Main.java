import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int opcao;
        boolean condicao = true;

        while (condicao) {
            System.out.println("Para sair, digite 0.");
            opcao = scanner.nextInt();
            
            if (opcao == 0) {
                condicao = false;
            }
            
        }

        scanner.close();
    }
}
