package aula02;

import java.util.Scanner;
  public class Exercicio05{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite a letra (F ou M): ");
        String letra = scanner.nextLine().toUpperCase();

        if (letra.equals("F")) {
            System.out.println("F - Feminino");
        } else if (letra.equals("M")) {
            System.out.println("M - Masculino");
        } else {
            System.out.println("Letra inválida.");
        }

        scanner.close();
    }
}
