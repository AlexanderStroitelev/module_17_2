from fastapi import FastAPI

from app.backend.db import Base , engine
from app.models import task , user

app = FastAPI()


@app.get("/")
async def wellcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router)
app.include_router(user.router)


Base.metadata.create_all(bind=engine)
print()

# информация о таблицах и их колонках
for table_name, table in Base.metadata.tables.items():
    print(f"Таблица: {table_name}")

    # их свойства
    print("Столбцы:")
    for column in table.columns:
        print(f"{column.name} - Тип: {column.type}")
        if column.primary_key:
            print(f"      Это первичный ключ")

    # связи (ForeignKey)
    print("Связи:")
    for fk in table.foreign_keys:
        print(f"      {fk.column} -> {fk.target_fullname}")

    print()
