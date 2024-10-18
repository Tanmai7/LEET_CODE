def reverseString(s):
    return s[::-1]
user_input = input("Enter a string to reverse: ")
reversed_string = reverseString(user_input)
print("Reversed string:", reversed_string)