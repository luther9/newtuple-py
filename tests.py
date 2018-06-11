#!/usr/bin/env python3

import unittest

import newtuple


class TupleTest:

  def testSetitem(self):
    self.assertEqual(self.call('setItem', (0, 1, 2), 1, 666), (0, 666, 2))


def makeTestCase(name, call):
  return type(name, (unittest.TestCase, TupleTest), {'call': call})


@staticmethod
def callMethod(name, tup, *args):
  return getattr(newtuple.Tuple(tup), name)(*args)


@staticmethod
def callFunction(name, tup, *args):
  return getattr(newtuple, name)(tup, *args)


ClassTest = makeTestCase('Classtest', callMethod)
GenericTest = makeTestCase('GenericTest', callFunction)
