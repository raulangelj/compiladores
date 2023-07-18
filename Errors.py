from antlr4 import *
from termcolor import colored

class ErrorListener(object):
  def __init__(self) -> None:
    self.true = False

  def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
    print(colored(f"Bad token at line: {line} : {column}", 'red'))
    print(colored(f"Hint: {msg}", 'red'))
    self.true = True
    # exit(1)

  def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
    pass

  def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
    pass

  def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
    pass