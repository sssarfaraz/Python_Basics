# Python Basics Course - Complete Guide

## Table of Contents
1. [Introduction to Python](#introduction-to-python)
2. [Chapter 1: The print() Function](#chapter-1-the-print-function)
3. [Chapter 2: Variables and Data Types](#chapter-2-variables-and-data-types)
4. [Chapter 3: Basic Operations](#chapter-3-basic-operations)

---

## Introduction to Python

Python is a high-level, interpreted programming language known for its simplicity and readability. It's perfect for beginners and widely used in professional development.

**Why Python?**
- Easy to learn and read
- Powerful and flexible
- Large community support
- Used in data science, web development, automation, and more

---

## Chapter 1: The print() Function

### What is the print() Function?

The `print()` function is one of the most fundamental functions in Python. It outputs text or data to the console (terminal/command prompt).

### Syntax

```python
print(object(s), sep=' ', end='\n', file=sys.stdout, flush=False)
```

### Basic Usage

#### 1.1 Printing Simple Text

```python
print("Hello, World!")
```

**Output:**
```
Hello, World!
```

#### 1.2 Printing Without Quotes

When you use `print()`, the string content is displayed without the surrounding quotes.

```python
print("Python is awesome!")
print("Welcome to coding!")
```

**Output:**
```
Python is awesome!
Welcome to coding!
```

#### 1.3 Printing Multiple Items

Use commas to separate multiple items. By default, they are separated by spaces.

```python
print("Hello", "World", "!")
```

**Output:**
```
Hello World !
```

#### 1.4 Printing Numbers

```python
print(42)
print(3.14)
print(100)
```

**Output:**
```
42
3.14
100
```

#### 1.5 Printing Mixed Data Types

```python
print("Age:", 25)
print("Price:", 99.99)
print("Count:", 1000)
```

**Output:**
```
Age: 25
Price: 99.99
Count: 1000
```

### Advanced print() Parameters

#### 1.6 The `sep` Parameter (Separator)

The `sep` parameter defines what separates multiple items. Default is a space `' '`.

```python
print("A", "B", "C", sep="-")
print("X", "Y", "Z", sep=":")
print("1", "2", "3", sep="")
```

**Output:**
```
A-B-C
X:Y:Z
123
```

#### 1.7 The `end` Parameter

The `end` parameter defines what comes at the end of the print statement. Default is newline `'\n'`.

```python
print("Hello", end=" ")
print("World")
```

**Output:**
```
Hello World
```

**Example 2:**

```python
print("A", end="-")
print("B", end="-")
print("C")
```

**Output:**
```
A-B-C
```

#### 1.8 Combining sep and end

```python
print("Name", "Age", sep=":", end=" | ")
print("John", 25, sep=":")
```

**Output:**
```
Name:Age | John:25
```

### Escape Sequences

Escape sequences are special character combinations that produce specific formatting.

#### 1.9 Newline (`\n`)

```python
print("Line 1\nLine 2\nLine 3")
```

**Output:**
```
Line 1
Line 2
Line 3
```

#### 1.10 Tab (`\t`)

```python
print("Name\tAge\tCity")
print("John\t25\tNew York")
print("Jane\t30\tLos Angeles")
```

**Output:**
```
Name    Age    City
John    25     New York
Jane    30     Los Angeles
```

#### 1.11 Backslash (`\\`)

```python
print("This is a backslash: \\")
```

**Output:**
```
This is a backslash: \
```

#### 1.12 Quote Escaping

```python
print("She said: \"Hello!\"")
print('He said: \'Hi there\'')
```

**Output:**
```
She said: "Hello!"
He said: 'Hi there'
```

### Formatting Output

#### 1.13 String Concatenation

```python
print("Hello " + "World")
print("The answer is " + str(42))
```

**Output:**
```
Hello World
The answer is 42
```

#### 1.14 f-strings (Formatted String Literals) - Python 3.6+

```python
name = "Alice"
age = 28
print(f"My name is {name} and I am {age} years old")
```

**Output:**
```
My name is Alice and I am 28 years old
```

#### 1.15 String Methods

```python
print("hello world".upper())
print("PYTHON".lower())
print("   spaces   ".strip())
```

**Output:**
```
HELLO WORLD
python
spaces
```

---

## Chapter 2: Variables and Data Types

### What are Variables?

A variable is a named container that stores a value. You can change the value inside it, which is why it's called a "variable."

### Syntax

```python
variable_name = value
```

### Naming Rules

- Must start with a letter or underscore (`_`)
- Can contain letters, numbers, and underscores
- Case-sensitive (`age` and `Age` are different)
- Cannot use Python reserved words (keywords)
- Use snake_case for variable names: `my_variable`, `student_name`

### Basic Variable Assignment

```python
name = "John"
age = 25
height = 5.9
is_student = True
```

### Data Types

#### 2.1 String (`str`)

Text enclosed in quotes.

```python
greeting = "Hello"
message = 'Python is fun'
multiline = """This is a
multiline
string"""

print(greeting)
print(message)
print(multiline)
```

#### 2.2 Integer (`int`)

Whole numbers.

```python
age = 25
count = 1000
negative = -50

print(age)
print(count)
print(negative)
```

#### 2.3 Float (`float`)

Decimal numbers.

```python
height = 5.9
pi = 3.14159
temperature = -10.5

print(height)
print(pi)
print(temperature)
```

#### 2.4 Boolean (`bool`)

True or False values.

```python
is_active = True
is_admin = False

print(is_active)
print(is_admin)
```

### Type Conversion

Convert one data type to another.

```python
# String to Integer
num_str = "42"
num_int = int(num_str)
print(num_int)  # Output: 42

# Integer to String
age = 25
age_str = str(age)
print(age_str)  # Output: '25'

# Float to Integer
decimal = 3.14
whole = int(decimal)
print(whole)  # Output: 3

# String to Float
price_str = "19.99"
price_float = float(price_str)
print(price_float)  # Output: 19.99
```

### Checking Data Types

```python
name = "Alice"
age = 30
height = 5.8
is_student = True

print(type(name))       # Output: <class 'str'>
print(type(age))        # Output: <class 'int'>
print(type(height))     # Output: <class 'float'>
print(type(is_student)) # Output: <class 'bool'>
```

---

## Chapter 3: Basic Operations

### Arithmetic Operations

```python
a = 10
b = 3

print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.333...
print(a // b) # Floor Division: 3
print(a % b)  # Modulus (remainder): 1
print(a ** b) # Exponentiation: 1000
```

### String Operations

```python
# Concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe

# Repetition
print("Ha" * 3)  # Output: HaHaHa

# Length
text = "Hello"
print(len(text))  # Output: 5
```

### Variable Assignment Shortcut

```python
# Instead of: x = x + 5
x = 10
x += 5  # x is now 15

y = 20
y -= 3  # y is now 17

z = 4
z *= 2  # z is now 8
```

---

## Next Steps

- Master the concepts in this guide through practice
- Complete the practice exercises in `01_print_practice.py`
- Experiment with your own code
- Build small projects to reinforce your learning

---

**Happy Coding! 🐍**
