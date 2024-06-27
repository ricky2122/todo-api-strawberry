from typing import Optional

import strawberry


@strawberry.type
class TodoType:
    id: int
    title: str
    description: str
    completed: bool


@strawberry.input
class TodoInput:
    title: str
    description: str
    completed: Optional[bool] = False


@strawberry.input
class TodoUpdate:
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
