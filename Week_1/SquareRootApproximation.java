import java.util.Scanner;

public class SquareRootApproximation {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a non-negative integer: ");
        int x = scanner.nextInt();
        if (x < 0) {
            System.out.println("Invalid input. Please enter a non-negative integer.");
            return;
        }
        double result = Math.sqrt(x);
        System.out.printf("The square root of %d is approximately %.6f%n", x, result);
    }
}
