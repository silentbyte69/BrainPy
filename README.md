# BrainPy

[![PyPI version](https://img.shields.io/pypi/v/brainpy.svg)](https://pypi.org/project/brainpy/)
[![Python versions](https://img.shields.io/pypi/pyversions/brainpy.svg)](https://pypi.org/project/brainpy/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/silentbyte69/brainpy/actions/workflows/test.yml/badge.svg)](https://github.com/silentbyte69/brainpy/actions/workflows/test.yml)
[![Code Coverage](https://codecov.io/gh/silentbyte69/brainpy/branch/main/graph/badge.svg)](https://codecov.io/gh/silentbyte69/brainpy)

BrainPy is a powerful Python library that converts Brainfuck code to Python and executes it seamlessly. Whether you want to run Brainfuck programs in Python, convert them to readable Python code, or integrate Brainfuck execution into your projects, BrainPy makes it simple and efficient.

## Features

- 🚀 **Direct Execution**: Run Brainfuck code directly in Python
- 📝 **Code Conversion**: Convert Brainfuck code to human-readable Python
- 🔧 **Flexible Configuration**: Customizable memory size and input handling
- 🛡️ **Error Handling**: Comprehensive syntax validation and runtime error reporting
- 💻 **CLI Support**: Command-line interface for easy file execution
- 📦 **Lightweight**: No dependencies, pure Python implementation

## Installation

```bash
pip install brainpy
```

Quick Start

Basic Usage

```python
import brainpy

# Execute Brainfuck code directly
result = brainpy.execute("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.")
print(result)  # Output: "Hello World!\n"

# Convert Brainfuck to Python code
python_code = brainpy.compile_to_python("+++>++<[->+<]>.")
print(python_code)
```

Using the Class Interface

```python
from brainpy import BrainPy

# Create an interpreter
interpreter = BrainPy(memory_size=30000)

# Execute with input
result = interpreter.execute(",.", "A")  # Reads input and outputs it
print(result)  # Output: "A"

# Or use direct execution (more efficient)
result = interpreter.execute_direct("+++[>++<-]>.")
print(result)
```

Command Line Usage

BrainPy comes with a convenient command-line interface:

```bash
# Execute a Brainfuck file
brainpy hello_world.bf

# Execute Brainfuck code from string
brainpy -c "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."

# Compile to Python without executing
brainpy --compile-only -o output.py program.bf

# Execute with input data
brainpy -i "input data" program.bf

# Set custom memory size
brainpy -m 50000 program.bf
```

API Reference

Functions

execute(brainfuck_code, input_data="", memory_size=30000)

Execute Brainfuck code directly and return the output.

Parameters:

· brainfuck_code (str): Brainfuck code to execute
· input_data (str): Input data for the program (default: "")
· memory_size (int): Size of the memory tape (default: 30000)

Returns: str - Output of the Brainfuck program

compile_to_python(brainfuck_code, memory_size=30000)

Convert Brainfuck code to Python code.

Parameters:

· brainfuck_code (str): Brainfuck code to convert
· memory_size (int): Size of the memory tape (default: 30000)

Returns: str - Generated Python code

BrainPy Class

BrainPy(memory_size=30000)

Main interpreter class.

Parameters:

· memory_size (int): Size of the memory tape

Methods

· compile(brainfuck_code): Convert Brainfuck to Python code
· execute(brainfuck_code, input_data=""): Execute via Python code generation
· execute_direct(brainfuck_code, input_data=""): Direct execution (more efficient)

Examples

Hello World

```python
import brainpy

hello_world_bf = """
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
"""

result = brainpy.execute(hello_world_bf)
print(result)  # Hello World!
```

Fibonacci Sequence

```python
from brainpy import BrainPy

fibonacci_bf = """
>++++++++++>+>+[
    [+++++[>++++++++<-]>.<++++++[>--------<-]+<<<]>.>>[
        [-]<[>+<-]>>[<<+>+>-]<[>+<-[>+<-[>+<-[>+<-[>+<-[>+<-
            [>+<-[>+<-[>+<-[>[-]>+>+<<<-[>+<-]]]]]]]]]]]
        >>>+
    ]<<<
]
"""

interpreter = BrainPy()
result = interpreter.execute_direct(fibonacci_bf)
print(result)  # 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
```

Rot13 Example

```python
import brainpy

rot13_bf = """
-,+[                         
    -[                       
        >>[>]+>+[<]<-        
    ]>>[<]<[                 
        >-[>>>]>>>>[-<+>]<[<+>-]<[<+>-]<[<+>-]<[<+>-]<[<+>-]
        <[<+>-]<[<+>-]<[<+>-]<[<+>-]<[<+>-]<[<+>-]<[<+>-]<<<
    ]<                        
]>>>[>]                      
+++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++
++++++++++.                  
"""

# Test with input
input_text = "hello"
result = brainpy.execute(rot13_bf, input_text)
print(f"ROT13 of '{input_text}': {result}")  # uryyb
```

Simple Calculator (Addition)

```python
import brainpy

# Adds two single-digit numbers (e.g., "3" and "4" becomes "7")
adder_bf = """
,>,>++++++[<-------->-]<<[->+<]>>++++++[<-------->-]<.
"""

result = brainpy.execute(adder_bf, "34")
print(f"3 + 4 = {result}")  # Output: 7
```

Brainfuck Language Reference

BrainPy supports the complete Brainfuck language:

Command Description Python Equivalent
> Move pointer right pointer = (pointer + 1) % memory_size
< Move pointer left pointer = (pointer - 1) % memory_size
+ Increment current cell memory[pointer] = (memory[pointer] + 1) % 256
- Decrement current cell memory[pointer] = (memory[pointer] - 1) % 256
. Output character from current cell output.append(chr(memory[pointer]))
, Input character to current cell memory[pointer] = ord(input_char) % 256
[ Start loop while current cell != 0 while memory[pointer] != 0:
] End loop (loop end)

Error Handling

BrainPy provides detailed error information:

```python
from brainpy import BrainPy, BrainPySyntaxError, BrainPyRuntimeError

interpreter = BrainPy()

try:
    result = interpreter.execute("+++[--->++<]>.>")  # Missing bracket
except BrainPySyntaxError as e:
    print(f"Syntax error: {e}")

try:
    result = interpreter.execute("+" * 1000000)  # Potential memory issues
except BrainPyRuntimeError as e:
    print(f"Runtime error: {e}")
```

Advanced Usage

Custom Memory Size

```python
from brainpy import BrainPy

# For memory-intensive programs
large_memory_interpreter = BrainPy(memory_size=1000000)

# For constrained environments
small_memory_interpreter = BrainPy(memory_size=1000)
```

Programmatic Code Generation

```python
from brainpy import BrainPy

interpreter = BrainPy()
brainfuck_code = "+++[>++<-]>."  # Multiply 3 by 2
python_code = interpreter.compile(brainfuck_code)

# Save the generated Python code
with open("generated_program.py", "w") as f:
    f.write(python_code)
```

Integration with Other Systems

```python
import brainpy
from brainpy import BrainPy

class BrainfuckRunner:
    def __init__(self):
        self.interpreter = BrainPy()
    
    def run_and_capture(self, code, input_data=""):
        """Run Brainfuck code and capture output"""
        return self.interpreter.execute_direct(code, input_data)
    
    def validate_code(self, code):
        """Validate Brainfuck code syntax"""
        try:
            self.interpreter.compile(code)
            return True
        except BrainPySyntaxError:
            return False

# Usage
runner = BrainfuckRunner()
if runner.validate_code("+++[->+<]"):
    result = runner.run_and_capture("+++[->+<]>.")
    print(f"Result: {result}")
```

Performance Considerations

BrainPy offers two execution methods:

1. execute_direct() - Faster, uses direct interpretation
2. execute() - Compiles to Python first, then executes (useful for code generation)

For most use cases, execute_direct() is recommended due to better performance.

```python
from brainpy import BrainPy
import time

interpreter = BrainPy()
code = "+++[>+++[>+++<-]<-]>>."  # 3 * 3 * 3 = 27

# Direct execution (faster)
start = time.time()
result1 = interpreter.execute_direct(code)
time_direct = time.time() - start

# Compilation + execution
start = time.time()
result2 = interpreter.execute(code)
time_compile = time.time() - start

print(f"Direct execution: {time_direct:.6f}s")
print(f"Compile + execute: {time_compile:.6f}s")
print(f"Results match: {result1 == result2}")
```

Testing

BrainPy includes comprehensive tests. To run them:

```bash
# Install test dependencies
pip install -e ".[dev]"

# Run all tests
pytest

# Run with coverage
pytest --cov=brainpy

# Run specific test categories
pytest tests/test_basic.py -v
pytest tests/test_edge_cases.py -v
```

Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add some amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request

Development Setup

```bash
# Clone the repository
git clone https://github.com/silentbyte69/brainpy.git
cd brainpy

# Install in development mode
pip install -e .

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black brainpy/ tests/

# Lint code
flake8 brainpy/ tests/
```

License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments

· Brainfuck language designed by Urban Müller
· Inspired by various Brainfuck implementations in different languages
· Thanks to all contributors and users of the library

Support

If you encounter any issues or have questions:

1. Check the documentation
2. Search existing issues
3. Create a new issue with a detailed description

Changelog

v0.1.0 (Initial Release)

· Basic Brainfuck to Python conversion
· Direct execution mode
· Command-line interface
· Comprehensive test suite
· PyPI packaging and distribution

---

BrainPy - Making Brainfuck accessible in Python!
