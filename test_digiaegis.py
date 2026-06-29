# test_digiaegis.py
"""
Tests for DigiAegis module.
"""

import unittest
from digiaegis import DigiAegis

class TestDigiAegis(unittest.TestCase):
    """Test cases for DigiAegis class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DigiAegis()
        self.assertIsInstance(instance, DigiAegis)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DigiAegis()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
