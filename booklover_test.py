# booklover_test.py

# IMPORT LIBRARIES
from booklover import BookLover
import unittest


# CREATE BOOKLOVERTESTSUITE CLASS
class BookLoverTestSuite(unittest.TestCase):
    
    
    def test_1_add_book(self):
        # add a book and test if it is in `book_list`.
        
        # set up test object
        test1_obj = BookLover('Mark Twain', 'mt@gmail', 'SciFi')
        book = 'The Hobbit'
        rating = 5
        test1_obj.add_book(book, rating)
        
        # create assert method
        self.assertTrue(test1_obj.book_list['book_name'].isin([book]).any())
    
    
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        
        # set up test object
        test2_obj = BookLover('Jane Austen', 'jane@gmail', 'History')
        book = 'Pride and Prejudice'
        rating = 3
        test2_obj.add_book(book, rating)
        test2_obj.add_book(book, rating)
        
        # create test variables
        expected_count = 1 
        book_count = int(test2_obj.book_list['book_name'].value_counts().get(book))
        
        # create assert method
        self.assertEqual(book_count, expected_count)
    
    
    def test_3_has_read(self):
        # pass a book in the list and test if the answer is `True`.
        
        # set up test object
        test3_obj = BookLover('Charles Dickens', 'chuck@gmail', 'Fantasy')
        book = 'A Tale of Two Cities'
        rating = 5
        test3_obj.add_book(book, rating)
        
        # create assert method
        self.assertTrue(test3_obj.has_read(book))
    
    
    def test_4_has_read(self):
        # pass a book NOT in the list and use `assert False` to test the answer is `True`.
        
        # set up test object
        test4_obj = BookLover('Stephen King', 'king@gmail', 'SciFi')
        book = 'The Shining'
        rating = 2 
        test4_obj.add_book(book, rating)
        
        # create test variables
        not_read = '1984'
        
        # create assert method
        self.assertFalse(test4_obj.has_read(not_read))
    
    
    def test_5_num_books_read(self):
        # add some books to the list, and test num_books matches expected.
        
        # set up test object
        test5_obj = BookLover('Frank Herbert', 'frank@gmail', 'SciFi')
        book1 = 'Foundation'
        rating1 = 4
        book2 = 'The Hitchhikers Guide to the Galaxy'
        rating2 = 3
        book3 = 'The Three-Body Problem'
        rating3 = 5
        test5_obj.add_book(book1, rating1)
        test5_obj.add_book(book2, rating2)
        test5_obj.add_book(book3, rating3)
        
        # create test variables
        expected_count = 3
        books_read = test5_obj.num_books_read()
        
        # create assert method
        self.assertEqual(books_read, expected_count)
        
    
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # test should check that the returned books have rating  > 3.
        
        # set up test object
        test6_obj = BookLover('James Joyce', 'jj@gmail', 'History')
        book1 = 'War and Peace'
        rating1 = 4
        book2 = 'The Great Gatsby'
        rating2 = 3
        book3 = 'The Old Man and the Sea'
        rating3 = 5
        test6_obj.add_book(book1, rating1)
        test6_obj.add_book(book2, rating2)
        test6_obj.add_book(book3, rating3)
        
        # create test variables
        expected_count = 2
        favorites_count = int(test6_obj.fav_books().shape[0])
        
        # create assert method
        self.assertEqual(favorites_count, expected_count)

    
if __name__ == "__main__":
    unittest.main(verbosity=2)
