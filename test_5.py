# Library concept


class Library:
    def __init__(self, books):
        self.books = books

    def borrow_books(self, books):
        if books > self.books:
            print("books are not availaible sorry..!")
        else:
            self.books -= books
            print(f"total books remains: {self.show_books()}")

    def return_books(self, books):
        self.books += books
        print(f"total books remains: {self.show_books()}")

    def show_books(self):
        return self.books


L = Library(10)
L.borrow_books(4)
print("--------------------------------------------------")
L.return_books(3)
print("--------------------------------------------------")
L.borrow_books(9)
