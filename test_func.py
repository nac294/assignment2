from main import *


###############################################################################################################
# Assert that this function returns 0 when ZeroDivisionError is thrown
def test_bmi_zero():
    assert get_bmi(0, 1) == 0

# Test a normal set of inputs to get_bmi()
def test_bmi_normal():
    assert get_bmi(63, 125) == 22.7

###############################################################################################################
# Test [-INF, 18.5)
def test_output_less_than():
    assert handle_output(0) == (0, "Invalid input")  # ON
    assert handle_output(0.1) == (0.1, "Underweight")  # OFF
    assert handle_output(9) == (9, "Underweight")  # INTERIOR
    assert handle_output(18.4) == (18.4, "Underweight")  # OFF
    assert handle_output(18.5) == (18.5, "Normal weight")  # ON

# Test [18.5, 25)
def test_output_level_1():
    assert handle_output(18.4) == (18.4, "Underweight")  # OFF
    assert handle_output(18.5) == (18.5, "Normal weight")  # ON
    assert handle_output(20) == (20, "Normal weight")  # INTERIOR
    assert handle_output(24.9) == (24.9, "Normal weight")  # ON
    assert handle_output(25) == (25, "Overweight")  # OFF

# Test [25, 30)
def test_output_level_2():
    assert handle_output(24.9) == (24.9, "Normal weight")  # OFF
    assert handle_output(25) == (25, "Overweight")  # ON
    assert handle_output(27) == (27, "Overweight")  # INTERIOR
    assert handle_output(29.9) == (29.9, "Overweight")  # ON
    assert handle_output(30) == (30, "Obese")  # OFF

# Test (30, +INF]
def test_output_greater_than():
    assert handle_output(29.9) == (29.9, "Overweight")  # OFF
    assert handle_output(30) == (30, "Obese")  # ON
    assert handle_output(31) == (31, "Obese")  # INTERIOR
