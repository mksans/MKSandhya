import pytest
from app import add_numbers

def test_positive_numbers():
    """Test adding two positive integers."""
    assert add_numbers(5, 10) == 15.0

def test_negative_numbers():
    """Test adding negative numbers."""
    assert add_numbers(-1, -5) == -6.0

def test_decimal_numbers():
    """Test adding floating-point decimals."""
    assert add_numbers(1.5, 2.5) == 4.0

def test_string_inputs():
    """Test that function handles string digits correctly."""
    assert add_numbers("10", "20") == 30.0

def test_invalid_input_raises_error():
    """Test that invalid text inputs trigger a ValueError."""
    with pytest.raises(ValueError):
        add_numbers("apple", 5)