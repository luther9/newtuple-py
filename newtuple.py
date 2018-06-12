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

from functools import reduce

from compdescriptors import Abstract


def setItem(seq, key, value):
  if isinstance(key, int):
    return seq[:key] + (value,) + seq[key + 1:]
  try:
    rKey = range(key.start or 0, key.stop, key.step or 1)
  except TypeError:
    raise TypeError(
      f'Argument 2 must be an int, slice, or range, got {type(key)}',
    )# from None

  def replace(seq, index):
    return setItem(seq, index[1], value[index[0]])

  return (
    seq[:key.start] + value + seq[key.stop:] if rKey.step == 1
    else reduce(replace, ((i, j) for i, j in enumerate(rKey)), seq)
  )


class Sequence:
  __add__ = Abstract()
  __getitem__ = Abstract()


def _fillClass():
  for name in 'setItem',:
    setattr(Sequence, name, globals()[name])


_fillClass()


class Tuple(tuple, Sequence):
  """A subclass of tuple whose methods mimic that of lists."""
