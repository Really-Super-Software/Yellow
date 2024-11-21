# int x = 67 + (3 * foo);
# TokenType.IntType int, TokenType.Identifier x, TokenType.Equals =, TokenType.Number 67, TokenType.Operator +, TokenType.OpenParen (
# TokenType.Number 3, TokenType.Operator *, TokenType.Identifier foo, TokenType.CloseParen ), TokenType.Semicolon ;

from dataclasses import dataclass
from typing import List, Dict

from tokens import TokenType
from errors import UnexpectedCharacterError

@dataclass
class token():
    token: TokenType
    value: str

RESERVED_KEYWORDS: Dict[str, TokenType]  = {
    "int": TokenType.IntType
}

def isalpha(chr: str) -> bool:
    return chr.lower() != chr.upper()

def isnum(chr: str) -> bool:
    return chr.isdigit()

def iswhitespace(chr: str) -> bool:
    return chr in [' ', '\n', '\t']

def tokenize(src: str) -> List[token]:
    tokens = []
    srcPtr = 0
    while srcPtr < len(src):
        chr = src[srcPtr]
        if chr == '(':
            tokens.append(token(TokenType.OpenParen, chr))
        elif chr == ')':
            tokens.append(token(TokenType.CloseParen, chr))
        elif chr == '+' or chr == '-' or chr == '*' or chr == '/' or chr == '%':
            tokens.append(token(TokenType.Operator, chr))
        elif chr == '=':
            tokens.append(token(TokenType.Equals, chr))
        elif chr == ';':
            tokens.append(token(TokenType.Semicolon, chr))
        elif iswhitespace(chr):
            pass
        else:
            # Number or Identifier
            if isalpha(chr):
                string = ''
                while isalpha(chr):
                    string += chr
                    srcPtr += 1
                    if srcPtr >= len(src):
                        break
                    chr = src[srcPtr]
                srcPtr -= 1
                if string in RESERVED_KEYWORDS:
                    keywordToken = RESERVED_KEYWORDS[string]
                    if keywordToken == TokenType.IntType:
                        tokens.append(token(TokenType.IntType, string))
                else:
                    tokens.append(token(TokenType.Identifier, string))
            elif isnum(chr):
                num = ''
                while isnum(chr):
                    num += chr
                    srcPtr += 1
                    if srcPtr >= len(src):
                        break
                    chr = src[srcPtr]
                srcPtr -= 1
                tokens.append(token(TokenType.Number, num))
            else:
                raise UnexpectedCharacterError(chr)
        srcPtr += 1
    tokens.append(token(TokenType.EOF, "EOF"))
    return tokens