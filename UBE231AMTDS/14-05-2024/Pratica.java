public class Pratica {

    public static boolean podeAssistir (int idadeUsuario, int classificacao,
                                        boolean assinaturaAtiva, boolean filmeLivre) {

        return idadeUsuario >= classificacao && (assinaturaAtiva || filmeLivre);
    }

    public static void main(String[] args) {

        String filme = "A volta dos que não foram!";
        int classificacaoIndicativa = 12;
        int idadeUsuario = 11;
        boolean assinaturaAtiva = false;
        boolean filmeLivre = true;

        System.out.println(podeAssistir(idadeUsuario, classificacaoIndicativa, assinaturaAtiva, filmeLivre));

        // Verifique se o usuário pode assistir o filme, retornando true ou false

    }
}
