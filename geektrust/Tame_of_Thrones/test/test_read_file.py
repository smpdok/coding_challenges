import unittest
from unittest.mock import patch
from context import ReadFile
import os


class TestReadFile(unittest.TestCase):
    @patch('test_read_file.ReadFile.read_from_file_as_rows',
           autospec=True,
           spec_set=True)
    def test_read_from_file_as_rows(self, mocked_read_from_file_as_rows):
        with patch('test_read_file.os', autospec=True,
                   spec_set=True) as mocked_os:
            mocked_read_from_file_as_rows.return_value = [
                'AIR ROZO', 'LAND FAIJWJSOOFAMAU', 'ICE STHSTSTVSASOS'
            ]
            rows = mocked_read_from_file_as_rows('./input1.txt')
            assert mocked_read_from_file_as_rows is ReadFile.read_from_file_as_rows
            self.assertIsInstance(rows, list)
            assert rows == [
                'AIR ROZO', 'LAND FAIJWJSOOFAMAU', 'ICE STHSTSTVSASOS'
            ]
            mocked_read_from_file_as_rows.assert_called_once_with(
                './input1.txt')


if __name__ == '__main__':
    unittest.main()