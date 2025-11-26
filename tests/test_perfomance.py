"""
Performance tests for BrainPy
"""

import time
import brainpy
from brainpy import BrainPy


class TestPerformance:
    """Performance and stress tests"""
    
    def test_simple_performance(self):
        """Test performance of simple programs"""
        start_time = time.time()
        
        # Simple but moderately complex program
        code = "+++[>+++[>+++<-]<-]>>."  # 3 * 3 * 3 = 27
        result = brainpy.execute(code, "")
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        assert result == chr(27)
        # Should execute quickly (under 1 second)
        assert execution_time < 1.0
    
    def test_large_loop_performance(self):
        """Test performance with large loops"""
        interpreter = BrainPy()
        
        # Program with many iterations but simple operations
        code = ">" + "+" * 100 + "[<+>-]<."  # Move 100 to next cell, add it to first cell
        start_time = time.time()
        result = interpreter.execute_direct(code, "")
        end_time = time.time()
        
        assert result == chr(100)
        assert (end_time - start_time) < 2.0  # Should be reasonably fast
    
    def test_memory_usage(self):
        """Test that memory usage doesn't explode"""
        # Program that uses much of the memory tape
        code = ">" * 10000 + "+."  # Move far right and increment
        result = brainpy.execute(code, "")
        assert result == chr(1)
