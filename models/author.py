from orm.orm import ORM

class Author:
    orm = ORM('library.db')

    @classmethod
    def create(cls, name):
        cls.orm.execute('INSERT INTO authors (name) VALUES (?)', (name,))

    @classmethod
    def get_all(cls):
        return cls.orm.fetchall('SELECT * FROM authors')

    @classmethod
    def delete(cls, author_id):
        cls.orm.execute('DELETE FROM authors WHERE id = ?', (author_id,))
