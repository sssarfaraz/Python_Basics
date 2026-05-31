# Python Print() Function - Quick Reference Guide

## 📌 Basic Syntax

```python
print(object(s), sep=' ', end='\n', file=sys.stdout, flush=False)
```

## 🔧 Essential Parameters

| Parameter | Default | Purpose |
|-----------|---------|---------|
| `object(s)` | - | What to print |
| `sep` | `' '` | Separator between objects |
| `end` | `'\n'` | What comes at the end |
| `file` | `sys.stdout` | Where to print (usually console) |
| `flush` | `False` | Force buffer flush |

---

## 📝 Quick Examples

### Basic Printing
```python
print("Hello, World!")                    # Output: Hello, World!
print(42)                                 # Output: 42
print(3.14)                               # Output: 3.14
print(True)                               # Output: True
```

### Multiple Arguments
```python
print("Hello", "World")                   # Output: Hello World
print("Age:", 25)                         # Output: Age: 25
print(1, 2, 3)                            # Output: 1 2 3
```

### Using `sep` Parameter
```python
print("A", "B", "C", sep="-")             # Output: A-B-C
print("1", "2", "3", sep="")              # Output: 123
print("X", "Y", "Z", sep=" | ")           # Output: X | Y | Z
```

### Using `end` Parameter
```python
print("Hello", end=" ")                   # Prints without newline
print("World")                            # Output on same line

# Combined:
print("A", end="-")
print("B", end="-")
print("C")                                # Output: A-B-C
```

### Combining `sep` and `end`
```python
print("X", "Y", sep=":", end=" | ")
print("A", "B", sep=":")                  # Output: X:Y | A:B
```

---

## 🎨 Escape Sequences

| Sequence | Meaning | Example |
|----------|---------|---------|
| `\n` | Newline | `print("Line1\nLine2")` |
| `\t` | Tab | `print("Col1\tCol2")` |
| `\\` | Backslash | `print("C:\\Users")` |
| `\'` | Single quote | `print('It\'s')` |
| `\"` | Double quote | `print("He said \"Hi\"")` |

### Escape Sequence Examples
```python
print("Line 1\nLine 2")                   # Multi-line output
print("Name\tAge\tCity")                  # Table-like output
print("Path: C:\\Users\\Documents")       # Windows path
print('He said: "Hello"')                 # Quotes inside
```

---

## ✨ String Formatting

### F-Strings (Python 3.6+)
```python
name = "Alice"
age = 30
print(f"Hello, {name}")                   # Output: Hello, Alice
print(f"{name} is {age} years old")       # Output: Alice is 30 years old
print(f"Result: {10 + 5}")                # Output: Result: 15
```

### F-String Formatting
```python
price = 19.99
print(f"Price: ${price:.2f}")             # Output: Price: $19.99
print(f"{name:>10}")                      # Right-aligned in 10 chars
print(f"{name:<10}")                      # Left-aligned in 10 chars
print(f"{number:05d}")                    # Pad with zeros
```

### String Concatenation
```python
print("Hello " + "World")                 # Output: Hello World
print("Number: " + str(42))               # Output: Number: 42
```

### String Methods
```python
print("hello".upper())                    # Output: HELLO
print("PYTHON".lower())                   # Output: python
print("hello world".title())              # Output: Hello World
print("  text  ".strip())                 # Output: text
print("a,b,c".split(","))                 # Output: ['a', 'b', 'c']
```

---

## 🎯 Common Use Cases

### Printing Variables
```python
x = 10
y = 20
print(x, y)                               # Output: 10 20
print(f"x={x}, y={y}")                    # Output: x=10, y=20
```

### Printing Calculations
```python
print(10 + 5)                             # Output: 15
print(f"10 + 5 = {10 + 5}")               # Output: 10 + 5 = 15
```

### Creating Tables
```python
print("Name    Age    City")
print("Alice   25     NYC")
print("Bob     30     LA")

# Or with sep:
print("Name", "Age", "City", sep="\t")
print("Alice", "25", "NYC", sep="\t")
```

### Progress Indicator
```python
print(".", end="", flush=True)
# (This prints dots without newline)
```

### Printing on Same Line
```python
for i in range(1, 4):
    print(i, end=" ")
# Output: 1 2 3
```

---

## 🚫 Common Mistakes

### ❌ Don't Forget Quotes
```python
print("Hello")      # ✓ Correct
print(Hello)        # ✗ Error - not a string
```

### ❌ Type Mismatch
```python
print("Age: " + str(25))  # ✓ Correct (convert to string)
print("Age: " + 25)       # ✗ Error - can't concatenate
```

### ❌ Newline Issues
```python
print("A", "B")     # Output: A B (with newline at end)
# To avoid newline:
print("A", "B", end="")
```

### ❌ Wrong Separator
```python
print("A", "B", sep="-")   # ✓ Correct
print("A" + "-" + "B")     # Also works but more tedious
```

---

## 🔢 Data Types You Can Print

```python
# String
print("text")               # Output: text

# Integer
print(42)                   # Output: 42

# Float
print(3.14)                 # Output: 3.14

# Boolean
print(True)                 # Output: True
print(False)                # Output: False

# List
print([1, 2, 3])            # Output: [1, 2, 3]

# Dictionary
print({"name": "Alice"})    # Output: {'name': 'Alice'}

# None
print(None)                 # Output: None
```

---

## 📊 Parameter Reference Table

### `sep` Parameter Examples
| Code | Output |
|------|--------|
| `print("A", "B", sep="-")` | A-B |
| `print("A", "B", sep="")` | AB |
| `print("A", "B", sep=" ")` | A B |
| `print("A", "B", sep="\t")` | A&nbsp;&nbsp;&nbsp;&nbsp;B |
| `print("A", "B", sep="\n")` | A<br>B |

### `end` Parameter Examples
| Code | Output (visual) |
|------|-----------------|
| `print("A"); print("B")` | A<br>B |
| `print("A", end=""); print("B")` | AB |
| `print("A", end=" "); print("B")` | A B |
| `print("A", end="\n"); print("B")` | A<br>B |
| `print("A", end="-")` | A- |

---

## 🎓 Tips for Mastery

1. **Experiment**: Try changing parameters in interactive Python shell
2. **Combine Features**: Mix `sep`, `end`, f-strings for complex output
3. **Use Variables**: Store values in variables before printing
4. **Test Edge Cases**: Try empty strings, special characters, very long strings
5. **Read Error Messages**: They usually tell you what's wrong

---

## 📚 Further Learning

- Official Python Docs: https://docs.python.org/3/library/functions.html#print
- PEP 8 Style Guide: https://www.python.org/dev/peps/pep-0008/
- Python String Methods: https://docs.python.org/3/library/stdtypes.html#string-methods

---

**Happy Printing! 🐍**
