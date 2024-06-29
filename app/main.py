from fastapi import FastAPI, APIRouter
from strawberry.fastapi import GraphQLRouter

from api.resolvers.todo import schema


app = FastAPI()


graphql_app: APIRouter = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
