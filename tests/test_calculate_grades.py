import pytest
import math
from unittest.mock import patch
from calculate_grades import *

# needs to run with ```pytest -s tests/test_calculate_grades.py``` in terminal to avoid `OSError: pytest: reading from stdin while output is captured`

@patch('builtins.input', side_effect=['90', '85', '95', '88', '92'])
def test_read_input(mock_input):
    assert read_input() == [90, 85, 95, 88, 92]

def test_calculate_stat():
    grade_list = [90, 85, 95, 88, 92]
    mean, sd = calculate_stat(grade_list)
    assert mean == 90.0
    assert math.isclose(sd, 3.406, abs_tol=1e-3)

def test_print_stat(capsys):
    mean = 90.0
    sd = 3.632
    print_stat(mean, sd)
    captured = capsys.readouterr()
    assert '****** Grade Statistics ******' in captured.out
    assert "The grades's mean is: 90.0" in captured.out
    assert 'The population standard deviation of grades is:  3.632' in captured.out
    assert '****** END ******' in captured.out

@patch('builtins.input', side_effect=['90', '85', '95', '88', '92'])
def test_display_grade_stat(mock_input, capsys):
    display_grade_stat()
    captured = capsys.readouterr()
    assert '****** Grade Statistics ******' in captured.out
    assert "The grades's mean is: 90.0" in captured.out
    assert 'The population standard deviation of grades is:  3.406' in captured.out
    assert '****** END ******' in captured.out