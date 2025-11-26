# BrainPy

[![PyPI version](https://img.shields.io/pypi/v/brainpy.svg)](https://pypi.org/project/brainpy/)

BrainPy is a powerful Python library that converts Brainfuck code to Python and executes it seamlessly.

## Installation

```bash
pip install brainpy
```

# Quick Start

```python
import brainpy

# Execute Brainfuck code directly
result = brainpy.execute("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.")
print(result)  # Output: "Hello World!\n"

# Convert Brainfuck to Python code
python_code = brainpy.compile_to_python("+++>++<[->+<]>.")
print(python_code)
```

Command Line Usage

```bash
# Execute a Brainfuck file
brainpy hello_world.bf

# Execute Brainfuck code from string  
brainpy -c "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."

# Compile to Python without executing
brainpy --compile-only program.bf
```

# License

MIT License
