public class ZorpFilmes {

    public static boolean liberaFilme(int classificacaoIndicativa, boolean ehLivre,
                                      boolean assinaturaAtiva, int idadeUsuario) {

        return idadeUsuario >= classificacaoIndicativa && (assinaturaAtiva || ehLivre);
    }

    public static void main(String[] args) {
        String titulo = "Os estagiários";
        int classificaoIndicativa = 12;
        boolean ehLivre = false;
        boolean assinaturaAtiva = false;
        int idadeUsuario = 16;

        // Construa uma função, que baseando-se nas informações passadas, retorne ao usuário
        // se o mesmo pode assistir o filme. (true / false)


    }
}
