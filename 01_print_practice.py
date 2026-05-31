"""
Python Basics - Print Function Practice Exercises
==================================================

This module contains beginner-level practice exercises focused on the print() function.
Each exercise is designed to help you master different aspects of printing in Python.

Difficulty Levels:
- ⭐ Easy: Basic concepts
- ⭐⭐ Medium: Combined concepts
- ⭐⭐⭐ Hard: Advanced techniques
"""

# ============================================================================
# SECTION 1: BASIC PRINTING - ⭐ Easy
# ============================================================================

def exercise_1_1_hello_world():
    """
    Exercise 1.1: Print a simple greeting
    
    Task: Print the text "Hello, World!" to the console
    Expected Output:
        Hello, World!
    """
    print("Hello, World!")


def exercise_1_2_multiple_lines():
    """
    Exercise 1.2: Print multiple lines of text
    
    Task: Print three different greetings, each on a new line
    Expected Output:
        Welcome to Python!
        Let's learn together!
        Happy coding!
    """
    print("Welcome to Python!")
    print("Let's learn together!")
    print("Happy coding!")


def exercise_1_3_print_numbers():
    """
    Exercise 1.3: Print numbers
    
    Task: Print the numbers 1 through 5, each on a separate line
    Expected Output:
        1
        2
        3
        4
        5
    """
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)


def exercise_1_4_mixed_data():
    """
    Exercise 1.4: Print mixed data types
    
    Task: Print a string, an integer, and a decimal number
    Expected Output:
        Python
        2024
        3.14
    """
    print("Python")
    print(2024)
    print(3.14)


# ============================================================================
# SECTION 2: MULTIPLE ARGUMENTS - ⭐ Easy
# ============================================================================

def exercise_2_1_multiple_arguments():
    """
    Exercise 2.1: Print multiple arguments in one statement
    
    Task: Print three words separated by spaces using a single print() call
    Expected Output:
        Hello Python World
    """
    print("Hello", "Python", "World")


def exercise_2_2_mixed_types_single_line():
    """
    Exercise 2.2: Print different data types in one line
    
    Task: Print a name (string), age (integer), and score (float) in one line
    Expected Output:
        Alice 25 95.5
    """
    print("Alice", 25, 95.5)


def exercise_2_3_print_with_labels():
    """
    Exercise 2.3: Print with descriptive labels
    
    Task: Print information about a person with labels
    Expected Output:
        Name: John
        Age: 30
        City: New York
    """
    print("Name:", "John")
    print("Age:", 30)
    print("City:", "New York")


def exercise_2_4_print_mathematical_result():
    """
    Exercise 2.4: Print the result of mathematical operations
    
    Task: Print the result of 10 + 5 with a label
    Expected Output:
        Result: 15
    """
    print("Result:", 10 + 5)


# ============================================================================
# SECTION 3: SEP PARAMETER - ⭐ Medium
# ============================================================================

def exercise_3_1_custom_separator():
    """
    Exercise 3.1: Use custom separator with sep parameter
    
    Task: Print three words separated by hyphens instead of spaces
    Expected Output:
        Apple-Banana-Cherry
    """
    print("Apple", "Banana", "Cherry", sep="-")


def exercise_3_2_no_separator():
    """
    Exercise 3.2: Print with no separator between items
    
    Task: Print numbers 1, 2, 3 without any separator
    Expected Output:
        123
    """
    print(1, 2, 3, sep="")


def exercise_3_3_comma_separator():
    """
    Exercise 3.3: Print with comma separator
    
    Task: Print a list of items separated by commas
    Expected Output:
        Python, JavaScript, Java, C++
    """
    print("Python", "JavaScript", "Java", "C++", sep=", ")


def exercise_3_4_pipe_separator():
    """
    Exercise 3.4: Print with pipe separator
    
    Task: Print information separated by pipes
    Expected Output:
        ID | Name | Score
    """
    print("ID", "Name", "Score", sep=" | ")


