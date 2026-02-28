# pip install mysql-connector-python
import mysql.connector
class database:
    def __init__(self):
        try:
            self.mydbms=mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="12345" )
            print("Connection establised successfully")
            self.mycursor=self.mydbms.cursor()
        except Exception as e:
            print(f"error: {e}")
    def make_db(self):
        
        self.mycursor.execute("create database if not exists Personal_library_tracker")
        print("Data base created")
    def make_table(self):
        self.mycursor.execute("use Personal_library_tracker")
        self.mycursor.execute("create table if not exists Books(" \
        "id int primary key," \
        "Name varchar(50) not null," \
        "Author varchar(25)," \
        "Rating float(2)," \
        "Genre varchar(15)," \
        "publication varchar(30)," \
        "language varchar(15))")

        self.mycursor.execute("create table if not exists Students(" \
        "id int , " \
        "name varchar(20)," \
        "occupation varchar(30)," \
        "gender varchar(10))")

    def insert_into(self,**args):
        table = args['table']
        columns = ', '.join(list(args.keys())[1:])
        placeholders = ', '.join(['%s'] * (len(args) - 1))
        values = tuple(args.values())[1:]

        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

        self.mycursor.execute(query, values)
        self.mydbms.commit()
        self.mycursor.close()
        

        


    
    
