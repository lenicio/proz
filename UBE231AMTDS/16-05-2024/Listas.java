/*
    Usando função, exiba a quantidade de alunos que foram aprovados, onde a condição é que a
    média seja maior ou igual a 6.
 */

import java.util.Scanner;

public class Listas {

    public static int calculaAprovados (double[] medias) {

        int qtdAprovados = 0;

        for (double media : medias) {
            if (media >= 6) {
                qtdAprovados += 1;
            }
        }

        return qtdAprovados;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double[] medias = new double[5];

        medias[0] = 5.0;
        medias[1] = 5.2;
        medias[2] = 7.2;
        medias[3] = 3.8;
        medias[4] = 10.0;

        System.out.println(calculaAprovados(medias));

  }
}
