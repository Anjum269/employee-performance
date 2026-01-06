from employee_rating import calculate_rating

def test_outstanding():
    assert calculate_rating(95) == "S"

def test_excellent():
    assert calculate_rating(85) == "A"

def test_good():
    assert calculate_rating(70) == "B"

def test_average():
    assert calculate_rating(55) == "C"

def test_poor():
    assert calculate_rating(30) == "F"
