"""
Denife a grammatical representation for a language
and an interpreter to interpret the gramar.

Client:
    Build the tree of expressions, the Interpret
    method of the top item in the tree is then called

Context (optional):
    Used to store any information that needs to be
    available to all expression objects

ExpressionBase:
    Base class defining the interpret method

TerminalExpression:
    Can be interpreted in a single object

NonTerminalExpression:
    Aggregates containing one or more further expressions,
    each of which may be terminal or no-terminal
"""


class ExpressionInterface:
    """
    Base class defining the interpret method
    """
    def interpret(self, text: str) -> bool:
        raise NotImplementedError()


class TerminalExpression(ExpressionInterface):
    """
    TerminalExpression
    
    Can be interpreted in a single object
    """
    def __init__(self, word: str) -> None:
        self._word = word

    def interpret(self, text: str) -> bool:
        if self._word in text:
            return True
        else:
            return False


class OrExpression(ExpressionInterface):
    """
    NonTerminalExpression

    Aggregates containing one or more further expressions,
    each of which may be terminal or no-terminal
    """
    def __init__(self, exp1: ExpressionInterface, exp2: ExpressionInterface) -> None:
        self._exp1 = exp1
        self._exp2 = exp2

    def interpret(self, text) -> bool:
        return self._exp1.interpret(text) or self._exp2.interpret(text)


class AndExpression(ExpressionInterface):
    """
    NonTerminalExpression

    Aggregates containing one or more further expressions,
    each of which may be terminal or no-terminal
    """
    def __init__(self, exp1: ExpressionInterface, exp2: ExpressionInterface) -> None:
        self._exp1 = exp1
        self._exp2 = exp2

    def interpret(self, text) -> bool:
        return self._exp1.interpret(text) and self._exp2.interpret(text)


jonh = TerminalExpression('Jonh')
henry = TerminalExpression('Henry')
mary = TerminalExpression('Mary')
sarah = TerminalExpression('Sarah')

# rules

rule1 = AndExpression(jonh, henry)
print(rule1.interpret('Jonh')) # should contains ("Jonh" and "Henry") -> False
print(rule1.interpret('Henry')) # should contains ("Jonh" and "Henry") -> False
print(rule1.interpret('Jonh + Henry')) # should contains ("Jonh" and "Henry") -> True

rule2 = OrExpression(mary, rule1)
print(rule2.interpret('Jonh')) # should contains ("Mary" or ("Jonh" and "Henry")) -> False
print(rule2.interpret('Henry')) # should contains ("Mary" or ("Jonh" and "Henry")) -> False
print(rule2.interpret('Mary')) # should contains ("Mary" or ("Jonh" and "Henry")) -> True
print(rule2.interpret('Jonh + Henry')) # should contains ("Mary" or ("Jonh" and "Henry")) -> True
print(rule2.interpret('Jonh + Henry + Mary')) # should contains ("Mary" or ("Jonh" and "Henry")) -> True

rule3 = AndExpression(sarah, rule2)
print(rule3.interpret('Mary')) # should contains (("Mary" or ("Jonh" and "Henry")) and "Sarah") -> False
print(rule3.interpret('Sarah')) # should contains (("Mary" or ("Jonh" and "Henry")) and "Sarah") -> False
print(rule3.interpret('Jonh + Henry')) # should contains (("Mary" or ("Jonh" and "Henry")) and "Sarah") -> False
print(rule3.interpret('Jonh + Henry + Mary')) # should contains (("Mary" or ("Jonh" and "Henry")) and "Sarah") -> False
print(rule3.interpret('Mary + Sarah')) # should contains (("Mary" or ("Jonh" and "Henry")) and "Sarah") -> True
print(rule3.interpret('Jonh + Henry + Sarah')) # should contains (("Mary" or ("Jonh" and "Henry")) and "Sarah") -> True

print(rule3.interpret('Mary + Jonh + Henry + Sarah')) # should contains (("Mary" or ("Jonh" and "Henry")) and "Sarah") -> True
