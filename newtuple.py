# 2018 Luther Thompson
# This code is public domain under CC0. See the file COPYING for details.

"""List-like functions for making tuples from other tuples.

These functions can be inefficient, but are useful if you really need to do
list-like operations on tuples. I try to make the functions as generic as
possible, so they can take any tuple-like arguments that make sense, including
lists.

I can't decide whether to provide these functions stand-alone, in a class, or
both, so right now, I'm doing both.

Function names are the same as list method names converted to snakeCase. If the
list method is a special method, we remove the underscores.
"""

from functools import reduce

from compdescriptors import Abstract


def _sliceToRange(s):
  try:
    return range(s.start or 0, s.stop, s.step or 1)
  except TypeError:
    raise TypeError(
      f'Argument 2 must be an int, slice, or range, got {type(s)}',
    )


def setItem(seq, key, value):
  if isinstance(key, int):
    return seq[:key] + (value,) + seq[key + 1:]
  try:
    rKey = _sliceToRange(key)
  except TypeError as e:
    raise e from None

  def replace(seq, index):
    return setItem(seq, index[1], value[index[0]])

  return (
    seq[:key.start] + value + seq[key.stop:] if rKey.step == 1
    else reduce(replace, enumerate(rKey), seq)
  )


def delItem(seq, key):
  if isinstance(key, int):
    return seq[:key] + seq[key + 1:]
  try:
    rKey = _sliceToRange(key)
  except TypeError as e:
    raise e from None
  return (
    seq[:key.start] + seq[key.stop:] if rKey.step == 1
    else type(seq)(x for i, x in enumerate(seq) if i not in rKey)
  )


def append(seq, x):
  return seq + (x,)


def insert(seq, i, x):
  return seq[:i] + (x,) + seq[i:]


def pop(seq, i=-1):
  return delItem(seq, i), seq[i]


def remove(seq, x):
  try:
    return delItem(seq, seq.index(x))
  except ValueError as e:
    raise e from None


class Sequence:
  __add__ = Abstract()
  __getitem__ = Abstract()
  index = Abstract()


def _fillClass():
  for name in 'setItem', 'delItem', 'append', 'insert', 'pop', 'remove':
    setattr(Sequence, name, globals()[name])


_fillClass()


class Tuple(tuple, Sequence):
  """A subclass of tuple whose methods mimic that of lists."""
