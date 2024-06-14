from orm.orm import ORM

class Category:
    orm = ORM('library.db')

    @classmethod
    def create(cls, name):
        cls.orm.execute('INSERT INTO categories (name) VALUES (?)', (name,))

    @classmethod
    def get_all(cls):
        return cls.orm.fetchall('SELECT * FROM categories')

    @classmethod
    def delete(cls, category_id):
        cls.orm.execute('DELETE FROM categories WHERE id = ?', (category_id,))
