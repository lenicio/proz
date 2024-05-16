import java.util.Scanner;

public class ImpostoRenda {

    public static void main(String[] args) {
     Scanner sc = new Scanner(System.in);
     double salario = 3002.00;
     double tributos = 0;

     if (salario > 2000) {
         tributos = (salario - 2000) * 0.8;
     }

        System.out.println(tributos);







    }
}
