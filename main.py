class Library:
  def __init__(self):
      self.file = open("books.txt", "a+")

  def __del__(self):
      self.file.close()

  def list_books(self):
      self.file.seek(0)
      books = self.file.readlines()
      if not books:
          print("No books available.")
          return
      print("List of Books:")
      for book in books:
          book_info = book.strip().split(',')
          print(f"Title: {book_info[0]}, Author: {book_info[1]}")

  def add_book(self):
      title = input("Enter the title of the book: ")
      author = input("Enter the author of the book: ")
      release_year = input("Enter the release year of the book: ")
      num_pages = input("Enter the number of pages of the book: ")
      book_info = f"{title},{author},{release_year},{num_pages}\n"
      self.file.write(book_info)
      print("Book added successfully.")

  def remove_book(self):
      title = input("Enter the title of the book to remove: ")
      self.file.seek(0)
      books = self.file.readlines()
      found = False
      for book in books:
          if title in book:
              books.remove(book)
              found = True
              break
      if not found:
          print("Book not found.")
          return
      self.file.seek(0)
      self.file.truncate()
      self.file.writelines(books)
      print("Book removed successfully.")

# Creating Library object
lib = Library()

# Adding 20 books from world classics
world_classics = [
  ("To Kill a Mockingbird", "Harper Lee", "1960", "281"),
  ("1984", "George Orwell", "1949", "328"),
  ("Pride and Prejudice", "Jane Austen", "1813", "279"),
  ("The Great Gatsby", "F. Scott Fitzgerald", "1925", "180"),
  ("Moby Dick", "Herman Melville", "1851", "704"),
  ("The Catcher in the Rye", "J.D. Salinger", "1951", "224"),
  ("War and Peace", "Leo Tolstoy", "1869", "1225"),
  ("Crime and Punishment", "Fyodor Dostoevsky", "1866", "671"),
  ("The Odyssey", "Homer", "8th century BC", "296"),
  ("The Picture of Dorian Gray", "Oscar Wilde", "1890", "254"),
  ("Jane Eyre", "Charlotte Bronte", "1847", "532"),
  ("Wuthering Heights", "Emily Bronte", "1847", "342"),
  ("Don Quixote", "Miguel de Cervantes", "1605", "863"),
  ("Frankenstein", "Mary Shelley", "1818", "280"),
  ("The Adventures of Huckleberry Finn", "Mark Twain", "1884", "366"),
  ("Alice's Adventures in Wonderland", "Lewis Carroll", "1865", "200"),
  ("Les Misérables", "Victor Hugo", "1862", "1463"),
  ("Gulliver's Travels", "Jonathan Swift", "1726", "311"),
  ("Dracula", "Bram Stoker", "1897", "418"),
  ("The Three Musketeers", "Alexandre Dumas", "1844", "704")
]

for book in world_classics:
  lib.file.write(','.join(book) + '\n')

# Main menu loop
while True:
  print("\n*** MENU ***")
  print("1) List Books")
  print("2) Add Book")
  print("3) Remove Book")
  print("4) Exit")
  choice = input("Enter your choice: ")

  if choice == "1":
      lib.list_books()
  elif choice == "2":
      lib.add_book()
  elif choice == "3":
      lib.remove_book()
  elif choice == "4":
      break
  else:
      print("Invalid choice. Please try again.")
