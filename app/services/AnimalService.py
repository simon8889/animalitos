from app.models.animal import Animal
from app.models.animal import Zoo
from app.database import get_session
from typing import List
from sqlmodel import select
from fastapi import HTTPException, status
from strawberry.file_uploads import Upload
from app.services.ImageUploadService import ImageUploadService
import uuid

class AnimalService:

	@staticmethod
	def get_animals_by_zoo_id(id: int) -> List[Animal]:
		session = get_session()
		query = select(Animal).where(Animal.zoo_id == id)
		results = session.exec(query)
		if not results:
			raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Zoo not found")
		return results
	
	@staticmethod
	def get_animal_by_id(id: int) -> Animal:
		session = get_session()
		query = select(Animal).where(Animal.id == id)
		results = session.exec(query).first()
		if not results:
			raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Animal not found")
		return results
	
	@staticmethod
	def upload_image(file: Upload) -> str:
		try:
			file_extension = file.filename.split('.')[-1]
			unique_filename = f"{uuid.uuid4()}.{file_extension}"
			ImageUploadService().upload(file, unique_filename)
		except:
			raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
	
	@staticmethod
	def add_animal(animal: Animal, file: Upload) -> Animal:
		session = get_session()
		new_animal = animal
		if file:
			new_animal["image"] = AnimalService.upload_image(file)
		session.add(new_animal)
		session.commit()
		session.refresh(new_animal)
		return new_animal
	
	@staticmethod
	def delete_animal(id: int) -> bool:
		session = get_session()
		try:
			query = select(Animal).where(Animal.id == id)
			animal = session.exec(query).first()
			if not animal:
				raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Animal not found")
			session.delete(animal)
			session.commit()
			return True
		finally:
			session.close()
		
