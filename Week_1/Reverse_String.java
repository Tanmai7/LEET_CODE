import java.util.Arrays;
import java.util.Scanner;

public class Reverse_String {

    public void reverseString(char[] s) {
        int left = 0;
        int right = s.length - 1;
        while (left < right) {
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        }
    }

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter a string: ");
            String inputString = scanner.nextLine();  

            char[] charArray = inputString.toCharArray();

            System.out.println("Original string: " + Arrays.toString(charArray));
            Reverse_String rs = new Reverse_String();
            rs.reverseString(charArray);
            System.out.println("Reversed string: " + Arrays.toString(charArray));  
        }
    }
}
