a={
    "name":"sarthak",
    "list" : "class"
}
print(a["list"])
print(a.items())
print(a.keys())
print(a.values())
a.update({"name":"avi"})
print(a.items())
print(a.get("name"))#give none if not available
e=()
s=set()#empty set
se={2,3,4,5}#set dont repeat the value
print(type(e),type(s))
s.add("sartyha")
s.clear()#empty set
###set are unordered unindexed immmutable  no duplicate value
len(s)
s.remove(8)
s.pop()
#Here’s a complete example demonstrating all Python **set** methods:  

#---

### **Python Set Methods with Examples**

#```python
# Creating sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {1, 2}

# 1. add() - Adds an element to the set
A.add(10)
print("add():", A)  # {1, 2, 3, 4, 5, 10}

# 2. clear() - Removes all elements from the set
temp = A.copy()
temp.clear()
print("clear():", temp)  # set()

# 3. copy() - Returns a shallow copy of the set
D = A.copy()
print("copy():", D)  # {1, 2, 3, 4, 5, 10}

# 4. difference() - Returns elements present in A but not in B
print("difference():", A.difference(B))  # {1, 2, 3, 10}

# 5. difference_update() - Removes elements found in another set
A.difference_update(B)
print("difference_update():", A)  # {1, 2, 3, 10}

# Reset A for next operations
A = {1, 2, 3, 4, 5}

# 6. discard() - Removes element if present, else does nothing
A.discard(5)
A.discard(100)  # No error if element is not present
print("discard():", A)  # {1, 2, 3, 4}

# 7. intersection() - Returns common elements
print("intersection():", A.intersection(B))  # {4}

# 8. intersection_update() - Updates A with common elements
A.intersection_update(B)
print("intersection_update():", A)  # {4}

# Reset A for next operations
A = {1, 2, 3, 4, 5}

# 9. isdisjoint() - Checks if two sets have no elements in common
print("isdisjoint():", A.isdisjoint({6, 7}))  # True
print("isdisjoint():", A.isdisjoint(B))  # False

# 10. issubset() - Checks if A is a subset of B
print("issubset():", C.issubset(A))  # True

# 11. issuperset() - Checks if A is a superset of C
print("issuperset():", A.issuperset(C))  # True

# 12. pop() - Removes and returns an arbitrary element
removed_element = A.pop()
print("pop():", removed_element, "Remaining Set:", A)  # Removed element, remaining set

# 13. remove() - Removes an element (raises error if not found)
A.remove(4)  
print("remove():", A)  # {2, 3, 5}

# 14. symmetric_difference() - Returns elements not common in both sets
print("symmetric_difference():", A.symmetric_difference(B))  # {2, 3, 5, 6, 7, 8}

# 15. symmetric_difference_update() - Updates A with elements not common in both sets
A.symmetric_difference_update(B)
print("symmetric_difference_update():", A)  # {2, 3, 5, 6, 7, 8}

# Reset A for next operations
A = {1, 2, 3, 4, 5}

# 16. union() - Returns a new set with all unique elements
print("union():", A.union(B))  # {1, 2, 3, 4, 5, 6, 7, 8}

# 17. update() - Adds elements from another set
A.update(B)
print("update():", A)  # {1, 2, 3, 4, 5, 6, 7, 8}
###```

#---

### **Summary Table of Set Methods**
'''| **Method** | **Description** |
|------------|----------------|
| `add(x)` | Adds element `x` to the set |
| `clear()` | Removes all elements from the set |
| `copy()` | Returns a shallow copy of the set |
| `difference(set2)` | Returns elements present in `set1` but not in `set2` |
| `difference_update(set2)` | Removes elements found in `set2` from `set1` |
| `discard(x)` | Removes `x` if present; does nothing if absent |
| `intersection(set2)` | Returns a new set with common elements |
| `intersection_update(set2)` | Updates `set1` with common elements |
| `isdisjoint(set2)` | Checks if two sets have no elements in common |
| `issubset(set2)` | Checks if `set1` is a subset of `set2` |
| `issuperset(set2)` | Checks if `set1` is a superset of `set2` |
| `pop()` | Removes and returns a random element |
| `remove(x)` | Removes `x`, raises error if absent |
| `symmetric_difference(set2)` | Returns a set with elements not common in both sets |
| `symmetric_difference_update(set2)` | Updates `set1` with elements not common in both sets |
| `union(set2)` | Returns a new set with all unique elements |
| `update(set2)` | Adds elements from `set2` to `set1` |

---

This covers **all set methods** in Python with examples. Let me know if you need further clarifications! '''