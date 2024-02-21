import pytest
from extract_position import extract_position

def test_extract_position_update():
    # Test with a string containing 'update' and a position
    line = '|update| the positron location in the particle accelerator is x:21.432'
    result = extract_position(line)
    assert result == 21.432

def test_extract_position_error():
    # Test with a string containing 'error'
    line = '|error| numerical calculations could not converge.'
    with pytest.raises(ValueError):
        extract_position(line)

def test_extract_position_no_keyword_or_position():
    # Test with a string without 'update' or 'error' or 'x:'
    line = 'the positron location in the particle accelerator is 21.432'
    with pytest.raises(ValueError):
      extract_position(line)

def test_extract_position_no_keyword_but_has_position():
    # Test with a string without 'update' or 'error' but has 'x:'
    line = 'the positron location in the particle accelerator is x:21.432'
    result = extract_position(line)
    assert result == 21.432

def test_extract_position_empty_string():
    # Test with an empty string
    line = ''
    with pytest.raises(ValueError):
        extract_position(line)
