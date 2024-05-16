public class EstruturaSwitch {
    public static void main(String[] args) {

        int opcao = 5;
        boolean check = false;
        double salario = 1000.00;
        String nome = "2";


        switch (nome) {
            case "1":
                System.out.println("Você tem privilégios administrativos!");
                break;
            case "2":
                System.out.println("Você não tem privilégios adminsitrativos");
                break;
            default:
                System.out.println("Você não é um usuário!");
                break;
        }

    }
}
