import unittest
from context import geektrust


class TestMain(unittest.TestCase):
    def setUp(self):
        self.ally_list = ['SPACE']
        self.rows1 = ['AIR ROZO', 'LAND FAIJWJSOOFAMAU', 'ICE STHSTSTVSASOS']
        self.rows2 = [
            'AIR OWLAOWLBOWLC', 'LAND OFBBMUFDICCSO', 'ICE VTBTBHTBBBOBAB',
            'WATER SUMMER IS COMING'
        ]
        self.rows3 = [
            'LAND PANDAUFSI', 'ICE MAMMOTH THVAO', 'FIRE DRAGON JXGMUT',
            'AIR ZORRO', 'WATER OCTO VJAVWBZ PUS'
        ]

    def test_parse_message1(self):
        allies1 = geektrust.parse_message(self.rows1, self.ally_list)
        self.assertIsInstance(allies1, list)
        assert allies1 == ['SPACE', 'AIR', 'LAND', 'ICE']

    def test_parse_message2(self):
        allies2 = geektrust.parse_message(self.rows2, self.ally_list)
        self.assertIsInstance(allies2, list)
        assert allies2 == ['SPACE', 'LAND', 'ICE']

    def test_parse_message3(self):
        allies3 = geektrust.parse_message(self.rows3, self.ally_list)
        self.assertIsInstance(allies3, list)
        assert allies3 == ['SPACE', 'FIRE', 'AIR', 'WATER']


if __name__ == '__main__':
    unittest.main()
