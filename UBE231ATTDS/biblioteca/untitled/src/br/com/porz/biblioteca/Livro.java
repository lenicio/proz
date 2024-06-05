package br.com.porz.biblioteca;

import javax.swing.text.StyledEditorKit;

public class Livro {
  private String titulo, genero, autor;
  private int anoDeLancamento;
  private boolean statusEmprestimo;


  // Construtor
  public Livro(String titulo, String genero, String autor, int anoDeLancamento) {
    this.titulo = titulo;
    this.genero = genero;
    this.autor = autor;
    this.anoDeLancamento = anoDeLancamento;
    this.statusEmprestimo = false;
  }

  public boolean getStatusEmprestimo() {
    return statusEmprestimo;
  }

  public void emprestar() {
    if (statusEmprestimo) {
      System.out.println("O livro já está emprestado!");
    } else {
      statusEmprestimo = true;
    }
  }


  public void devolver() {
    if (statusEmprestimo) {
      statusEmprestimo = false;
    } else {
      System.out.println("O livro não está emprestado!");
    }
  }

  public String getTitulo() {
    return titulo;
  }

  public void setTitulo(String titulo) {
    this.titulo = titulo;
  }

  public String getGenero() {
    return genero;
  }

  public void setGenero(String genero) {
    this.genero = genero;
  }

  public String getAutor() {
    return autor;
  }

  public void setAutor(String autor) {
    this.autor = autor;
  }

  public int getAnoDeLancamento() {
    return anoDeLancamento;
  }

  public void setAnoDeLancamento(int anoDeLancamento) {
    this.anoDeLancamento = anoDeLancamento;
  }
}
