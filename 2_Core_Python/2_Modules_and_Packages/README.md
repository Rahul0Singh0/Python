# 🔹 What is a Module?

A module is a Python file (.py) that contains variables, functions, or classes, which can be reused in other programs.

## 📌 In short:

One file = One module

# 🧠 Why Modules?

- Code reusability

- Better organization

- Avoid code duplication

- Easy maintenance

# 🔹 Import Styles (INTERVIEW FAVORITE)

## 1️⃣ import module
import math_utils
math_utils.add(2, 3)

## 2️⃣ from module import function
from math_utils import add
print(add(2, 3))

## 3️⃣ Import multiple functions
from math_utils import add, subtract

## 4️⃣ Import everything (NOT recommended)
from math_utils import *


#### ⚠️ Interview Tip:
Avoid * because it causes namespace pollution

## 🔹 Rename Module (Alias)
import math_utils as mu

print(mu.add(5, 5))

## 📌 Used heavily in real projects (import numpy as np)


# 🔹 Built-in Modules (VERY IMPORTANT)
- math => Mathematical operations
- random =>	Random values
- datetime => Date & time
- os =>	OS-level operations
- sys => System-specific parameters


# 🔹 What is a Package?
A package is a collection of related modules stored in a directory.

📌 Package = Folder
📌 Module = File



# 🔹 What is __init__.py?

__init__.py tells Python that the folder should be treated as a package.

(It can be empty or contain initialization code.)

## 🔹 Relative vs Absolute Import (INTERVIEW)
### Absolute Import
from calculator.add import add

### Relative Import (inside package)
from .add import add


📌 Relative imports are used inside packages only

# 🧠 Interview Quick Q&A

Q: Difference between module and package?
➡️ Module = single .py file
➡️ Package = folder of modules

Q: What is namespace?
➡️ Container that holds identifiers (variables, functions)

Q: Are packages mandatory to have __init__.py?
➡️ Earlier yes, now optional (but still recommended)

