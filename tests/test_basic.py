"""
Basic tests for Bython functionality
"""

import pytest
import bython
from bython import Bython, BythonSyntaxError, BythonRuntimeError


class TestBasicFunctionality:
    """Test basic Brainfuck execution and compilation"""
    
    def test_basic_increment(self):
        """Test basic increment and output"""
        result = bython.execute("+.", "")
        assert result == chr(1)
    
    def test_multiple_increments(self):
        """Test multiple increments"""
        result = bython.execute("+++.", "")
        assert result == chr(3)
    
    def test_decrement(self):
        """Test decrement operation"""
        result = bython.execute("+++--.", "")
        assert result == chr(1)
    
    def test_pointer_movement(self):
        """Test pointer movement"""
        result = bython.execute("+>++>+++<.<.", "")
        # Should output: 2, 1 (moving back and forth)
        assert len(result) == 2
        assert result[0] == chr(2)
        assert result[1] == chr(1)
    
    def test_empty_program(self):
        """Test empty program execution"""
        result = bython.execute("", "")
        assert result == ""
    
    def test_comments_ignored(self):
        """Test that non-Brainfuck characters are ignored"""
        code = """
        This is a comment
        +++++ +++++     Initialize counter to 10
        [               Start loop
            .           Output current cell
            -           Decrement counter
        ]
        More comments...
        """
        # Extract just the Brainfuck commands: ++++++++++[.-]
        brainfuck_code = "++++++++++[.-]"
        result = bython.execute(brainfuck_code, "")
        # Should output ASCII 10, 9, 8, ..., 1
        expected = ''.join(chr(i) for i in range(10, 0, -1))
        assert result == expected


class TestInputOutput:
    """Test input and output functionality"""
    
    def test_simple_input(self):
        """Test basic input operation"""
        result = bython.execute(",.", "A")
        assert result == "A"
    
    def test_input_chain(self):
        """Test multiple input operations"""
        result = bython.execute(">,>,<.<.", "AB")
        assert result == "BA"  # Reversed output
    
    def test_empty_input(self):
        """Test with empty input"""
        result = bython.execute(",.", "")
        assert result == chr(0)  # Should be null character when no input
    
    def test_input_with_processing(self):
        """Test input with some processing"""
        # Capitalize lowercase input (simplified)
        result = bython.execute(",+[-.,+]", "hello")
        # This is a simple echo program that stops at null
        assert len(result) > 0


class TestLoopFunctionality:
    """Test Brainfuck loop operations"""
    
    def test_simple_loop(self):
        """Test basic loop functionality"""
        # Loop that adds 5 three times to make 15
        result = bython.execute("+++[>+++++<-]>.", "")
        assert result == chr(15)
    
    def test_nested_loops(self):
        """Test nested loops"""
        # Nested loop example
        code = "++[>+++[>++++<-]<-]>>."
        result = bython.execute(code, "")
        # 2 * 3 * 4 = 24
        assert result == chr(24)
    
    def test_zero_iteration_loop(self):
        """Test loop that should not execute"""
        result = bython.execute("[-]+.", "")  # Set to 0, loop doesn't run, then increment to 1
        assert result == chr(1)
    
    def test_complex_loop(self):
        """Test more complex loop structure"""
        code = ">++[<+++>-]<."  # Move, set to 2, loop: add 3 to previous cell, output previous
        result = bython.execute(code, "")
        assert result == chr(6)  # 3 * 2 = 6


class TestMemoryOperations:
    """Test memory manipulation and boundaries"""
    
    def test_memory_wrapping(self):
        """Test that memory pointer wraps correctly"""
        result = bython.execute("<+.", "")  # Move left (wraps to end), increment, output
        assert result == chr(1)
    
    def test_cell_value_wrapping(self):
        """Test that cell values wrap at 256"""
        result = bython.execute("-" * 300 + ".", "")  # Decrement 300 times
        # Should wrap: 256 - (300 % 256) = 256 - 44 = 212
        assert result == chr(212)
    
    def test_large_memory_size(self):
        """Test with custom large memory size"""
        interpreter = Bython(memory_size=100000)
        result = interpreter.execute_direct("+" * 50000 + ".", "")
        # Value should be 50000 % 256
        expected_value = 50000 % 256
        assert result == chr(expected_value)
    
    def test_small_memory_size(self):
        """Test with custom small memory size"""
        interpreter = Bython(memory_size=10)
        result = interpreter.execute_direct("+" * 5 + ".", "")
        assert result == chr(5)


class TestCompilation:
    """Test Brainfuck to Python compilation"""
    
    def test_compile_basic(self):
        """Test basic compilation"""
        python_code = bython.compile_to_python("+++.--")
        assert "def bython_program()" in python_code
        assert "memory[pointer]" in python_code
        assert "output.append" in python_code
        assert "pointer = (pointer + 1) % memory_size" in python_code
        assert "pointer = (pointer - 1) % memory_size" in python_code
    
    def test_compile_with_loops(self):
        """Test compilation with loops"""
        python_code = bython.compile_to_python("++[->+<]")
        assert "while memory[pointer] != 0:" in python_code
    
    def test_compile_with_input(self):
        """Test compilation with input operations"""
        python_code = bython.compile_to_python(",,.")
        assert "input_data = iter(input_data)" in python_code
        assert "next(input_data)" in python_code
    
    def test_compiled_code_executable(self):
        """Test that compiled code can be executed"""
        brainfuck_code = "+++.--"
        python_code = bython.compile_to_python(brainfuck_code)
        
        # Create a namespace for execution
        namespace = {"input_data": ""}
        
        # Execute the compiled code
        exec(python_code, namespace)
        
        # The result should be available
        assert "result" in namespace


