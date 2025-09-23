from repository import WarehouseRepository
from storage import Warehouse

class WarehouseService:
    def __init__(self,repository:WarehouseRepository):
        self.repository = repository

    def create_storage(self, storage:Warehouse):
        """Добавление овоща"""
        return self.repository.create_storage(storage)
    
    def get_all(self):
        '''Получить все полёты'''
        return self.repository.get_all()
        
    def get_by_id(self,storage_id:int):
        '''Получить полёт по id'''
        return self.repository.get_by_id(storage_id)
    
    def update_storage(self, storage:Warehouse):
        """Изменить существующий рейс. 
            Если рейса не существует, ничего не делать."""
        return self.repository.update_storage(storage)
    
    def delete_storage(self,storage_id:int):
        """Удалить существующий рейс.
            Если рейса не существует, ничего не делать."""
        return self.repository.delete_storage(storage_id)