def exercise_3_5_custom_separator_table():
    """
    Exercise 3.5: Print table-like data with custom separators
    
    Task: Print a simple table row with data separated by spaces and pipes
    Expected Output:
        1 | John | 95
        2 | Jane | 87
    """
    print(1, "John", 95, sep=" | ")
    print(2, "Jane", 87, sep=" | ")


# ============================================================================
# SECTION 4: END PARAMETER - ⭐ Medium
# ============================================================================

def exercise_4_1_no_newline():
    """
    Exercise 4.1: Print without newline
    
    Task: Print three words on the same line using end parameter
    Expected Output:
        Hello World !
    """
    print("Hello", end=" ")
    print("World", end=" ")
    print("!")


def exercise_4_2_custom_ending():
    """
    Exercise 4.2: Print with custom ending
    
    Task: Print three lines with custom ending (dash)
    Expected Output:
        Line 1-
        Line 2-
        Line 3
    """
    print("Line 1", end="-\n")
    print("Line 2", end="-\n")
    print("Line 3")


def exercise_4_3_inline_sequence():
    """
    Exercise 4.3: Print a sequence inline
    
    Task: Print numbers 1-5 on the same line
    Expected Output:
        1 2 3 4 5
    """
    print(1, end=" ")
    print(2, end=" ")
    print(3, end=" ")
    print(4, end=" ")
    print(5)


def exercise_4_4_progress_bar():
    """
    Exercise 4.4: Simulate a simple progress indicator
    
    Task: Print dots on the same line to simulate progress
    Expected Output:
        ...
    """
    print(".", end="")
    print(".", end="")
    print(".")


def exercise_4_5_custom_separator_with_ending():
    """
    Exercise 4.5: Combine sep and end parameters
    
    Task: Print coordinates with hyphen separator and pipe ending
    Expected Output:
        10-20|30-40|
    """
    print(10, 20, sep="-", end="|")
    print(30, 40, sep="-", end="|")


# ============================================================================
# SECTION 5: ESCAPE SEQUENCES - ⭐⭐ Medium
# ============================================================================

def exercise_5_1_newline_escape():
    """
    Exercise 5.1: Use newline escape sequence
    
    Task: Print text with newline characters within a single print()
    Expected Output:
        Line 1
        Line 2
        Line 3
    """
    print("Line 1\nLine 2\nLine 3")


def exercise_5_2_tab_escape():
    """
    Exercise 5.2: Use tab escape sequence
    
    Task: Print formatted table using tabs
    Expected Output:
        Name    Age    City
        John    25     NYC
    """
    print("Name\tAge\tCity")
    print("John\t25\tNYC")


def exercise_5_3_mixed_escapes():
    """
    Exercise 5.3: Mix different escape sequences
    
    Task: Print formatted information using tabs and newlines
    Expected Output:
        Product:    Laptop
        Price:      $999
        In Stock:   Yes
    """
    print("Product:\tLaptop\nPrice:\t$999\nIn Stock:\tYes")


def exercise_5_4_quote_escaping():
    """
    Exercise 5.4: Escape quotes in strings
    
    Task: Print a sentence with quotes inside
    Expected Output:
        He said: "Hello!"
    """
    print('He said: "Hello!"')


def exercise_5_5_backslash():
    r"""
    Exercise 5.5: Print a backslash
    
    Task: Print text that contains a backslash
    Expected Output:
        Path: C:\Users\Documents
    """
    print("Path: C:\\Users\\Documents")


# ============================================================================
# SECTION 6: F-STRINGS - ⭐⭐ Medium
# ============================================================================

def exercise_6_1_basic_f_string():
    """
    Exercise 6.1: Use f-strings for variable interpolation
    
    Task: Print a greeting using an f-string with a variable
    Expected Output:
        Hello, Alice!
    """
    name = "Alice"
    print(f"Hello, {name}!")


