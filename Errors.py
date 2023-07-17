from antlr4 import *

class ErrorListener(object):
  def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
    print("Bad token at line:", line, ":", column)
    try:
      print(f"Hint: {offendingSymbol.text}")
    except:
      print(f"Hint: {msg}")
    exit(1)

  def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
    pass

  def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
    pass

  def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
    pass