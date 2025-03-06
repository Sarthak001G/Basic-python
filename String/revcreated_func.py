def reverse_string(s):
    result = ""
    for char in s:
        result = char + result  # Add each character to the front
    return result

# Example usage
text = "Hello World!"
reversed_text = reverse_string(text)
print(reversed_text)  # Output: !dlroW olleH
