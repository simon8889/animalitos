from app.models.zoo import Zoo
from app.models.animal import Animal
from typing import List
from app.database import get_session
from sqlmodel import select
from fastapi import HTTPException, status

class ZooService:
	
	@staticmethod
	def get_zoo_list() -> List[Zoo]:
		session = get_session()
		query = select(Zoo)
		results = session.exec(query)
		return results
	
	@staticmethod
	def get_zoo_by_id(id: int) -> Zoo:
		session = get_session()
		query = select(Zoo).where(Zoo.id == id)
		results = session.exec(query).first()
		if not results:
			raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Zoo not found")		
		return results
	
	@staticmethod
	def add_zoo(zoo: Zoo) -> Zoo:
		session = get_session()
		session.add(zoo)
		session.commit()
		session.refresh(zoo)
		return zoo
	
	@staticmethod
	def delete_zoo(id: int) -> bool:
		session = get_session()
		try:
			query = select(Zoo).where(Zoo.id == id)
			zoo_obj = session.exec(query).first()
			if not zoo_obj:
				raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Zoo not found")
			session.delete(zoo_obj)
			session.commit()
			return True
		finally:
			session.close()