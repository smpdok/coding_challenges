import unittest
from context import Ally


class TestAlly(unittest.TestCase):
    def setUp(self):
        self.msg1, self.animal1 = ['O', 'L', 'W', 'L'], 'OWL'
        self.ally1 = Ally(self.msg1, self.animal1)
        self.msg2, self.animal2 = ['A', 'L', 'W', 'L'], 'OWL'
        self.ally2 = Ally(self.msg2, self.animal2)

    def test_ally_check(self):
        result1 = self.ally1.ally_check()
        assert result1 == True
        result2 = self.ally2.ally_check()
        assert result2 == False


if __name__ == '__main__':
    unittest.main()