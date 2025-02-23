import strawberry
from app.graphql.query import Query

schema = strawberry.Schema(query=Query)