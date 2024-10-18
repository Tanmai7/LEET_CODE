def is_happy(n: int):
    s = set()

    while n != 1 and n not in s:
        s.add(n)
        n = sum_of_squares(n)

    return n

def sum_of_squares(n: int):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10
    return total

number = int(input("Enter a number: "))
result = is_happy(number)

if result == 1:
    print(f"{number} is a happy number!")
else:
    print(f"{number} is not a happy number.")
