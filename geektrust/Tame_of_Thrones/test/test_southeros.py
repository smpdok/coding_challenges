import unittest
from context import Southeros


class TestMain(unittest.TestCase):
    def setUp(self):
        self.allies_required = 3
        self.king1 = 'King Shan'
        self.king2 = 'Al Falcone'
        self.king3 = 'Captain Jack Sparrow'
        self.valid_message = [
            'LAND FAIJWJSOOFAMAU', 'ICE MAMMOTH THVAO', 'FIRE DRAGON JXGMUT',
            'AIR ZORRO', 'WATER OCTO VJAVWBZ PUS'
        ]
        self.invalid_message = [
            'AIR OWLAOWLBOWLC', 'LAND OFBBMUFDICCSO', 'ICE VTBTBHTBBBOBAB',
            'WATER SUMMER IS COMING'
        ]
        self.space_obj = Southeros(self.king1, self.valid_message,
                                   self.allies_required)
        self.air_obj = Southeros(self.king2, self.invalid_message,
                                 self.allies_required)
        self.water_obj = Southeros(self.king3, self.valid_message,
                                   self.allies_required)

    def test_space_send_ravens_with_valid_message(self):

        # Sending the ravens..
        self.space_obj.send_the_ravens()
        self.assertEqual(self.space_obj.get_allies(),
                         'SPACE LAND FIRE AIR WATER')

    def test_air_send_ravens_with_invalid_message(self):

        # Sending the ravens..
        self.air_obj.send_the_ravens()
        self.assertIsNone(self.air_obj.get_allies())

    def test_water_send_ravens_with_valid_message(self):

        # Sending the ravens..
        self.water_obj.send_the_ravens()
        self.assertEqual(self.water_obj.get_allies(), 'WATER LAND FIRE AIR')


if __name__ == '__main__':
    unittest.main()
