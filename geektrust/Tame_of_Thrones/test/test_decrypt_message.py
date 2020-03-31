import unittest
from context import DecryptMessage


class TestDecryptMessage(unittest.TestCase):
    def setUp(self):
        self.msg1, self.animal1 = 'ROZO', 'OWL'
        self.decrypt_obj1 = DecryptMessage(self.msg1, self.animal1)
        self.msg2, self.animal2 = 'FAIJWJSOOFAMAU', 'PANDA'
        self.decrypt_obj2 = DecryptMessage(self.msg2, self.animal2)

    def test_decrypt_message1(self):
        msg1 = self.decrypt_obj1.alphabet_to_number()
        assert msg1 == [18, 15, 26, 15]
        msg1 = self.decrypt_obj1.decrypt()
        assert msg1 == [15, 12, 23, 12]
        msg1 = self.decrypt_obj1.negative_cases()
        assert msg1 == [15, 12, 23, 12]
        msg1 = self.decrypt_obj1.number_to_alphabet()
        assert msg1 == ['O', 'L', 'W', 'L']

    def test_decrypt_message2(self):
        msg2 = self.decrypt_obj2.alphabet_to_number()
        assert msg2 == [6, 1, 9, 10, 23, 10, 19, 15, 15, 6, 1, 13, 1, 21]
        msg2 = self.decrypt_obj2.decrypt()
        assert msg2 == [1, -4, 4, 5, 18, 5, 14, 10, 10, 1, -4, 8, -4, 16]
        msg2 = self.decrypt_obj2.negative_cases()
        assert msg2 == [1, 22, 4, 5, 18, 5, 14, 10, 10, 1, 22, 8, 22, 16]
        msg2 = self.decrypt_obj2.number_to_alphabet()
        assert msg2 == [
            'A', 'V', 'D', 'E', 'R', 'E', 'N', 'J', 'J', 'A', 'V', 'H', 'V',
            'P'
        ]


if __name__ == '__main__':
    unittest.main()