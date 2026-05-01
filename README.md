# Python_Picsine

A comprehensive Python learning curriculum designed to progressively build programming skills through practical exercises. The project uses a garden/nature theme to make learning engaging and relatable.

## 📚 Project Overview

Python_Picsine is an educational project containing 11 progressive modules (Python_Module_00 through Python_Module_10), each focusing on specific Python concepts and skills. Each module contains multiple exercises that build upon previous knowledge.

## 📦 Module Structure

### Python_Module_00: Fundamentals

Introduction to basic Python concepts including:

- Simple functions
- Output and printing
- Basic calculations
- String manipulation
- **Exercises**: ex0-ex7

### Python_Module_01: Object-Oriented Programming Basics

Introduction to classes and objects:

- Class definition and instantiation
- Instance attributes and methods
- Introduction to OOP principles
- **Exercises**: ex0-ex6

### Python_Module_02: Exception Handling

Error handling and robust code:

- Try-except blocks
- Exception types and custom errors
- Finally blocks
- Raising exceptions
- **Exercises**: ex0-ex5

### Python_Module_03: Data Structures & Collections

Working with complex data types:

- Lists and list manipulation
- Dictionaries and key-value pairs
- Sets and other collections
- Data organization and management
- **Exercises**: ex0-ex6

### Python_Module_04: File I/O & Context Management

Working with files and resources:

- Reading and writing files
- Context managers (with statements)
- File operations and stream handling
- **Exercises**: ex0-ex4

### Python_Module_05: Data Processing

Introduction to data processing patterns:

- Data stream handling
- Pipeline architecture
- Processing workflows
- **Files**: data_processor.py, data_stream.py, data_pipeline.py

### Python_Module_06: Packages & Modules

Organizing code into packages:

- Creating and structuring packages
- Module imports and namespaces
- Subpackage organization (alchemy package with submodules)
- **Exercises**: ft*alembic*_, ft*distillation*_, ft*kaboom*_, ft*transmutation*_
- **Package**: alchemy/ (with elements, potions, transmutation subpackages)

### Python_Module_07: Advanced OOP

Object-oriented design patterns:

- Inheritance and polymorphism
- Strategy patterns
- Complex class hierarchies
- **Files**: battle.py, capacitor.py, tournament.py
- **Exercises**: ex0 (normal), ex1 (capabilities), ex2 (strategies)

### Python_Module_08: External Dependencies & Configuration

Working with third-party libraries:

- Package management with requirements.txt
- Project configuration (pyproject.toml)
- Dependency management
- **Exercises**: ex0-ex2

### Python_Module_09: Advanced Concepts

Complex programming patterns:

- Specialized implementations
- **Exercises**: ex0-ex2

### Python_Module_10: Functional Programming

Functional programming paradigms:

- Lambda functions
- Higher-order functions
- Functional approach to problem-solving
- **Exercises**: ex0+

## 🗂️ Project Structure

```
Python_Picsine/
├── Python_Module_00/
│   ├── ex0/
│   ├── ex1/
│   └── ...
├── Python_Module_01/
│   ├── ex0/
│   ├── ex1/
│   └── ...
├── ...
└── Python_Module_10/
    ├── ex0/
    ├── ex1/
    └── ...
```

Each exercise folder contains Python files with implementations and/or test functions.

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- A terminal or command prompt
- A text editor or IDE (VS Code recommended)

### Running Exercises

To run an exercise:

```bash
# Navigate to the exercise directory
cd Python_Module_00/ex0

# Run the Python file
python ft_hello_garden.py
```

For exercises with test functions, run them directly:

```bash
# Run with test function
python ft_first_exception.py
```

### Running with Dependencies

Some modules may have external dependencies. Check for `requirements.txt`:

```bash
# Install dependencies (e.g., in Python_Module_08/ex1)
pip install -r requirements.txt

# Then run the exercise
python solution.py
```

## 📖 Learning Path

1. Start with **Python_Module_00** to learn fundamentals
2. Progress through **Python_Module_01** for OOP basics
3. Continue sequentially through each module
4. Complete exercises in order within each module
5. Use later modules to reinforce and expand knowledge

Each module builds on concepts from previous modules, so sequential learning is recommended.

## 🎯 Key Concepts Covered

- **Functions & Control Flow**: Conditionals, loops, function definition
- **Object-Oriented Programming**: Classes, inheritance, polymorphism, design patterns
- **Exception Handling**: Error handling, custom exceptions, resource management
- **Data Structures**: Lists, dictionaries, sets, complex collections
- **File I/O**: Reading/writing files, context managers, streams
- **Packages & Modules**: Code organization, namespacing, imports
- **Functional Programming**: Lambda functions, higher-order functions, functional patterns
- **Best Practices**: Code organization, dependency management, project configuration

## 💡 Tips for Success

- Read the code carefully and understand what each function does
- Run exercises and modify them to experiment
- Pay attention to type hints and function signatures
- Test your understanding by creating your own examples
- Progress at your own pace through the modules

## 📝 Exercise Format

Most exercises follow this pattern:

```python
def function_name(parameters) -> return_type:
    """Function documentation."""
    # Implementation
    pass

def test_function() -> None:
    """Test or demonstration function."""
    # Test code
    pass

if __name__ == "__main__":
    test_function()
```

Run the file directly to see the exercise in action.

## 🔧 Development Tools

Recommended tools for working with this project:

- **Editor**: VS Code with Python extension
- **Linter**: pylint or flake8
- **Formatter**: black or autopep8
- **Type Checker**: mypy

## 📄 License

This project is part of an educational curriculum.

## 🤝 Contributing

This is a learning project. Modifications and experiments are encouraged!

---

**Happy Learning!** 🌱🌿🌳
