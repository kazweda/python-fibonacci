import unittest
import fibonacci

class TestFibonacci(unittest.TestCase):

  cases = [[0,0],[1,1],[2,1],[3,2]]

  def test_fibo(self):
    for i in range(len(self.cases)):
      self.assertAlmostEqual(fibonacci.fibo(self.cases[i][0]), self.cases[i][1])

if __name__ == '__main__':
  unittest.main()
