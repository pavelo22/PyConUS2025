import time


class Pittcoin:
    def __init__(self, pc=0, pd=0):
        self.pc = pc
        self.pd = pd
        self.created = time.time()

    def __add__(self, other):
        if isinstance(other, Pittcoin):
            pc = self.pc + other.pc
            pd = self.pd + other.pd

            if pd >= 60:
                pc += pd // 60
                pd = pd % 60
            return Pittcoin(pc, pd)

        raise NotImplemented

    def __str__(self):
        return f'{self.pc} Pittcoin, {self.pd} Pittdust'

    def __repr__(self):
        return f'{self.pc} PC, {self.pd} PD; created: {self.created}'

    def __eq__(self, other):
        if isinstance(other, Pittcoin):
            return self.pc == other.pc and self.pd == other.pd
        return False

    def __lt__(self, other):
        if isinstance(other, Pittcoin):
            this_object = self.pc * 60 + self.pd
            other_object = other.pc * 60 + other.pd
            return this_object < other_object


def simple_test_addition_representation():
    # arrange
    coin1 = Pittcoin(1, 10)
    coin2 = Pittcoin(3, 55)

    # act
    coin3 = coin1 + coin2

    # assert
    assert coin3 == Pittcoin(5, 5)
    assert str(coin3) == str(Pittcoin(5, 5))


def simple_test_addition():
    # arrange
    coin1 = Pittcoin(3, 55)
    coin2 = Pittcoin(-2, 0)

    # act & assert
    assert coin1 + coin2 == Pittcoin(1, 55)


def simple_test_comparison():
    # arrange
    coin1 = Pittcoin(1, 10)
    coin2 = Pittcoin(1, 20)

    # act & assert
    assert coin1 < coin2


if __name__ == '__main__':
    simple_test_addition_representation()
    simple_test_addition()
    simple_test_comparison()
