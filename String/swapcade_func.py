def swap_case(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':  # If lowercase, convert to uppercase
            result += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':  # If uppercase, convert to lowercase
            result += chr(ord(char) + 32)
        else:  # If not a letter, keep it unchanged
            result += char
    return result

# Example usage
text = "Hello World!"
swapped_text = swap_case(text)
print(swapped_text)  # Output: hELLO wORLD!
