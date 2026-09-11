def calculate_grade(marks):
    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def test_grade():
    marks = [85, 78, 92, 88, 75]
    assert calculate_grade(marks) == "A"
