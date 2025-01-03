def reverse(x):
    # Initialize sum to store reversed number
    sum = 0

    # Loop until x is 0 continues
    while x != 0:
        rem = x % 10  # Get the last digit
        sum = sum * 10 + rem  # Build the reversed number
        x //= 10  # Remove the last digit from x

    return sum  # Return the reversed integer

#input
user_input = int(input("Enter an integer to reverse: "))  # user  input
reversed_integer = reverse(user_input)  # Call the reverse function
print(f"The reversed integer is:" ,reversed_integer)  # Output
