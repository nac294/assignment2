from main import *


# Assert that this function returns a negative number when division by 0 occurs
# THIS TEST IS SUPPOSED TO FAIL
# THE CODE EXITS ON DIVISION BY ZERO
def test_bmi_zero():
    assert get_bmi(0, 1) == 0


def test_bmi_normal():
    assert get_bmi(63, 125) == 22.7

###############################################################################################################
# The lower bound only needs one test because it is negative 18.5 -> inf
def test_output_less_than():
    assert handle_output(-2) == "Invalid BMI"
    assert handle_output(0) == "Invalid BMI"
    assert handle_output(5) == "Underweight"

# These are the tests for weak N x 1
def test_output_level_1():
    assert handle_output(18.4) == "Underweight"  # OFF
    assert handle_output(18.5) == "Normal weight"  # ON
    assert handle_output(20) == "Normal weight"  # INTERIOR
    assert handle_output(24.9) == "Normal weight"  # ON
    assert handle_output(25) == "Overweight"  # OFF

def test_output_level_2():
    assert handle_output(24.9) == "Normal weight"  # OFF
    assert handle_output(25) == "Overweight"  # ON
    assert handle_output(27) == "Overweight"  # INTERIOR
    assert handle_output(29.9) == "Overweight"  # ON
    assert handle_output(30) == "Obese"  # OFF

def test_output_greater_than():
    assert handle_output(30.1) == "Obese"
    assert handle_output(31) == "Obese"
