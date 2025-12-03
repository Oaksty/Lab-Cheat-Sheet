import bmi

def test_bmi_normal_weight():
    test = 0
    result = bmi.calculate_bmi(1.73,57)
    assert(result == test)

def test_bmi_over_weight():
    expected = 1
    result = bmi.calculate_bmi(1.73,87)
    assert(result == expected)

def test_bmi_under_weight():
    expected = -1
    result = bmi.calculate_bmi(1.73,37)
    assert(result == expected)
