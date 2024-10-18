#include<stdio.h>
#include<limits.h> 
int reverse(int x) {
    long sum = 0;
    while (x != 0) {
        int rem = x % 10;
        sum = sum * 10 + rem;
        x = x / 10;
    }
    if (sum > INT_MAX || sum < INT_MIN) {
        return 0;
    }
    return (int)sum;
}

int main() {
    int number;
    printf("Enter an integer: ");
    scanf("%d", &number);

    int reversedNumber = reverse(number);
    printf("Reversed number: %d\n", reversedNumber);

    return 0;
}
