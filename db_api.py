import mysql.connector as connector


class DBHelper:
    def __init__(self) -> None:
        self.conn = connector.connect(
            host="localhost",
            user="root",
            port="3306",
            password="",
            database="python_mysql",
        )
        query = '''
            create table if not exists users (
                user_id int primary key,
                full_name varchar(50),
                phone_number varchar(13)
            )
        '''
        cur = self.conn.cursor()
        cur.execute(query)

    def create(self, id: int, full_name: str, phone_number: str):
        query = f'''
            insert into users(user_id, full_name, phone_number)
            values({id}, "{full_name}", "{phone_number}");
        '''
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()

    def fetch_all(self):
        query = '''
            select * from users;
        '''
        cur = self.conn.cursor()
        cur.execute(query)
        return cur

    def fetch(self, id):
        query = f'''
            select * from users where user_id = {id};
        '''
        cur = self.conn.cursor()
        cur.execute(query)
        for row in cur:
            return row

    def update(self, id, new_full_name, new_phone_number):
        query = f'''
            update users
            set full_name = "{new_full_name}", phone_number = "{new_phone_number}"
            where user_id = {id};
        '''
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()

    def delete(self, id: int):
        query = f'''
            delete from users where user_id = {id};
        '''
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
