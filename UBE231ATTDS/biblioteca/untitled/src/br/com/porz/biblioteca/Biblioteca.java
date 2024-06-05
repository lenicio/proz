package br.com.porz.biblioteca;

public class Biblioteca {
  private String nome;
  Livro[] livros;
  private int quantidadeDeLivros;



  // Construtor
  public Biblioteca(String nome, int capacidadeDeLivros) {
    this.nome = nome;
    livros = new Livro[capacidadeDeLivros];
  }

  public void adicionarLivro(Livro livro) {
    livros[quantidadeDeLivros] = livro;
    quantidadeDeLivros++;
  }

  public void exibirLivros() {
    for (int i = 0; i < quantidadeDeLivros; i++) {
      System.out.println(livros[i].getTitulo());
    }
  }

  public void emprestarLivro(Livro livro) {
    livro.emprestar();
  }

  public void devolverLivro(Livro livro) {
    livro.devolver();
  }
}
