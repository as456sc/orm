import sqlalchemy
from sqlalchemy.orm import sessionmaker



from models  import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = 'postgresql://postgres:86380029@localhost:5432/ORM_SQL-DB-Python_hw'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind = engine)
session = Session()




#for  i,o,p,t in  session.query(Book.title,Shop.name,Sale.price,Sale.date_sale).distinct():
 #  print(i,o,p,t)

def searching_publisher_name():
    query_join = session.query(Shop).join(Stock).join(Book).join(Publisher)
    name = input('Введите имя (name) издателя: ')
    query_result = query_join.filter(Publisher.name == name)
    for result in query_result.all():
        print(f'Издатель "{name}" найден в магазине "{result.name}" с идентификатором {result.id}')





if __name__ == '__main__':
    searching_publisher_name()
    
session.close()

