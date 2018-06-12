#!/usr/bin/env python3

import unittest

import newtuple


class TupleTest:

  def testSetItem(self):
    self.assertEqual(self.call('setItem', (0, 1, 2), 1, 666), (0, 666, 2))

  def testSetItemSlice(self):
    self.assertEqual(
      self.call('setItem', (0, 1, 2, 3), slice(1, 3), (10, 20, 100)),
      (0, 10, 20, 100, 3),
    )

  def testSetItemSliceStep(self):
    self.assertEqual(
      self.call('setItem', (0, 1, 2, 3, 4), slice(1, 5, 2), (10, 30)),
      (0, 10, 2, 30, 4),
    )

  def testDelItem(self):
    self.assertEqual(self.call('delItem', (0, 1, 2), 1), (0, 2))

  def testDelItemSlice(self):
    self.assertEqual(self.call('delItem', (0, 1, 2, 3), slice(1, 3)), (0, 3))

  def testDelItemSliceStep(self):
    self.assertEqual(
      self.call('delItem', (0, 1, 2, 3, 4), slice(1, 5, 2)), (0, 2, 4),
    )

  def testAppend(self):
    self.assertEqual(self.call('append', (0, 1), 55), (0, 1, 55))

  def testInsert(self):
    self.assertEqual(self.call('insert', (0, 1), 1, 55), (0, 55, 1))

  def testPop(self):
    self.assertEqual(self.call('pop', (0, 1, 2), 1), ((0, 2), 1))

  def testRemove(self):
    self.assertEqual(self.call('remove', (0, 100, 2, 100), 100), (0, 2, 100))


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

if __name__ == '__main__':
  unittest.main()
