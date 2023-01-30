class Book:
    
    def __init__(self, name, price, attributes):
        self.name = name
        self.price = price
        self.attributes = attributes
        
    def __str__(self):
        return f'{self.name} {self.attributes.author}' 
        
class BookAttributs:
    
    def __init__(self, type, author, genre):
        self.type = type
        self.author = author
        self.genre = genre
        
    def is_same(self, type, author, genre):
        return self.type is type and self.author is author and self.genre is genre
        
    def __str__(self):
        return f'{self.type} {self.author} {self.genre}'
        
class BookFlyweight:
    attributes = []
    
    def __init__(self, attributes = []):
        self.attributes = attributes
        
    def create_book(self, name, price, type, author, genre):
        attr = False
        for att in self.attributes:
            if att.is_same(type, author, genre):
                attr = att
                break
        if not attr:
            attr = BookAttributs(type, author, genre)
            self.attributes.append(attr)
        return Book(name, price, attr)
        
flyweight = BookFlyweight()

book1 = flyweight.create_book('name 1', 20, 'poem', 'author 1', 'horor')
book2 = flyweight.create_book('name 2', 30, 'novel', 'author 1', 'horor')
book3 = flyweight.create_book('name 3', 19.9, 'poem', 'author 1', 'horor')
book4 = flyweight.create_book('name 4', 49.99, 'novel', 'author 2', 'comedy')
book5 = flyweight.create_book('name 5', 50, 'poem', 'author 1', 'horor')

print(book1)
print(book2)
print(book3)
print(book4)
print(book5)

print(flyweight.attributes)
