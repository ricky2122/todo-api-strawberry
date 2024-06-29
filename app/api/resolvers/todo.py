from typing import Optional

import strawberry

from api.schemas.todo import TodoType, TodoInput, TodoUpdate


@strawberry.type
class Query:
    @strawberry.field
    def todos(self) -> list[TodoType]:
        return [
            TodoType(id=1, title="todo1", description="test1", completed=False),
            TodoType(id=2, title="todo2", description="test2", completed=True),
        ]

    @strawberry.field
    def todo(self, id: int) -> Optional[TodoType]:
        return TodoType(id=1, title="todo1", description="test1", completed=False)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_todo(self, todo: TodoInput) -> TodoType:
        completed = todo.completed if todo.completed is not None else True
        return TodoType(
            id=1, title=todo.title, description=todo.description, completed=completed
        )

    @strawberry.mutation
    def update_todo(self, id: int, todo: TodoUpdate) -> Optional[TodoType]:
        title = todo.title if todo.title else "todo1"
        description = todo.description if todo.description else "test1"
        completed = todo.completed if todo.completed is not None else True
        return TodoType(
            id=id, title=title, description=description, completed=completed
        )

    @strawberry.mutation
    def delete_todo(self, id: int) -> bool:
        return True


schema = strawberry.Schema(query=Query, mutation=Mutation)
