from fastapi import FastAPI, status
from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse
from app.database import init_db
from app.config import settings
from app.graphql.schema import schema
from app.api.routers import zoo_router, animal_router
from strawberry.fastapi import GraphQLRouter
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
	init_db()
	yield
 
app: FastAPI = FastAPI(
	debug=settings.DEBUG,
	lifespan=lifespan
	)

origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization", "Content-Type"],
    expose_headers=["Content-Disposition"], 
)

graphql_app = GraphQLRouter(schema, multipart_uploads_enabled=True)

app.include_router(graphql_app, prefix="/graphql")
app.include_router(zoo_router, prefix="/zoo")
app.include_router(animal_router, prefix="/animal")

@app.get("/")
def health_check():
	return JSONResponse({"running": True}, status_code=status.HTTP_200_OK)