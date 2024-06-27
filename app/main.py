from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from api.resolvers.todo import schema


app = FastAPI()


graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
