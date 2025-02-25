import strawberry
from app.graphql.types import Zoo, Animal
from typing import List
from sqlmodel import select
from app.services.ZooService import ZooService
from app.services.AnimalService import AnimalService

@strawberry.type
class Query:
	
	@strawberry.field
	def health(self) -> str:
		return "running"

	get_zoo_list: List[Zoo] = strawberry.field(resolver=ZooService.get_zoo_list)
	get_zoo_by_id: Zoo = strawberry.field(resolver=ZooService.get_zoo_by_id)
	
	get_animals_by_zoo_id: List[Animal] = strawberry.field(resolver=AnimalService.get_animals_by_zoo_id)
	get_animal_by_id: Animal = strawberry.field(resolver=AnimalService.get_animal_by_id)