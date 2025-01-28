""" immutable Data type are =integer,floating point number ,boolean, string, tuple
In Python, **mutable** and **immutable** refer to whether or not an object's value can be changed after it is created.

---

### **1. Mutable Objects**
These are objects whose values can be changed after creation. When you modify a mutable object, its memory address remains the same.

#### Examples of Mutable Objects:
- **Lists**
- **Dictionaries**
- **Sets**
- **User-defined objects (depending on implementation)**

#### Example with a List (Mutable):
```python
# Create a list
my_list = [1, 2, 3]
print("Before:", my_list)

# Modify the list
my_list.append(4)
print("After:", my_list)  # Output: [1, 2, 3, 4]

# Memory address remains the same
print(id(my_list))  # Memory address
```

---

### **2. Immutable Objects**
These are objects whose values cannot be changed after creation. Any modification to an immutable object results in the creation of a new object in memory.

#### Examples of Immutable Objects:
- **Numbers (int, float, complex, etc.)**
- **Strings**
- **Tuples**
- **Frozen sets**

#### Example with a String (Immutable):
```python
# Create a string
my_string = "Hello"
print("Before:", my_string)

# Modify the string
my_string = my_string + " World"
print("After:", my_string)  # Output: "Hello World"

# Memory address changes
print(id(my_string))  # New memory address
```

---

### **Key Differences Between Mutable and Immutable Objects**

| Feature                     | Mutable Objects             | Immutable Objects           |
|-----------------------------|-----------------------------|-----------------------------|
| **Can be modified?**        | Yes                         | No                          |
| **Examples**                | Lists, dictionaries, sets   | Strings, tuples, numbers    |
| **Memory address changes?** | No (same object)            | Yes (new object created)    |
| **Use case**                | When frequent updates are needed | When data consistency is important |

---

### **Why Use Immutable Objects?**
1. **Thread Safety:** Immutable objects can be safely shared between threads.
2. **Hashing:** Immutable objects can be used as keys in dictionaries and elements in sets.
3. **Predictability:** Reduces unintended side effects by preventing modifications.

### **Why Use Mutable Objects?**
1. **Efficiency:** You can modify the object in place without creating new ones.
2. **Flexibility:** They allow dynamic changes, making them useful for collections and data structures.

Let me know if you'd like further clarification!"""