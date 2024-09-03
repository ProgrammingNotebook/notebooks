class IncorrectOperatorError(Exception):

    def __init__(self, message: str):
        super().__init__(message)


class InvalidEquationError(Exception):

    def __init__(self, message: str):
        super().__init__(message)
