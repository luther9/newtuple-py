"""List-like functions for making tuples from other tuples.

These functions can be inefficient, but are useful if you really need to do
list-like operations on tuples. I try to make the functions as generic as
possible, so they can take any tuple-like arguments that make sense, including
lists.

I can't decide whether to provide these functions stand-alone, in a class, or
both, so right now, I'm doing both.

Function names are the same as list method names converted to snakeCase. If the
list method is a special method, we remove the underscores.

All functions require tuple-like arguments to support slicing and addition and
return a tuple, usually slightly modified from the first argument.
"""

from compdescriptors import Abstract


def setItem(seq, key, value):
  return seq[:key] + (value,) + seq[key + 1:]


class Sequence:
  __add__ = Abstract()
  __getitem__ = Abstract()


def _fillClass():
  for name in 'setItem',:
    setattr(Sequence, name, globals()[name])


_fillClass()


class Tuple(tuple, Sequence):
  """A subclass of tuple whose methods mimic that of lists."""
