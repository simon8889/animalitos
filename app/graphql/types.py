import strawberry
from typing import Optional, List

@strawberry.type
class AnimalType:
	id: Optional[int]
	name: str
	scientific_name: Optional[str]
	species: str
	age: Optional[int]
	weight_kg: Optional[float]
	habitat: Optional[str]
	diet: Optional[str]
	zoo: "ZooType"
	
@strawberry.type
class ZooType:
	id: Optional[int]
	name: str
	latitude: Optional[float]
	longitude: Optional[float]
	established_year: Optional[int]
	area_sq_km: Optional[float]
	num_animals: Optional[int]
	opening_hours: Optional[str]
	animals: List[AnimalType]
	