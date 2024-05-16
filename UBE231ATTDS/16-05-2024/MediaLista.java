//

import java.util.Scanner;

public class MediaLista {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] numeros = new int[3];
        double totalSoma = 0;

        for (int i = 0; i < numeros.length; i++) {
            System.out.printf("Informe um número para posição %d do array: ", i);
            numeros[i] = sc.nextInt();
        }

        for (int numero : numeros) {
            totalSoma += numero;
        }
        System.out.printf("%n%nA média é: %f", totalSoma / numeros.length);
    }
}
