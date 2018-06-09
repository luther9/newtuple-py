class Tuple(tuple):
  """A subclass of tuple whose methods mimic that of lists.

  Method names are all lowercase to reflect the names of special methods.

  These methods return a modified version of self.
  """

  def setitem(self, key, value):
    return self[:key] + (value,) + self[key + 1:]
