import strawberry 
from app.services.AnimalService import AnimalService
from app.services.ZooService import ZooService
from app.graphql.types import Zoo, Animal, ZooInput, AnimalInput
from app.models.animal import Animal as AnimalModel
from app.models.zoo import Zoo as ZooModel
from typing import Optional
from strawberry.file_uploads import Upload
from fastapi import HTTPException, status

@strawberry.type
class Mutation:
	
	@strawberry.mutation
	def add_zoo(self, zoo: ZooInput) -> Zoo:
		new_zoo: ZooModel = ZooModel(**zoo.__dict__)
		try:
			return ZooService.add_zoo(new_zoo)
		except:
			raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
	
	@strawberry.mutation
	def add_animal(self, animal: AnimalInput, file: Optional[Upload] = None) -> Animal:
		new_animal: AnimalModel = AnimalModel(**animal.__dict__)
		try:
			return AnimalService.add_animal(new_animal, file)
		except:
			raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
	
	delete_zoo: bool = strawberry.mutation(resolver=ZooService.delete_zoo)
	delete_animal: bool = strawberry.mutation(resolver=AnimalService.delete_animal)
	
		
	
		
	