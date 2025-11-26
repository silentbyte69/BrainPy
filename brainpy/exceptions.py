class BrainPyError(Exception):
    """Base exception for BrainPy library"""
    pass

class BrainPySyntaxError(BrainPyError):
    """Raised when there's a syntax error in Brainfuck code"""
    pass

class BrainPyRuntimeError(BrainPyError):
    """Raised when there's a runtime error during execution"""
    pass
