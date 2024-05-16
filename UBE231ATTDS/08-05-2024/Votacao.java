/*
	verificar se uma pessoa tem idade suficiente para votar (idade maior ou 
	igual a 18) e se possui menos de 70 anos.
 */

import java.util.Scanner;

public class Votacao {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		System.out.print("Insira a idade: ");
		int idade = scanner.nextInt();

		if (idade >= 18 & idade < 70) {
			System.out.println("Voto Obrigatório!");
		}

		scanner.close();
	}
}