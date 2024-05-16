// Aproveite a estrutura abaixo, e implemente uma solução que exiba o MENOR@Suporte$yst3m
// número do array.
import java.util.Scanner;

public class Listas {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] numeros = new int[3];
        int maiorNumero;

        for (int i = 0; i < numeros.length; i++) {
            System.out.printf("Informe um número para posição %d do array: ", i);
            numeros[i] = sc.nextInt();
        }

        maiorNumero = numeros[0];

        for (int numero : numeros) {
            if (numero > maiorNumero) {
                maiorNumero = numero;
            }
        }
        System.out.printf("%n%nO maior número é: %d", maiorNumero);
    }
}
