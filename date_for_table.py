from models  import create_tables, Publisher, Book, Shop, Stock, Sale
import sqlalchemy
from sqlalchemy.orm import sessionmaker


DSN = 'postgresql://postgres:86380029@localhost:5432/ORM_SQL-DB-Python_hw'
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind = engine)
session = Session()


publisher_1 = Publisher(name = "O\u2019Reilly")
publisher_2 = Publisher(name = "Pearson")
publisher_3 = Publisher(name = "Microsoft Press")
publisher_4 = Publisher(name = "No starch press")

session.add_all([publisher_1, publisher_2, publisher_3, publisher_4])
session.commit()


book_1 = Book(title = "Programming Python, 4th Edition", id_publisher = 1)
book_2 = Book(title = "Learning Python, 4th Edition", id_publisher = 1)
book_3 = Book(title = "Natural Language Processing with Python", id_publisher = 1)
book_4 = Book(title = "Hacking: The Art of Exploitation", id_publisher = 4)
book_5 = Book(title = "Modern Operating Systems", id_publisher = 2)
book_6 = Book(title = "Code Complete: Second Edition", id_publisher = 3)

session.add_all([book_1, book_2, book_3, book_4, book_5, book_6])
session.commit()

shop_1 = Shop(name = "Labirint")
shop_2 = Shop(name = "OZON")
shop_3 = Shop(name = "Amazon")

session.add_all([shop_1, shop_2, shop_3,])
session.commit()

stock_1 = Stock(id_book = 1, id_shop = 1, count = 34)
stock_2 = Stock(id_book = 2, id_shop = 1, count = 30)
stock_3 = Stock(id_book = 3, id_shop = 1, count = 0)
stock_4 = Stock(id_book = 5, id_shop = 2, count = 40)
stock_5 = Stock(id_book = 6, id_shop = 2, count = 50)
stock_6 = Stock(id_book = 4, id_shop = 3, count = 10)
stock_7 = Stock(id_book = 6, id_shop = 3, count = 10)
stock_8 = Stock(id_book = 1, id_shop = 2, count = 10)
stock_9 = Stock(id_book = 1, id_shop = 3, count = 10)

session.add_all([stock_1, stock_2, stock_3, stock_4, stock_5, stock_6, stock_7, stock_8, stock_9])
session.commit()

sale_1 = Sale(price = 50.05, date_sale = "2018-10-25T09:45:24.552Z",id_stock = 1, count = 16 )
sale_2 = Sale(price = 50.05, date_sale = "2018-10-25T09:51:04.113Z",id_stock = 3, count = 10)
sale_3 = Sale(price = 10.50, date_sale = "2018-10-25T09:52:22.194Z",id_stock = 6, count = 9 )
sale_4 = Sale(price = 16.00, date_sale = "2018-10-25T10:59:56.230Z",id_stock = 5, count = 5 )
sale_5 = Sale(price = 16.00, date_sale = "2018-10-25T10:59:56.230Z",id_stock = 9, count = 5 )
sale_6 = Sale(price = 16.00, date_sale = "2018-10-25T10:59:56.230Z",id_stock = 4, count = 1 )

session.add_all([sale_1, sale_2, sale_3, sale_4, sale_5, sale_6])
session.commit()

session.close()