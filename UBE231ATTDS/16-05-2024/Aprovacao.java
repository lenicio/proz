// Gerar um código que receba do usuário 3 notas, armazene-os em um array, e
// utilizando função, informe a quantidade de alunos aprovados no curso (media >=6)

import java.util.Scanner;

public class Aprovacao {

    public static int calculaAprovacao(double[] medias) {

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double[] medias = new double[3];

        for (int i = 0; i < medias.length; i++) {
            System.out.printf("Informe a média do %dº aluno: ", i+1);
            medias[i] = sc.nextFloat();
        }

        // 2 alunos aprovados.

    }
}
