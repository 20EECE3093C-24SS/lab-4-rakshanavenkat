import pytest
from course_grader import convert_to_letter_grade

# TODO-1: Add test_exact_grade_boundaries() function
@pytest.mark.parametrize("score, expected_grade", [
    (0, 'F'),
    (59, 'F'),
    (60, 'D'),
    (69, 'D'),
    (70, 'C'),
    (79, 'C'),
    (80, 'B'),
    (89, 'B'),
    (90, 'A'),
    (100, 'A'),
])
def test_exact_boundaries(score, expected_grade):
    assert convert_to_letter_grade(score) == expected_grade

# TODO-2: Add test_invalid_numerical_score() function
def test_invalid_numerical_score():
    with pytest.raises(ValueError) as e:
        convert_to_letter_grade(-5)
    assert str(e.value) == "Score must be between 0 and 100."

    with pytest.raises(ValueError) as e:
        convert_to_letter_grade(105)
    assert str(e.value) == "Score must be between 0 and 100."

# TODO-3: Add test_non_numeric_input() function
@pytest.mark.parametrize("invalid_input", ["abc", [1, 2, 3], None])
def test_non_numeric_type(invalid_input):
    with pytest.raises(TypeError) as e:
        convert_to_letter_grade(invalid_input)
    assert str(e.value) == "Score must be a numeric value."
