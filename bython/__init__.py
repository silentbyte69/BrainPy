"""
Bython - Brainfuck to Python converter and executor

A library that converts Brainfuck code to Python and executes it.
"""

__version__ = "0.1.0"
__author__ = "Bython Developer"

from .core import Bython
from .exceptions import BythonError, BythonSyntaxError, BythonRuntimeError

__all__ = [
    "Bython",
    "BythonError", 
    "BythonSyntaxError",
    "BythonRuntimeError",
    "execute",
    "compile_to_python"
]

def execute(brainfuck_code, input_data="", memory_size=30000):
    """
    Execute Brainfuck code directly.
    
    Args:
        brainfuck_code (str): The Brainfuck code to execute
        input_data (str): Input data for the program
        memory_size (int): Size of the memory tape
        
    Returns:
        str: Output of the Brainfuck program
    """
    interpreter = Bython(memory_size=memory_size)
    return interpreter.execute(brainfuck_code, input_data)

def compile_to_python(brainfuck_code, memory_size=30000):
    """
    Convert Brainfuck code to Python code.
    
    Args:
        brainfuck_code (str): The Brainfuck code to convert
        memory_size (int): Size of the memory tape
        
    Returns:
        str: Generated Python code
    """
    interpreter = Bython(memory_size=memory_size)
    return interpreter.compile(brainfuck_code)
