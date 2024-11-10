# booklover.py

# IMPORT LIBRARIES
import pandas as pd


# CREATE BOOKLOVER CLASS
class BookLover:
    
    
    # INITIALIZE OBJECT
    def __init__(self, name, email, fav_genre, num_books=0, book_list=pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list


    # ADD BOOK TO BOOK LIST
    def add_book(self, book_name, rating):
        
        if self.book_list['book_name'].isin([book_name]).any():
            print(f"'{book_name}' ALREADY IN BOOK LIST! TRY ADDING ANOTHER BOOK.")
        else:
            new_book = pd.DataFrame({'book_name': [book_name],
                                     'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
            print(f"SUCCESS! '{book_name}' ADDED TO BOOK LIST.")
            
    
    # CHECK IF BOOK HAS ALREADY BEEN READ
    def has_read(self, book_name):
        
        return self.book_list['book_name'].isin([book_name]).any()
            
    
    # GET THE TOTAL NUMBER OF BOOKS READ
    def num_books_read(self):
        
        return self.num_books
        
    
    # GET FAVORITE BOOKS
    def fav_books(self):
        
        favorite_books = self.book_list[self.book_list['book_rating'] > 3]
        return favorite_books
            

if __name__ == '__main__':
    
    test_obj = BookLover(name='Han Solo', email='hsolo@gmail', fav_genre='scifi')
    test_obj.add_book('War of the Worlds', 4)
    print(test_obj.has_read('Fight Club'))
    print(test_obj.has_read('War of the Worlds'))
    test_obj.add_book('Dune', 5)
    test_obj.add_book('War of the Worlds', 4)
    print(test_obj.num_books_read())
    print(test_obj.fav_books())