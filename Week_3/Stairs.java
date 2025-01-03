import java.util.Scanner;

class Stairs {
    public int climbStairs(int n) {
        if (n == 1) return 1;

        int first = 1, second = 2;//f=1 like 1 way and s=2 there are 2 ways.

        for (int i = 3; i <= n; i++) {//start from steps=3
            int third = first + second;
            first = second;
            second = third;
        }

        return second;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of steps: ");//input teesko
        int n = scanner.nextInt();

        Stairs ways = new Stairs();
        int result = ways.climbStairs(n);

        System.out.println("Ways to climb: " + result);

    }
}
