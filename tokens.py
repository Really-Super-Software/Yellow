from enum import Enum

class TokenType(Enum):
    # Literal types
    Number = "Number"
    Identifier = "Identifier"

    # Runtime types
    IntType = "IntType"

    # Single character types
    Operator = "Operator"      # + - * / %
    Equals = "Equals"          # =
    OpenParen = "OpenParen"    # (
    CloseParen = "CloseParen"  # )
    Semicolon = "Semicolon"    # ;
    
    # Extremely special types
    EOF = "EOF"