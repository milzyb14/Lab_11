"""
Program: rotation_utils.py
Author: Gabriel Walters
Date: October 27, 2025
Purpose: A utility module to adjust degree rotations to a 0-359 degree range.
"""

def adjust_rotation(degrees: int | float) -> int | float:
    """
    Adjusts a degree rotation to be within the 0-359.99... degree range.
    
    For example, 460 becomes 100, and -100 becomes 260.
    
    Raises:
        TypeError: If the input is not a numeric value.
    """
    if not isinstance(degrees, (int, float)):
        raise TypeError("Input must be a numeric value.")
    
    # The modulo operator (%) correctly handles positive and negative
    # values to find the equivalent positive angle.
    return degrees % 360