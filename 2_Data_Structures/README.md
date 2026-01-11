# 🧩 Python Data Structures – Interview Notes

This README contains **complete theory + interview-oriented definitions and Q&A** for Python Data Structures.

---

## 📘 1. List

### Interview Definition
A **list** is a **mutable, ordered collection** used to store multiple elements in a single variable.

```python
nums = [1, 2, 3, 4]
```

### Key Properties
- Ordered (maintains insertion order)
- Allows duplicate elements
- Mutable (can be modified)
- Supports indexing & slicing

### Common Operations
```python
nums.append(5)
nums.remove(2)
nums[0] = 10
```

### Interview Q&A
**Q: Difference between list and tuple?**  
A: List is mutable, tuple is immutable.

**Q: Why lists are slower than tuples?**  
A: Because lists support mutability.

---

## 📘 2. Tuple

### Interview Definition
A **tuple** is an **immutable, ordered collection** of elements.

```python
point = (10, 20)
```

### Key Properties
- Ordered
- Immutable
- Faster than lists
- Can be used as dictionary keys (if immutable)

### Interview Q&A
**Q: When should you use tuple instead of list?**  
A: When data should not be modified.

---

## 📘 3. Set

### Interview Definition
A **set** is an **unordered collection of unique elements**.

```python
nums = {1, 2, 3}
```

### Key Properties
- No duplicate values
- Unordered
- Mutable
- Uses hashing

### Common Operations
```python
nums.add(4)
nums.remove(2)
```

### Interview Q&A
**Q: Why sets are faster for searching?**  
A: Because they use hash tables.

---

## 📘 4. Dictionary

### Interview Definition
A **dictionary** stores data in the form of **key–value pairs**.

```python
student = {"name": "Rahul", "age": 24}
```

### Key Properties
- Keys must be unique
- Keys must be immutable
- Values can be mutable or immutable
- Fast lookup using hashing

### Common Operations
```python
student["age"] = 25
student.get("name")
```

### Interview Q&A
**Q: Why dictionary lookup is fast?**  
A: Because dictionaries use hash tables.

---

## 📊 Data Structure Comparison (Interview Favorite)

| Data Structure | Ordered | Mutable | Duplicates | Best Use Case |
|---------------|--------|--------|-----------|--------------|
| List | Yes | Yes | Yes | Dynamic data |
| Tuple | Yes | No | Yes | Fixed data |
| Set | No | Yes | No | Unique values |
| Dictionary | Yes | Yes | Keys No | Key-value mapping |

---

## 🧠 Interview Tips (Very Important)

- Prefer **tuple** over list when data should not change
- Use **set** for fast membership testing
- Use **dictionary** for mappings and fast lookup
- Lists consume more memory than tuples

---

## 📌 Common Interview Questions (Quick Revision)

1. Is Python dictionary ordered?
   - Yes (from Python 3.7+)
2. Can a list store different data types?
   - Yes
3. Can dictionary keys be lists?
   - No (lists are mutable)

---
