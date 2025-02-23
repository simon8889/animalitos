from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship

class Zoo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    latitude: Optional[float] = Field(default=None)
    longitude: Optional[float] = Field(default=None)
    established_year: Optional[int] = Field(default=None)
    area_sq_km: Optional[float] = Field(default=None)
    num_animals: Optional[int] = Field(default=None)
    opening_hours: Optional[str] = Field(default="09:00-18:00")
    animals: List["Animal"] = Relationship(back_populates="zoo")
