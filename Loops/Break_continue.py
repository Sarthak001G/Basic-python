"""The `break` and `continue` statements are used to control the flow of loops in Python. They allow you to either exit a loop prematurely or skip an iteration, depending on your needs.

---

### **1. `break` Statement**
The `break` statement is used to **terminate the loop** immediately when a specific condition is met. The program then moves to the next statement after the loop.

#### Example:
```python
# Find the first number divisible by 7 in a range
for num in range(1, 20):
    if num % 7 == 0:
        print("Found:", num)
        break  # Exit the loop
print("Loop ended.")
```

**Output:**
```
Found: 7
Loop ended.
```

In this example:
- The loop stops as soon as the condition `num % 7 == 0` is satisfied.

---

### **2. `continue` Statement**
The `continue` statement is used to **skip the current iteration** of the loop and move to the next one, without executing the remaining code in the loop body.

#### Example:
```python
# Skip numbers divisible by 3
for num in range(1, 10):
    if num % 3 == 0:
        continue  # Skip the rest of the code for this iteration
    print(num)
```

**Output:**
```
1
2
4
5
7
8
```

In this example:
- Numbers divisible by 3 are skipped because the `continue` statement prevents the `print(num)` from running for those numbers.

---

### **Comparison: `break` vs `continue`**

| Feature           | `break`                          | `continue`                     |
|--------------------|----------------------------------|---------------------------------|
| **Effect**         | Exits the loop immediately      | Skips the current iteration    |
| **Loop termination?** | Yes                           | No                              |
| **Example use case** | Stop searching when condition is met | Skip processing specific cases |

---

### **3. Use in `while` Loops**
Both `break` and `continue` work the same way in `while` loops.

#### Example of `break` in `while` loop:
```python
count = 0
while count < 10:
    if count == 5:
        break  # Exit the loop when count is 5
    print(count)
    count += 1
```

**Output:**
```
0
1
2
3
4
```

#### Example of `continue` in `while` loop:
```python
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # Skip even numbers
    print(count)
```

**Output:**
```
1
3
5
7
9
```

---

### **When to Use `break` and `continue`**
- **`break`:** Use when you want to exit the loop based on a condition, e.g., finding an element or error handling.
- **`continue`:** Use when you want to skip some specific iterations but continue the loop, e.g., filtering unwanted values.

Let me know if you'd like more examples or further clarification!"""