def exercise_6_2_multiple_variables():
    """
    Exercise 6.2: Use f-strings with multiple variables
    
    Task: Print person information using f-string
    Expected Output:
        John is 30 years old
    """
    name = "John"
    age = 30
    print(f"{name} is {age} years old")


def exercise_6_3_f_string_with_operations():
    """
    Exercise 6.3: Use f-strings with expressions
    
    Task: Print the result of an operation using f-string
    Expected Output:
        5 + 3 = 8
    """
    a = 5
    b = 3
    print(f"{a} + {b} = {a + b}")


def exercise_6_4_f_string_formatting():
    """
    Exercise 6.4: Format numbers in f-strings
    
    Task: Print a price formatted to 2 decimal places
    Expected Output:
        Price: $19.99
    """
    price = 19.99
    print(f"Price: ${price:.2f}")


def exercise_6_5_f_string_alignment():
    """
    Exercise 6.5: Use f-string alignment for table formatting
    
    Task: Print aligned data using f-strings
    Expected Output:
        Item       Price
        Apples     $2.99
        Oranges    $3.49
    """
    print(f"{'Item':<10} {'Price':>7}")
    print(f"{'Apples':<10} {'$2.99':>7}")
    print(f"{'Oranges':<10} {'$3.49':>7}")


# ============================================================================
# SECTION 7: STRING CONCATENATION - ⭐⭐ Medium
# ============================================================================

def exercise_7_1_basic_concatenation():
    """
    Exercise 7.1: Concatenate strings with +
    
    Task: Create a full greeting by concatenating strings
    Expected Output:
        Good morning, World!
    """
    greeting = "Good morning, " + "World!"
    print(greeting)


def exercise_7_2_concatenation_with_conversion():
    """
    Exercise 7.2: Concatenate strings with type conversion
    
    Task: Print a message with a number converted to string
    Expected Output:
        I have 5 apples
    """
    message = "I have " + str(5) + " apples"
    print(message)


def exercise_7_3_concatenation_multiline():
    """
    Exercise 7.3: Concatenate multiple strings
    
    Task: Create a complete sentence from multiple parts
    Expected Output:
        My name is Alice and I am 28 years old.
    """
    sentence = "My name is " + "Alice" + " and I am " + str(28) + " years old."
    print(sentence)


# ============================================================================
# SECTION 8: ADVANCED FORMATTING - ⭐⭐⭐ Hard
# ============================================================================

def exercise_8_1_ascii_art():
    """
    Exercise 8.1: Print ASCII art using escape sequences
    
    Task: Print a simple box using special characters
    Expected Output:
        +-----+
        |     |
        +-----+
    """
    print("+-----+")
    print("|     |")
    print("+-----+")


def exercise_8_2_formatted_table():
    """
    Exercise 8.2: Create a formatted table
    
    Task: Print a table with aligned columns
    Expected Output:
        ID  Name    Score
        1   Alice   95
        2   Bob     87
        3   Charlie 92
    """
    print("ID  Name    Score")
    print("1   Alice   95")
    print("2   Bob     87")
    print("3   Charlie 92")


def exercise_8_3_complex_separator_output():
    """
    Exercise 8.3: Print complex data with different separators
    
    Task: Print inventory data with different formatting for each line
    Expected Output:
        Item: Apple, Price: $1.50, Quantity: 10
        Item: Banana, Price: $0.75, Quantity: 20
    """
    print("Item: Apple, Price: $1.50, Quantity: 10")
    print("Item: Banana, Price: $0.75, Quantity: 20")


def exercise_8_4_multilevel_formatting():
    """
    Exercise 8.4: Combine multiple formatting techniques
    
    Task: Create a formatted report using different techniques
    Expected Output:
        ========== Report ==========
        Name    : John Doe
        Age     : 30
        Location: New York
        Score   : 95.5
        =============================
    """
    print("========== Report ==========")
    print("Name    : John Doe")
    print("Age     : 30")
    print("Location: New York")
    print("Score   : 95.5")
    print("=============================")


