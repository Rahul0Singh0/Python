# 🐍 Python Basics – Theory Notes

These notes cover **everything learned so far** in Python, written in **README format** for revision, GitHub, and interviews.

---

## 📌 What is Python?

**Interview Definition:**  
Python is a **high-level, interpreted, dynamically typed, object-oriented programming language** designed for **readability and rapid development**.

**Key Points (Interview):**
- High-level → human-readable syntax
- Interpreted → executed line by line
- Dynamically typed → no need to declare data types
- Object-oriented → supports OOP concepts

---

## 📌 Python Installation & First Program

### Check Python Version
```bash
python --version
```

### First Python Program
```python
print("Hello, World!")
```

---

## 📌 Variables & Data Types

**Interview Definition:**  
A variable is a **name that refers to a memory location** used to store data values.

Python variables are **dynamically typed**, meaning the type is decided at runtime.

```python
x = 10      # int
y = 10.5    # float
name = "Rahul"  # string
```

**Interview Questions:**
- Q: Why is Python called dynamically typed?
- A: Because variable types are determined at runtime, not at declaration.

---

## 📌 Input & Output

```python
name = input("Enter name: ")
age = int(input("Enter age: "))
print(name, age)
```

📌 `input()` always returns **string**.

---

## 📌 Operators

**Interview Definition:**  
Operators are **symbols used to perform operations** on operands.

**Types of Operators (Interview):**
- Arithmetic (`+ - * / %`)
- Comparison (`== != > < >= <=`)
- Logical (`and or not`)

**Interview Q:**
- Q: Difference between `=` and `==`?
- A: `=` assigns value, `==` compares values.

---

## 📌 Conditional Statements

**Interview Definition:**  
Conditional statements are used to **execute code based on conditions**.

**Types:**
- if
- if-else
- if-elif-else

**Interview Q:**
- Q: Does Python support switch-case?
- A: Yes, using `match-case` (Python 3.10+).

---

## 📌 Loops

**Interview Definition:**  
Loops are used to **repeat a block of code multiple times**.

**Types of Loops:**
- for loop → known iterations
- while loop → condition-based

**Interview Q:**
- Q: Difference between for and while loop?
- A: for is iteration-based, while is condition-based.

---

## 📌 Functions in Python

**Interview Definition:**  
A function is a **reusable block of code that performs a specific task and returns a result**.

**Why Functions? (Interview):**
- Code reusability
- Modularity
- Easy debugging

---

### Simple Function
```python
def greet():
    print("Hello")
```

---

### Function with Parameters
```python
def greet(name):
    print("Hello", name)
```

---

### Function with Return
```python
def add(a, b):
    return a + b
```

---

### Default Parameters
```python
def greet(name="User"):
    print("Hello", name)
```

---

### Keyword Arguments
```python
def student(name, age):
    print(name, age)

student(age=24, name="Rahul")
```

---

### *args (Variable Arguments)
```python
def total(*nums):
    return sum(nums)
```

---

### **kwargs (Keyword Arguments)
```python
def info(**data):
    print(data)
```

---

### Lambda Function

**Interview Definition:**  
A lambda function is a **small anonymous function written in a single line**.

```python
lambda a, b: a + b
```

**Interview Q:**
- Q: When should lambda be used?
- A: For short, one-time operations.

---

### Recursion

**Interview Definition:**  
Recursion is a technique where a **function calls itself** to solve a problem.

**Important Rule (Interview):**
- Must have a **base condition** to stop recursion.

---

## 📌 Variable Scope

**Interview Definition:**  
Scope defines the **accessibility of a variable** inside or outside functions.

**Types:**
- Local scope
- Global scope

**Interview Q:**
- Q: What is the `global` keyword?
- A: Used to modify global variables inside functions.

---

## 📌 Docstring

**Interview Definition:**  
A docstring is a **string literal used to document functions, classes, or modules**.

**Interview Q:**
- Q: How to access docstring?
- A: Using `__doc__` attribute.

---

## 📌 Common Built-in Functions

- `len()`
- `type()`
- `sum()`
- `max()`
- `min()`
- `sorted()`

---

## 📌 Interview Notes (Important)

- Python is dynamically typed
- `return` sends value, `print` displays
- Functions can return multiple values
- `*args` → tuple, `**kwargs` → dictionary
- Time complexity matters in loops & recursion

---

## ✅ Topics Covered So Far

✔ Python basics
✔ Variables & Data Types
✔ Operators
✔ Conditions
✔ Loops
✔ Functions (complete)
✔ Recursion

🚀 Happy Coding!

