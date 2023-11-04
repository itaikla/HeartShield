class SimpleWeight:
    def __init__(self, value):
        assert value in {True, False}
        self.value_ = value

    @classmethod
    def zero(cls):
        return cls(False)
