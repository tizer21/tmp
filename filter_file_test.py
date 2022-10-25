import unittest

from typing import List
from unittest.mock import mock_open, patch

from filter_file import filter_file


def execute_filter_file(file_content: str, words: List[str]) -> List[str]:
    with patch('builtins.open', mock_open(read_data=file_content)):
        return list(filter_file('test.txt', words))


class TestFilterFile(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(execute_filter_file('', []), [])

        self.assertEqual(execute_filter_file('', ['word']), [])
        self.assertEqual(execute_filter_file('word', []), [])

        self.assertEqual(execute_filter_file('word', ['word']), ['word'])
        self.assertEqual(execute_filter_file('abcd', ['word']), [])
        self.assertEqual(execute_filter_file('word', ['abcd']), [])
        self.assertEqual(execute_filter_file('drow', ['word']), [])
        self.assertEqual(execute_filter_file('word', ['drow']), [])

        self.assertEqual(execute_filter_file('word', ['wordword']), [])
        self.assertEqual(execute_filter_file('wordword', ['word']), [])

        self.assertEqual(execute_filter_file('word word', ['wordword']), [])
        self.assertEqual(execute_filter_file('word word', ['word']),
                                             ['word word'])

        self.assertEqual(execute_filter_file('word', ['word', 'word']),
                         ['word'])
        self.assertEqual(execute_filter_file('wordword',['word', 'word']), [])
        self.assertEqual(execute_filter_file('word word', ['word word']),
                         ['word word'])

        self.assertEqual(execute_filter_file('word', ['WORD']), ['word'])
        self.assertEqual(execute_filter_file('WORD', ['word']), ['WORD'])
        self.assertEqual(execute_filter_file('WORD', ['WORD']), ['WORD'])

        self.assertEqual(execute_filter_file('word', ['world']), [])
        self.assertEqual(execute_filter_file('WORD', ['world']), [])
        self.assertEqual(execute_filter_file('word', ['WORLD']), [])
        self.assertEqual(execute_filter_file('WORD', ['WORLD']), [])

        self.assertEqual(execute_filter_file('word', ['WoRd']), ['word'])
        self.assertEqual(execute_filter_file('WoRd', ['word']), ['WoRd'])
        self.assertEqual(execute_filter_file('WoRd', ['WoRd']), ['WoRd'])
        self.assertEqual(execute_filter_file('WoRd', ['WORD']), ['WoRd'])
        self.assertEqual(execute_filter_file('WORD', ['WoRd']), ['WORD'])

        self.assertEqual(execute_filter_file('word\nWORD\nWoRd\n', ['word']),
                         ['word\n', 'WORD\n', 'WoRd\n'])
        self.assertEqual(execute_filter_file('word\nWORD\nWoRd\n', ['WORD']),
                         ['word\n', 'WORD\n', 'WoRd\n'])
        self.assertEqual(execute_filter_file('word\nWORD\nWoRd\n', ['WoRd']),
                         ['word\n', 'WORD\n', 'WoRd\n'])
        self.assertEqual(execute_filter_file('word\nWORD\nWoRd\n', ['wOrD']),
                         ['word\n', 'WORD\n', 'WoRd\n'])

        self.assertEqual(execute_filter_file('word\nWORD\nWoRd\n', ['world']),
                         [''])
        self.assertEqual(execute_filter_file('world\nWORD\nWoRd\n', ['wOrD']),
                         ['word\n', 'WORD\n', 'WoRd\n'])
        self.assertEqual(execute_filter_file('word\nWORD\nWoRd\n', ['wOrD']),
                         ['word\n', 'WORD\n', 'WoRd\n'])

    def test_example(self):
        file_content = 'a Roza upala na lapu Azora'

        self.assertEqual(execute_filter_file(file_content, ['roza']),
                         [file_content])

        self.assertEqual(execute_filter_file(file_content, ['roz']), [])
        self.assertEqual(execute_filter_file(file_content, ['rozan']), [])

    def test_one_one(self):
        self.assertEqual(execute_filter_file('a B c', ['a']), ['a B c'])
        self.assertEqual(execute_filter_file('A b C', ['a']), ['A b C'])
        self.assertEqual(execute_filter_file('a B c', ['A']), ['a B c'])
        self.assertEqual(execute_filter_file('A b C', ['A']), ['A b C'])

    def test_multiple_one(self):
        file_content = 'a B c\n' + 'B C D\n' + 'c d E\n'

        self.assertEqual(execute_filter_file(file_content, ['a']), ['a B c\n'])
        self.assertEqual(execute_filter_file(file_content, ['b']),
                         ['a B c\n', 'B C D\n'])
        self.assertEqual(execute_filter_file(file_content, ['c']),
                         ['a B c\n', 'B C D\n', 'c d E\n'])
        self.assertEqual(execute_filter_file(file_content, ['d']),
                         ['B C D\n', 'c d E\n'])
        self.assertEqual(execute_filter_file(file_content, ['e']), ['c d E\n'])
        self.assertEqual(execute_filter_file(file_content, ['f']), [])

        self.assertEqual(execute_filter_file(file_content, ['A']), ['a B c\n'])
        self.assertEqual(execute_filter_file(file_content, ['B']),
                         ['a B c\n', 'B C D\n'])
        self.assertEqual(execute_filter_file(file_content, ['C']),
                         ['a B c\n', 'B C D\n', 'c d E\n'])
        self.assertEqual(execute_filter_file(file_content, ['D']),
                         ['B C D\n', 'c d E\n'])
        self.assertEqual(execute_filter_file(file_content, ['E']), ['c d E\n'])
        self.assertEqual(execute_filter_file(file_content, ['F']), [])

    def test_one_multiple(self):
        pass

    def test_multiple_multiple(self):
        pass


if __name__ == '__main__':
    unittest.main()
