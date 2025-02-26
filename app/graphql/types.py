import strawberry
from typing import Optional, List

@strawberry.type
class Animal:
	id: Optional[int]
	name: str
	scientific_name: Optional[str]
	species: str
	age: Optional[int]
	weight_kg: Optional[float]
	habitat: Optional[str]
	diet: Optional[str]
	image: Optional[str]
	zoo: "Zoo"
	
@strawberry.type
class Zoo:
	id: Optional[int]
	name: str
	latitude: Optional[float]
	longitude: Optional[float]
	established_year: Optional[int]
	area_sq_km: Optional[float]
	num_animals: Optional[int]
	opening_hours: Optional[str]
	animals: List[Animal]

@strawberry.input
class AnimalInput:
    name: str
    scientific_name: Optional[str] = None
    species: str
    age: Optional[int] = None
    weight_kg: Optional[float] = None
    habitat: Optional[str] = None
    diet: Optional[str] = None
    zoo_id: int

@strawberry.input
class ZooInput:
    name: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    established_year: Optional[int] = None
    area_sq_km: Optional[float] = None
    num_animals: Optional[int] = None
    opening_hours: Optional[str] = None
	