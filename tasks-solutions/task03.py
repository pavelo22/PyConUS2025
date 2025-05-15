from task01 import Pittcoin


class OperationLogger:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'a')
        self.file.write('Start of operation\n')
        return self.file  # so the user can write to it

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.write('End of operation\n')
        self.file.close()
        # Do not suppress exceptions
        return False


def simple_context_manager_test():
    # arrange
    coin1 = Pittcoin(1, 1)
    coin2 = Pittcoin(2, 1)
    file_name = 'operations.txt'

    # act
    exception_raised = False
    try:
        with OperationLogger(file_name) as file:
            coin1.pc = 'abcd'
            file.write('\tAddition\n')
            coin3 = coin1 + coin2
    except TypeError:
        exception_raised = True

    # assert
    with open(file_name) as file:
        text = file.read()

    # assert
    assert 'Start of operation' in text
    assert 'Addition' in text
    assert 'End of operation' in text
    assert exception_raised


if __name__ == '__main__':
    simple_context_manager_test()
