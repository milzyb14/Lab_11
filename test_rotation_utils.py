# test_rotation_utils.py
# Myles Buchanan
# A pytest suite to verify the behavior of the adjust_rotation() function from rotation_utils.py.
# April 5th 2026

import pytest
from rotation_utils import adjust_rotation

def test_positive_within_range():
    """Input within 0-359 should be returned unchanged."""
    assert adjust_rotation(100) == 100

def test_positive_one_full_rotation():
    """Input of 460 (360 + 100) should wrap to 100."""
    assert adjust_rotation(460) == 100

def test_positive_two_full_rotations():
    """Input of 820 (720 + 100) should normalize to 100."""
    assert adjust_rotation(820) == 100

def test_negative_one_full_rotation():
    """Input of -100 should wrap to 260."""
    assert adjust_rotation(-100) == 260

def test_negative_two_full_rotations():
    """Input of -820 should normalize to 260."""
    assert adjust_rotation(-820) == 260

def test_non_numeric_raises_type_error():
    """Passing a string should raise a TypeError."""
    with pytest.raises(TypeError):
        adjust_rotation("ABC")
