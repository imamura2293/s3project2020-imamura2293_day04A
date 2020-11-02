import math


class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def area(self) -> int:
        return self.width * self.height

    def perimeter(self) -> int:
        return 2 * (self.width + self.height)

    def diagonal(self) -> float:
        return math.sqrt(self.width ** 2 + self.height ** 2)


def test_長方形の面積を計算できる():
    assert Rectangle(width=3, height=4).area() == 12


def test_長方形の周の長さを計算できる():
    assert Rectangle(width=3, height=4).perimeter() = 14


def test_長方形の対角線の長さを計算できる_整数となる場合():
    assert Rectangle(width=3, height=4).diagonal() == 5


def test_長方形の対角線の長さを計算できる_少数となる場合():
    assert Rectangle(width=1, height=2).diagonal() == 2.23
