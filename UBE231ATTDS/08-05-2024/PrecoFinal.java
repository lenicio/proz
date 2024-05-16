/*	calcular o preço final de um produto com base no valor original e aplicar 
	um desconto de 10% se o cliente for um membro premium. */

public class PrecoFinal {
	public static void main(String[] args) {
		double precoOriginal, precoFinal;
		boolean ehPremium = true;

		precoOriginal = 100;

		if (ehPremium) {
			precoFinal = precoOriginal * 0.9;
		} else {
			precoFinal = precoOriginal;
		}

		System.out.println(String.format("O preço original é: %.2f, e o preço com desconto é: %.2f",
				precoOriginal, precoFinal));
	}
}