def exercise_8_5_interactive_output():
    """
    Exercise 8.5: Print multiple pieces of information with consistent formatting
    
    Task: Print formatted product information
    Expected Output:
        Product Details
        ---------------
        Name: Laptop
        Brand: Dell
        Price: $899.99
        Stock: In Stock
    """
    print("Product Details")
    print("---------------")
    print(f"Name: {'Laptop'}")
    print(f"Brand: {'Dell'}")
    print(f"Price: ${899.99}")
    print(f"Stock: {'In Stock'}")


# ============================================================================
# SOLUTION RUNNER - Uncomment to test exercises
# ============================================================================

def run_all_exercises():
    """
    Run all exercises and display their output
    """
    exercises = [
        # Section 1
        ("1.1 Hello World", exercise_1_1_hello_world),
        ("1.2 Multiple Lines", exercise_1_2_multiple_lines),
        ("1.3 Print Numbers", exercise_1_3_print_numbers),
        ("1.4 Mixed Data", exercise_1_4_mixed_data),
        # Section 2
        ("2.1 Multiple Arguments", exercise_2_1_multiple_arguments),
        ("2.2 Mixed Types Single Line", exercise_2_2_mixed_types_single_line),
        ("2.3 Print with Labels", exercise_2_3_print_with_labels),
        ("2.4 Mathematical Result", exercise_2_4_print_mathematical_result),
        # Section 3
        ("3.1 Custom Separator", exercise_3_1_custom_separator),
        ("3.2 No Separator", exercise_3_2_no_separator),
        ("3.3 Comma Separator", exercise_3_3_comma_separator),
        ("3.4 Pipe Separator", exercise_3_4_pipe_separator),
        ("3.5 Custom Separator Table", exercise_3_5_custom_separator_table),
        # Section 4
        ("4.1 No Newline", exercise_4_1_no_newline),
        ("4.2 Custom Ending", exercise_4_2_custom_ending),
        ("4.3 Inline Sequence", exercise_4_3_inline_sequence),
        ("4.4 Progress Bar", exercise_4_4_progress_bar),
        ("4.5 Separator with Ending", exercise_4_5_custom_separator_with_ending),
        # Section 5
        ("5.1 Newline Escape", exercise_5_1_newline_escape),
        ("5.2 Tab Escape", exercise_5_2_tab_escape),
        ("5.3 Mixed Escapes", exercise_5_3_mixed_escapes),
        ("5.4 Quote Escaping", exercise_5_4_quote_escaping),
        ("5.5 Backslash", exercise_5_5_backslash),
        # Section 6
        ("6.1 Basic F-String", exercise_6_1_basic_f_string),
        ("6.2 Multiple Variables", exercise_6_2_multiple_variables),
        ("6.3 F-String Operations", exercise_6_3_f_string_with_operations),
        ("6.4 F-String Formatting", exercise_6_4_f_string_formatting),
        ("6.5 F-String Alignment", exercise_6_5_f_string_alignment),
        # Section 7
        ("7.1 Basic Concatenation", exercise_7_1_basic_concatenation),
        ("7.2 Concatenation with Conversion", exercise_7_2_concatenation_with_conversion),
        ("7.3 Multiline Concatenation", exercise_7_3_concatenation_multiline),
        # Section 8
        ("8.1 ASCII Art", exercise_8_1_ascii_art),
        ("8.2 Formatted Table", exercise_8_2_formatted_table),
        ("8.3 Complex Separator Output", exercise_8_3_complex_separator_output),
        ("8.4 Multilevel Formatting", exercise_8_4_multilevel_formatting),
        ("8.5 Interactive Output", exercise_8_5_interactive_output),
    ]
    
    for name, exercise_func in exercises:
        print(f"\n{'='*60}")
        print(f"Exercise {name}")
        print(f"{'='*60}")
        exercise_func()
    
    print(f"\n{'='*60}")
    print("All exercises completed!")
    print(f"{'='*60}")


if __name__ == "__main__":
    # Run all exercises
    run_all_exercises()
