from tokens import TokenType

class YellowException(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)

class UnexpectedCharacterError(YellowException):
    def __init__(self, char: str):
        self.char = char
        super().__init__(f'Unexpected character found in source: {char}')

class UnexpectedTokenError(YellowException):
    def __init__(self, token: TokenType):
        self.token = token
        super().__init__(f'Unexpected token found in token list: {token}')

class ExpectationError(YellowException):
    def __init__(self, token: TokenType, err: str):
        self.token = token
        self.err = err
        super()._init__(f'{err} Instead got {token}')