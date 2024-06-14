from orm.orm import ORM

class Book:
    orm = ORM('library.db')

    @classmethod
    def create(cls, title, author_id, category_id):
        cls.orm.execute('INSERT INTO books (title, author_id, category_id) VALUES (?, ?, ?)', (title, author_id, category_id))

    @classmethod
    def get_all(cls):
        return cls.orm.fetchall('SELECT * FROM books')

    @classmethod
    def update(cls, book_id, title, author_id, category_id):
        cls.orm.execute('UPDATE books SET title = ?, author_id = ?, category_id = ? WHERE id = ?', (title, author_id, category_id, book_id))

    @classmethod
    def delete(cls, book_id):
        cls.orm.execute('DELETE FROM books WHERE id = ?', (book_id,))
