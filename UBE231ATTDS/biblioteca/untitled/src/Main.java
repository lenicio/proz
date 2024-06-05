import br.com.porz.biblioteca.Biblioteca;
import br.com.porz.biblioteca.Livro;

public class Main {
  public static void main(String[] args) {
    Biblioteca biblioteca = new Biblioteca("Sebo Uberlândia", 5000);
    Livro livro1 = new Livro("Harry Potter e a Pedra Filosofial", "Ficção", "JK", 2002);
    Livro livro2 = new Livro("Harry Potter e a Camara Secreta", "Ficção", "JK", 2003);
    Livro livro3 = new Livro("Harry Potter e o Prisioneiro De Askaban", "Ficção", "JK", 2004);
    Livro livro4 = new Livro("Harry Potter e o Calice De Fogo", "Ficção", "JK", 2004);


    biblioteca.adicionarLivro(livro1);
    biblioteca.adicionarLivro(livro2);
    biblioteca.adicionarLivro(livro3);
    biblioteca.adicionarLivro(livro4);


    biblioteca.emprestarLivro(livro1);
    biblioteca.emprestarLivro(livro1);
    biblioteca.devolverLivro(livro2);


  }
}