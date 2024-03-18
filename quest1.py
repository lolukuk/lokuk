from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Создание приложения FastAPI
app = FastAPI()

# Создание базовой модели SQLAlchemy
Base = declarative_base()

# Модель данных для контакта
class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Подключение к базе данных
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создание таблицы
Base.metadata.create_all(bind=engine)

# Модель данных Pydantic для валидации входных данных
class ContactCreate(BaseModel):
    name: str
    description: str

# Создание контакта
@app.post("/contacts/")
def create_contact(contact: ContactCreate):
    db = SessionLocal()
    db_contact = Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

# Получение списка контактов
@app.get("/contacts/")
def get_contacts():
    db = SessionLocal()
    return db.query(Contact).all()

# Получение контакта по id
@app.get("/contacts/{contact_id}")
def get_contact(contact_id: int):
    db = SessionLocal()
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

# Обновление контакта
@app.put("/contacts/{contact_id}")
def update_contact(contact_id: int, contact: ContactCreate):
    db = SessionLocal()
    db_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    for key, value in contact.dict().items():
        setattr(db_contact, key, value)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

# Удаление контакта
@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int):
    db = SessionLocal()
    db_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    db.delete(db_contact)
    db.commit()
    return {"message": "Contact deleted successfully"}

# Запуск приложения
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
