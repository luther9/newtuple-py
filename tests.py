#!/usr/bin/env python3

import unittest

import newtuple


class TupleTest:

  def _method(self, name):
    def f(tup, *args):
      return getattr(self.lib, name)(tup, *args)
    return f

  def testSetitem(self):
    self.assertEqual(self._method('setitem')((0, 1, 2), 1, 666), (0, 666, 2))


def makeTestCase(name, lib):
  return type(name, (unittest.TestCase, TupleTest), {'lib': lib})


ClassTest = makeTestCase('Classtest', newtuple.Tuple)
