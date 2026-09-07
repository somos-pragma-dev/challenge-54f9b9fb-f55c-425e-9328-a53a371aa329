import unittest
from unittest.mock import patch, mock_open
from src.word_counter import count_words

class TestWordCounter(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='Hello world\nThis is a test.')
    def test_count_words(self, mock_file):
        self.assertEqual(count_words('test_file.txt'), 6)

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_file_not_found(self, mock_file):
        self.assertEqual(count_words('non_existent_file.txt'), 0)

    @patch('builtins.open', side_effect=PermissionError)
    def test_permission_error(self, mock_file):
        self.assertEqual(count_words('restricted_file.txt'), 0)

if __name__ == '__main__':
    unittest.main()