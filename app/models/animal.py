from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from app.models.zoo import Zoo

class Animal(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    scientific_name: Optional[str] = Field(default=None, index=True)
    species: str = Field(index=True)
    age: Optional[int] = Field(default=None)
    weight_kg: Optional[float] = Field(default=None)
    habitat: Optional[str] = Field(default=None)
    diet: Optional[str] = Field(default=None)
    zoo_id: Optional[int] = Field(default=None, foreign_key="zoo.id")
    zoo: Optional[Zoo] = Relationship(back_populates="animals")