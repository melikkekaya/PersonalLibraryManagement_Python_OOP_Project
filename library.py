from tabulate import tabulate

class Library():
    num_books = 0
    available_books = 0
    borrowed_books = 0
    
    book_list = []
    available_book_list = []
    borrowed_book_list = []
   
    
    def __init__(self, book_name, writer, situation="Available", location="Brussels"):
        self.book_name = book_name
        self.writer = writer
        self.situation = situation
        self.location = location
        Library.num_books += 1
        self.book_code = Library.num_books
        
        Library.book_list.append([self.book_code,self.book_name,self.writer,self.situation])
        if self.situation == "Available":
            Library.available_book_list.append([self.book_code,self.book_name,self.writer,self.situation])

    def display_booklist():
        print("---------------------------------------------------------")
        print(f"""Total number of books: {Library.num_books}\nAvailable books: \nBorrowed books: """)
        print("---------------------------------------------------------")
        df = Library.book_list
        col_names = ["Book Code", "Book Name", "Writer", "Situation"]
        print (tabulate(df, headers=col_names, tablefmt = "plain"))
        print("---------------------------------------------------------")

    @classmethod
    def new_book(cls,book_info_list):
        for book_info in book_info_list:
            book_name, writer = book_info[0], book_info[1]
            cls(book_name, writer)
    

book1 = Library("Gülün Adı", "Umberto Eco", "Borrowed")
book2 = Library("Hacı Murat", "Tolstoy")


Library.new_book([("İnsancıklar", "Dostoyevski"), ("Ölümcül Kimlikler", "Amin Maalouf")])

Library.display_booklist()
