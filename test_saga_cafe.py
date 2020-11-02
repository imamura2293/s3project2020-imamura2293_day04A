class SagaCafe:
    def __init__(self, name: str, size: str):
        self.name = name
        self.size = size

        def price(self) -> int:
            price = 100

            if self.size == "L":
                price += 30

            if self.name == "アイスコーヒー":
                price += 20

            return price


def test_ホットコーヒーのRサイズは100円():
    assert SagaCafe(name="ホットコーヒー", size="R").price() == 100


def test_ホットコーヒーのLサイズは100円():
    assert SagaCafe(name="ホットコーヒー", size="L").price() == 130


def test_アイスコーヒーのRサイズは120円():
    assert SagaCafe(name="アイスコーヒー", size="R").price() == 120


def test_アイスコーヒーのRサイズは150円():
    assert SagaCafe(name="アイスコーヒー", size="L").price() == 150