class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._is_borrowed = False
        self.history = []

    @property
    def is_borrowed(self):
        return self._is_borrowed

    def borrow(self):
        if self._is_borrowed:
            return False
        self._is_borrowed = True
        self.history.append("borrow")
        return True

    def return_book(self):
        if not self._is_borrowed:
            return False
        self._is_borrowed = False
        self.history.append("return")
        return True

    def describe(self):
        return f"{self.title} — {self.author}"


a = Book("Python cơ bản", "Linh")
b = Book("Git thực hành", "Hà")
print(a.describe())
print(b.describe())

print(a.borrow())       
print(a.borrow())       
print(b.is_borrowed)   
print(a.return_book()) 
print(a.is_borrowed) 
print(a.return_book())  

print(a.history)       
print(b.history)        