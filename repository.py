from storage import Warehouse
from database import DatabaseConnection


class WarehouseRepository:
    '''Класс-репозиторий для доступа к БД'''

    def __init__(self,connection: DatabaseConnection):
        self.connection=connection

    def create_storage(self, storage:Warehouse):
        """Добавление овоща"""

        conn = self.connection.get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO warehouse
                        (plane,price)
                        VALUES (%s,%s)
            ''',(storage.box,storage.weight))
        conn.commit()

        cursor.close()
        conn.close()

        return storage
    
    def get_all(self):
        conn = self.connection.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM vegetables ORDER BY id")
        rows = cursor.fetchall()

        storage = []
        for row in rows:
            storage.append(storage(
                row[0],
                row[1],
                row[2]
            ))
              
        cursor.close()
        conn.close()
        return storage
        
    def get_by_id(self,storage_id:int):
        """Получить овощ по идентификатору"""
        conn = self.connection.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM vegetables WHERE id = %s",(storage_id,))
        row = cursor.fetchone()
        
        cursor.close()
        conn.close()

        if row:
            return Warehouse(
                row[0],
                row[1],
                row[2]
            )
        return None
    
    def update_storage(self, storage:Warehouse):
        """Изменить существующий овощ. 
            Если овоща не существует, ничего не делать."""
        conn = self.connection.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE vegetables
            SET price = %s, plane = %s
            WHERE id = %s
            ''',(storage.weight, storage.box, storage.id))
        
        result = cursor.fetchone()
        storage.id = result[0]
        conn.commit()

        cursor.close()
        conn.close()

        return storage
    
    def delete_storage(self,storage_id:int):
        """Удалить существующий овощ.
            Если овоща не существует, ничего не делать."""
        conn = self.connection.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM vegetables WHERE id = %s
            ''',(storage_id,))
        conn.commit()
        deleted = cursor.rowcount

        cursor.close()
        conn.close()

        return deleted >0
