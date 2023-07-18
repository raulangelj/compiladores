from antlr4 import *
from termcolor import colored

class ErrorListener(object):
  def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
    print("Bad token at line:", line, ":", column)
    try:
      print(colored(f"Hint: {offendingSymbol.text}", 'red'))
    except Exception:
      print(colored(f"Hint: {msg}", 'red'))
    self.true = True
    # exit(1)

  def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
    pass

  def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
    pass

  def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
    pass