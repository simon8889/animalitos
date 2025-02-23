import strawberry
from app.graphql.types import ZooType, AnimalType
from typing import List
from app.models.animal import Animal
from app.models.zoo import Zoo
from sqlmodel import select
from app.database import get_session
from fastapi import Depends

@strawberry.type
class Query:
	
	@strawberry.field
	def health(self) -> str:
		return "running"
	
	def getZooList(session = Depends(get_session)) -> List[ZooType]:
		statement = select(Zoo)
		results = session.exec(statement)
		return results
		