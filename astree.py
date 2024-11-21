from dataclasses import dataclass
from typing import List, Literal

NodeType = Literal["Program",
                   "NumericLiteral",
                   "Identifier",
                   "BinaryExpr"]

@dataclass
class Stmt:
    kind: NodeType

@dataclass
class Program(Stmt):
    kind = "Program"
    body: List[Stmt]

@dataclass
class Expr(Stmt):
    pass

@dataclass
class BinaryExpr(Expr):
    kind = "BinaryExpr"
    left: Expr
    right: Expr
    operator: str

@dataclass
class Identifier(Expr):
    kind = "Identifier"
    symbol: str

@dataclass
class NumericLiteral(Expr):
    kind = "NumericLiteral"
    value: int