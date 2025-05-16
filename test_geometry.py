import pytest
from math import pi
from test_task.figures.circle import Circle
from test_task.figures.triangle import Triangle
from test_task.factory import create_shape

# ----- Circle Tests -----

def test_circle_area():
    c = Circle(2)
    assert pytest.approx(c.area()) == pi * 4

# ----- Triangle Tests -----

def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert pytest.approx(t.area()) == 6

def test_triangle_right_angled():
    t = Triangle(3, 4, 5)
    assert t.is_right_angled()

def test_triangle_not_right_angled():
    t = Triangle(3, 4, 6)
    assert not t.is_right_angled()

def test_invalid_triangle_raises():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)

# ----- Factory Tests -----

def test_factory_circle():
    shape = create_shape({"type": "circle", "radius": 1})
    assert pytest.approx(shape.area()) == pi

def test_factory_triangle():
    shape = create_shape({"type": "triangle", "a": 3, "b": 4, "c": 5})
    assert pytest.approx(shape.area()) == 6

def test_factory_invalid_type():
    with pytest.raises(ValueError):
        create_shape({"type": "square", "side": 4})
