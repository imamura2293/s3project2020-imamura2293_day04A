class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def area(self) -> int:
        return 0


def test_長方形の面積を計算できる():
    assert Rectangle(width=3, height=4).area() == 12
