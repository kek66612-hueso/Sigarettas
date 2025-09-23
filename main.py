from database import DatabaseConfig, DatabaseConnection
from migrations import MigrationManager
from repository import WarehouseRepository
from service import WarehouseService
from fastapi import FastAPI, HTTPException
from storage import Warehouse

#Initialize
## DB config
db_config= DatabaseConfig(
    'storagesdb',
    'postgres',
    'postgres',
    '123Secret_a',
    5432
)
db_connection = DatabaseConnection(db_config)
## Migrations
migration_manager = MigrationManager(db_config)
migration_manager.create_tables()
# Repository and Service
repository = WarehouseRepository(db_connection)
service = WarehouseService(repository)

app = FastAPI(
    title="Storage API"
)

@app.get("/")
async def root():
    return {"message":"Hello from FastAPI"}

@app.get("/vegetables")
async def get_vegetables():
    try:
        return service.get_all()
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Ошибка при получении овощей: {str(e)}")

@app.post("/vegetables")
async def create_vegetables(flight_data: dict):
    try:
        #Validation
        required_fields = ["weight","box"]
        for field in required_fields:
            if field not in flight_data:
                raise HTTPException(status_code=400,detail=f"Отсутствует обязательное поле {field}")
        
        storage = Warehouse(
            weight=storage_data['weight'],
            box=storage_data['box']
        )

        created_storage = service.create_storage(storage)
        return created_storage

    except Exception as e:
        return HTTPException(status_code=500, detail=f"Ошибка при добавлении овощей: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0", port=8080)
