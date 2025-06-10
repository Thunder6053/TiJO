import unittest
from unittest.mock import Mock
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from library import Library
from library_repository import LibraryRepository

class LibraryTestCase(unittest.TestCase):

    def test_borrow_book_success(self):
        mock_repo = Mock(spec=LibraryRepository)
        mock_repo.remove_book.return_value = True
        library = Library(mock_repo)

        result = library.borrow_book("Wiedźmin")

        self.assertTrue(result)
        mock_repo.remove_book.assert_called_once_with("Wiedźmin")

    def test_return_book(self):
        mock_repo = Mock(spec=LibraryRepository)
        library = Library(mock_repo)

        library.return_book("Wiedźmin", "Sapkowski", 1990)

        mock_repo.add_book.assert_called_once_with("Wiedźmin", "Sapkowski", 1990)

    def test_list_books(self):
        mock_repo = Mock(spec=LibraryRepository)
        mock_repo.get_all_books.return_value = [("Wiedźmin", "Sapkowski", 1990)]
        library = Library(mock_repo)

        result = library.list_books()

        self.assertEqual(result, [("Wiedźmin", "Sapkowski", 1990)])
        mock_repo.get_all_books.assert_called_once()


if __name__ == '__main__':
    unittest.main()