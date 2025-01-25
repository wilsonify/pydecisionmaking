
from pydecisionmaking.p01c01_introduction.hello_world import squares, tab_separated_string

def test_squares_function():
    result = squares(range(11))  # Assuming squares function works with range objects
    assert result == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100], "The squares function did not return the expected results."

def test_tab_separated_string_function():
    result = tab_separated_string(squares(range(11)))
    assert result == "\t0\t1\t4\t9\t16\t25\t36\t49\t64\t81\t100", "The tab_separated_string function did not return the expected results."
