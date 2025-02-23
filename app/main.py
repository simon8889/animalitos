from fastapi import FastAPI, status
from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse
from app.database import init_db
from app.config import settings
from app.graphql.schema import schema
from strawberry.fastapi import GraphQLRouter

@asynccontextmanager
async def lifespan(app: FastAPI):
	init_db()
	yield
 
app: FastAPI = FastAPI(
	debug=settings.DEBUG,
	lifespan=lifespan
	)

graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
def health_check():
	return JSONResponse({"running": True}, status_code=status.HTTP_200_OK)