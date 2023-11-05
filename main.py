class SimpleWeight:
    def __init__(self, value):
        assert value in {True, False}
        self.value_ = value

    @classmethod
    def zero(cls):
        return cls(False)

    def toggle(self):
        self.value_ = not self.value_

    def copy(self):
        return SimpleWeight(self.value_)

    def __eq__(self, other):
        if isinstance(other, SimpleWeight):
            return self.value_ == other.value_
        return False