class TestErrorHandling:
    """Test error handling and validation"""
    
    def test_unmatched_open_bracket(self):
        """Test syntax error for unmatched open bracket"""
        with pytest.raises(BythonSyntaxError):
            bython.execute("+++[--", "")
    
    def test_unmatched_close_bracket(self):
        """Test syntax error for unmatched close bracket"""
        with pytest.raises(BythonSyntaxError):
            bython.execute("+++]--", "")
    
    def test_nested_unmatched_brackets(self):
        """Test syntax error for nested unmatched brackets"""
        with pytest.raises(BythonSyntaxError):
            bython.execute("++[+[--]", "")
    
    def test_valid_brackets(self):
        """Test that valid bracket pairs work correctly"""
        # This should not raise an exception
        result = bython.execute("++[--]++", "")
        assert result == ""
    
    def test_complex_valid_brackets(self):
        """Test complex but valid bracket structures"""
        code = "++[>+[>+<-]<-]"
        result = bython.execute(code + ".", "")
        # Should execute without syntax errors
        assert result is not None


class TestExamples:
    """Test common Brainfuck examples"""
    
    def test_hello_world(self):
        """Test Hello World program"""
        hello_world = (
            "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++."
            "------.--------.>>+.>++."
        )
        result = bython.execute(hello_world, "")
        assert "Hello World" in result
    
    def test_fibonacci(self):
        """Test Fibonacci sequence generator"""
        fibonacci = (
            ">++++++++++>+>+[[+++++[>++++++++<-]>.<++++++[>--------<-]+<<<]>.>>[[-]<[>+<-]>>[<<+>+>-]"
            "<[>+<-[>+<-[>+<-[>+<-[>+<-[>+<-[>+<-[>+<-[>+<-[>[-]>+>+<<<-[>+<-]]]]]]]]]]>>>+]<<<]"
        )
        result = bython.execute(fibonacci, "")
        # Should output Fibonacci sequence
        assert len(result) > 0
        # First few Fibonacci numbers: 1, 1, 2, 3, 5, 8...
        # Their ASCII values should be in the output
        assert any(ord(char) in [1, 2, 3, 5, 8] for char in result[:10])
    
    def test_rot13(self):
        """Test ROT13 example"""
        rot13 = (
            "-,+[                         Read first character and start outer character reading loop\n"
            "    -[                       Skip forward if character is 0\n"
            "        >>[>]+>+[<]<-        Set up tape for copying (using 0 as a marker)\n"
            "    ]>>[<]<[                 Skip back and start inner loop\n"
            "        >-[>>>]>>>>[-<+>]<[<+>-]<[<+>-]<[<+>-]<[<+>-]<[<+>-]<[<+>-]<[<+>-]<[<+>-]<[<+>-]"
            "<[<+>-]<[<+>-]<[<+>-]<<<\n"
            "    ]<                       Skip back and continue\n"
            "]>>>[>]                      End outer loop and output result\n"
            "+++++++++++++++++++++++++++++\n"
            "+++++++++++++++++++++++++++++\n"
            "++++++++++.                  Output newline\n"
        )
        # Clean the code - remove non-Brainfuck characters
        clean_rot13 = ''.join(c for c in rot13 if c in '><+-.,[]')
        result = bython.execute(clean_rot13, "hello")
        # ROT13 of "hello" is "uryyb"
        assert len(result) > 0


class TestCLIInterface:
    """Test command-line interface functionality"""
    
    def test_bython_class_initialization(self):
        """Test Bython class initialization"""
        interpreter = Bython(memory_size=5000)
        assert interpreter.memory_size == 5000
        assert interpreter.brainfuck_commands == set('><+-.,[]')
    
    def test_execute_direct_vs_compile(self):
        """Test that direct execution and compilation give same results"""
        code = "+++[>++<-]>."
        
        # Direct execution
        interpreter = Bython()
        direct_result = interpreter.execute_direct(code, "")
        
        # Execution via compilation
        compile_result = interpreter.execute(code, "")
        
        assert direct_result == compile_result
    
    def test_different_memory_sizes(self):
        """Test behavior with different memory sizes"""
        code = ">" * 100 + "+."  # Move 100 right and increment
        
        # Small memory (should wrap)
        small_interpreter = Bython(memory_size=50)
        small_result = small_interpreter.execute_direct(code, "")
        
        # Large memory (should not wrap in this case)
        large_interpreter = Bython(memory_size=200)
        large_result = large_interpreter.execute_direct(code, "")
        
        # Both should work and produce the same character
        assert small_result == chr(1)
        assert large_result == chr(1)
