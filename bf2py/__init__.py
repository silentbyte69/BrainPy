"""
bf2py - Brainfuck to Python converter and executor
"""

__version__ = "0.1.0"
__author__ = "Dmitry Seksov"

from .core import BF2Py
from .exceptions import BF2PyError, BF2PySyntaxError, BF2PyRuntimeError

__all__ = [
    "BF2Py",
    "BF2PyError", 
    "BF2PySyntaxError",
    "BF2PyRuntimeError",
    "execute",
    "compile_to_python"
]

def execute(brainfuck_code, input_data="", memory_size=30000):
    """Execute Brainfuck code directly."""
    interpreter = BF2Py(memory_size=memory_size)
    return interpreter.execute(brainfuck_code, input_data)

def compile_to_python(brainfuck_code, memory_size=30000):
    """Convert Brainfuck code to Python code."""
    interpreter = BF2Py(memory_size=memory_size)
    return interpreter.compile(brainfuck_code)
