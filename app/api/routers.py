from fastapi.routing import APIRouter
from app.services.ZooService import ZooService
from app.services.AnimalService import AnimalService
from fastapi.responses import JSONResponse
from fastapi import status

zoo_router = APIRouter()
animal_router = APIRouter()

@zoo_router.get("/", tags=["zoo"])
def get_zoo_list():
	zoo_list = [zoo for zoo in ZooService.get_zoo_list()]
	return JSONResponse(status_code=status.HTTP_200_OK, content={"data": zoo_list})

@zoo_router.get("/", tags=["zoo"])
def get_zoo_by_id(id: int):
	return JSONResponse(status_code=status.HTTP_200_OK, content={"data": ZooService.get_zoo_by_id(id)})

@animal_router.get("/zoo", tags=["animal"])
def get_animals_by_zoo_id(zoo_id: int):
	animal_list = [animal for animal in AnimalService.get_animals_by_zoo_id(zoo_id)]
	return JSONResponse(status_code=status.HTTP_200_OK, content={"data": animal_list})
	
@animal_router.get("/", tags=["animal"])
def get_animal_by_id(id: int):
	return JSONResponse(status_code=status.HTTP_200_OK, content={"data": AnimalService.get_animal_by_id(id)})