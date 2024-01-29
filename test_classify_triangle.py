def classify_triangle(a,b,c):
    if a+b > c and b+c > a and a+c > b:
        if a == b and a == c:
            return "Equilateral"
        elif a != b and a != c and b != c:
            if a**2 + b**2 == c**2:
                return "Right Scalene"
            return "Scalene"
        else:
            if round(a**2) + round(b**2) == round(c**2):
                return "Right Isosceles"
            return "Isosceles"
    else:
        return "Invalid Input"
    
def test_equilateral():
    assert classify_triangle(1, 1, 1) == "Equilateral"
    assert classify_triangle(2, 2, 2) == "Equilateral"
    assert classify_triangle(3, 3, 3) == "Equilateral"
def test_scalene():
        assert classify_triangle(2, 4, 5) == "Scalene"
        assert classify_triangle(4, 11, 8) == "Scalene"
        assert classify_triangle(15, 11, 8) == "Scalene"

def test_isocelse():
        assert classify_triangle(1, 3, 3) == "Isosceles"
        assert classify_triangle(6, 1, 6) == "Isosceles"
        assert classify_triangle(8, 8, 1) == "Isosceles"

def test_right():
       assert classify_triangle(3, 4, 5) == "Right Scalene"
       assert classify_triangle(1, 1, 2**0.5) == "Right Isosceles"

def test_invalid():
       assert classify_triangle(1, 1, 0) == "Invalid Input"
       assert classify_triangle(-3, 4, 5) == "Invalid Input"
       assert classify_triangle(1, 0, 3) == "Invalid Input"
