#!/usr/bin/env python3

import unittest

import newtuple


class TupleTest:

  def testSetitem(self):
    self.assertEqual(self.lib.setItem((0, 1, 2), 1, 666), (0, 666, 2))


def makeTestCase(name, lib):
  return type(name, (unittest.TestCase, TupleTest), {'lib': lib})


ClassTest = makeTestCase('Classtest', newtuple.Tuple)
GenericTest = makeTestCase('GenericTest', newtuple)
