from lexer import tokenize, TokenType, token
from astree import Program, Stmt, Expr, BinaryExpr, Identifier, NumericLiteral

from errors import UnexpectedTokenError, ExpectationError

class Parser:
    def notEOF(self) -> bool:
        return self.tokens[0].token != TokenType.EOF
    
    def at(self):
        return token(self.tokens[0].token, self.tokens[0].value)

    def eat(self):
        tok = self.tokens.pop(0)
        prev = token(tok.token, tok.value)
        return prev

    def expect(self, type: TokenType, err: any):
        tok = self.tokens.pop(0)
        prev = token(tok.token, tok.value)
        if (not prev) or prev.token != type:
            raise ExpectationError(token, f'Parser Error:\n{err}')
        return prev

    def parse(self, src) -> Program:
        self.tokens = tokenize(src)
        program = Program("Program", [])
        while self.notEOF():
            program.body.append(self.parseStmt())
        return program
    
    def parseStmt(self) -> Stmt:
        # Just return parse expr for now
        return self.parseExpr()
    
    def parseExpr(self) -> Expr:
        # Just return parse addative expr for now
        return self.parseAdditiveExpr()
    
    def parseAdditiveExpr(self) -> Expr:
        left = self.parseMultiplicitaveExpr()
        while self.at().value == "+" or self.at().value == "-":
            operator = self.eat().value
            right = self.parseMultiplicitaveExpr()
            left = BinaryExpr("BinaryExpr", left, right, operator)
        return left
    
    def parseMultiplicitaveExpr(self) -> Expr:
        left = self.parsePrimaryExpr()
        while self.at().value == "/" or self.at().value == "*" or self.at().value == "%":
            operator = self.eat().value
            right = self.parsePrimaryExpr()
            left = BinaryExpr("BinaryExpr", left, right, operator)
        return left
    
    def parsePrimaryExpr(self) -> Expr:
        tk = self.at().token
        # Determine which token we are currently at and return literal value
        if tk == TokenType.Identifier:
            val = self.eat()
            return Identifier("Identifier", val.value)
        elif tk == TokenType.Number:
            val = self.eat()
            return NumericLiteral("NumericLiteral", eval(val.value))
        elif tk == TokenType.OpenParen:
            self.eat()
            value = self.parseExpr()  # Corrected function call
            self.expect(
                TokenType.CloseParen,
                "Unexpected token found inside parenthesized expression. Expected closing parenthesis."
            )
            return value
        else:
            raise UnexpectedTokenError(tk)

import json
from dataclasses import asdict

def ast_to_dict(node):
    if isinstance(node, list):  # Handle lists of nodes (e.g., Program body)
        return [ast_to_dict(n) for n in node]
    elif hasattr(node, '__dict__'):  # Convert dataclass objects to dictionaries
        node_dict = {key: ast_to_dict(value) for key, value in asdict(node).items()}
        node_dict['kind'] = node.kind  # Add kind explicitly if not already in __dict__
        return node_dict
    else:  # Handle primitive types (e.g., strings, numbers)
        return node

def prettyPrint(ast, indent=2):
    return json.dumps(ast_to_dict(ast), indent=indent)