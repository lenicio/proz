/*
 * calcular a média de três números e verificar se a média é maior ou igual à 7.
*/

public class Media {
    public static void main(String[] args) {
        double n1, n2, n3, media;

        n1 = 10;
        n2 = 8;
        n3 = 5.5;

        media = (n1 + n2 + n3) / 3;

        if (media >= 7) {
            System.out.println("Maior ou igual");
        } else {
            System.out.println("Menor");
        }

    }
}
