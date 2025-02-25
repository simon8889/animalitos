import strawberry
from strawberry.file_uploads import Upload
from starlette.datastructures import UploadFile
from app.graphql.query import Query
from app.graphql.mutation import Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)