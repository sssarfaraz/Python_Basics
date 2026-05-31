# print fuction in multiple use cases

PRINT()

1. Build-in Python Function

2. Display Message in output for users

3. Use Cases:
    Communicate, Show Results, Debigg,Test


# example 1:

print( "Hello World")

# example 2:

print('Hello World')\

# example 3:

print("----------------------------")
print("    Hello World    ")

print("----------------------------")

# Normal characters

A B Z
5 9 0
@ ?

# Speial characters

1. \" (doule quote)
2. \' (single quote)
3. \\ (double backslash)
4. \n (New Line)
5. \t (Tab)
6. \b (Backspace)

# Examples

\"

print("Hi "Python"")
# It's wrong

# Correct format
print("Hi \"Python\"")
print('Hi "Python"')
print('Hi \'Python\'')

# Examples

print("Path C:\Users\Syed")
It's wrong

# Correct format
print("Path C:\\Users\\Syed")

# Exmaples

print("Message1")
print("Messeage2")

print("Message1")
print()
print("Messeage2")

print("Message1\n")
print("Messeage2")

print("Message1\n\n\n")
print("Messeage2")

print("Message1\nMesseage2") (Single line)
print("Message1\n\n\nMesseage2") (Double lines)
print("Message1\n\n\nMesseage2") (Three Lines)
print("Message1\tMesseage2") (With space)


# Print Using single line
# print("Your learning Path:\n\t-Python Basics-\n\t-DataEnineering\n\t-AI

# Print using multiple lines (Triplequotes)(""")
# print("Your learning Path:\n\t-Python Basics-\n\t-DataEnineering\n\t-AI

# With Extra Spaces
print("""ur learning Path:
\n\t-Python Basics-
\n\t-DataEnineering
\n\t-AI""")

# Without Extra Spaces

# print("""our Learning Path:
\t-Python Basics
\t-DataEnineering
\t-AI""")

# Best Eample for Real-wold use cases

# Example of print function in real use case

price_shirt = 25.00
price_pants = 45.50

qty_shirt = 2
qty_pants = 1

total_shirt = price_shirt * qty_shirt
total_pants = price_pants * qty_pants
subtotal = total_shirt + total_pants
print("Subtotal:", subtotal)
discount = subtotal * 0.10
print("Discount:", discount)
final_total = subtotal - discount
print("Final Total:", final_total)






