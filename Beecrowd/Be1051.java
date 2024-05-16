/*
    de    0,00 até 2000,00 - Isento
    de 2000,01 até 3000,00 - 8%
    de 3000,01 até 4500,00 - 18%
    acima de 4500,00       - 28%
 */

import java.util.Scanner;

public class Be1051 {

    public static double calcularImposto(double salario) {

        double imposto = 0;

        if (salario > 4500) {
            imposto += (salario - 4500) * 0.28;
            salario = 4500;
        }

        if (salario > 3000) {
            imposto += (salario - 3000) * 0.18;
            salario = 3000;
        }

        if (salario > 2000) {
            imposto += (salario - 2000) * 0.08;
        }

        return imposto;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        double salario = sc.nextDouble();
        double imposto;

        if (salario >= 0 && salario <= 2000) {
            System.out.println("Isento");
        } else {
            System.out.printf("R$ %.2f", calcularImposto(salario));
        }

    }
}
