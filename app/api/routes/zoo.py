from fastapi.routing import APIRouter
from app.services.ZooService import ZooService
from fastapi.responses import JSONResponse
from fastapi import status

zoo_router = APIRouter()

@zoo_router.get("/list/", tags=["zoo"])
def get_zoo_list():
	zoo_list = [zoo.model_dump() for zoo in ZooService.get_zoo_list()]
	return JSONResponse(status_code=status.HTTP_200_OK, content={"data": zoo_list})

@zoo_router.get("/", tags=["zoo"])
def get_zoo_by_id(id: int):
	return JSONResponse(status_code=status.HTTP_200_OK, content={"data": ZooService.get_zoo_by_id(id).model_dump()})

