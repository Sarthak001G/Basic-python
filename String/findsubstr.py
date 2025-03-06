def find_substring(string, substring):
    str_len = len(string)
    sub_len = len(substring)

    for i in range(str_len - sub_len + 1):  # Loop through main string
        match = True
        for j in range(sub_len):  # Loop through substring
            if string[i + j] != substring[j]:  # Compare characters
                match = False
                break
        if match:
            return i  # Return the first index of occurrence

    return -1  # Return -1 if substring not found

# Example usage
text = "Hello World!"
sub_text = "World"
result = find_substring(text, sub_text)
print(result)  # Output: 6
