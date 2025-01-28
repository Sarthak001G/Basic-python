#Here are some common Python string functions you might find helpful:
# s = "hello world hello"
# print(s.count("hello", 0, 10))  # Output: 1 (only considers the substring within the first 10 characters)


### 1. **Basic String Methods**
# - **`len(string)`**: Returns the length of the string.  
#   ```python
#   s = "hello"
#   print(len(s))  # Output: 5
#   ```

# - **`string.lower()`**: Converts the string to lowercase.  
#   ```python
#   s = "HELLO"
#   print(s.lower())  # Output: hello
#   ```

# - **`string.upper()`**: Converts the string to uppercase.  
#   ```python
#   s = "hello"
#   print(s.upper())  # Output: HELLO
#   ```

# - **`string.capitalize()`**: Capitalizes the first letter of the string.  
#   ```python
#   s = "hello"
#   print(s.capitalize())  # Output: Hello
#   ```

# - **`string.title()`**: Converts the first letter of each word to uppercase.  
#   ```python
#   s = "hello world"
#   print(s.title())  # Output: Hello World
#   ```

# ### 2. **String Searching and Replacing**
# - **`string.find(substring)`**: Returns the index of the first occurrence of the substring (-1 if not found).  
#   ```python
#   s = "hello world"
#   print(s.find("world"))  # Output: 6
#   ```

# - **`string.replace(old, new)`**: Replaces all occurrences of a substring with another substring.  
#   ```python
#   s = "hello world"
#   print(s.replace("world", "Python"))  # Output: hello Python
#   ```

# ### 3. **String Splitting and Joining**
# - **`string.split(separator)`**: Splits the string into a list based on the separator.  
#   ```python
#   s = "apple,banana,cherry"
#   print(s.split(","))  # Output: ['apple', 'banana', 'cherry']
#   ```

# - **`string.join(iterable)`**: Joins elements of an iterable into a string with a specified separator.  
#   ```python
#   words = ["apple", "banana", "cherry"]
#   print(", ".join(words))  # Output: apple, banana, cherry
#   ```

# ### 4. **Checking String Content**
# - **`string.isdigit()`**: Returns `True` if the string contains only digits.  
#   ```python
#   s = "123"
#   print(s.isdigit())  # Output: True
#   ```

# - **`string.isalpha()`**: Returns `True` if the string contains only alphabetic characters.  
#   ```python
#   s = "hello"
#   print(s.isalpha())  # Output: True
#   ```

# - **`string.isalnum()`**: Returns `True` if the string contains only alphanumeric characters.  
#   ```python
#   s = "hello123"
#   print(s.isalnum())  # Output: True
#   ```

# - **`string.isspace()`**: Returns `True` if the string contains only whitespace characters.  
#   ```python
#   s = "   "
#   print(s.isspace())  # Output: True
#   ```

# ### 5. **String Stripping**
# - **`string.strip(chars)`**: Removes leading and trailing characters (default is whitespace).  
#   ```python
#   s = "  hello  "
#   print(s.strip())  # Output: hello
#   ```

# - **`string.lstrip(chars)`**: Removes leading characters.  
#   ```python
#   s = "  hello"
#   print(s.lstrip())  # Output: hello
#   ```

# - **`string.rstrip(chars)`**: Removes trailing characters.  
#   ```python
#   s = "hello  "
#   print(s.rstrip())  # Output: hello
#   ```

# ### 6. **Other Useful Methods**
# - **`string.startswith(prefix)`**: Checks if the string starts with the specified prefix.  
#   ```python
#   s = "hello world"
#   print(s.startswith("hello"))  # Output: True
#   ```

# - **`string.endswith(suffix)`**: Checks if the string ends with the specified suffix.  
#   ```python
#   s = "hello world"
#   print(s.endswith("world"))  # Output: True
#   ```

# Let me know if you'd like examples or details on any of these!