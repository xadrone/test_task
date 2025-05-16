from .figures.circle import Circle
from .figures.triangle import Triangle
from .figures.base import Shape

def create_shape(data: dict) -> Shape:
    if data["type"] == "circle":
        return Circle(data["radius"])
    elif data["type"] == "triangle":
        return Triangle(data["a"], data["b"], data["c"])
    else:
        raise ValueError("Unknown shape type")
