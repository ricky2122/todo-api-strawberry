from fastapi.testclient import TestClient


def test_get_todos(client: TestClient):
    query = """
    query {
        todos {
            id
            title
            description
            completed
        }
    }
    """
    response = client.post("/graphql", json={"query": query})

    assert response.status_code == 200

    data = response.json()

    assert "errors" not in data
    assert len(data["data"]["todos"]) == 2

    todos = data["data"]["todos"]
    assert todos[0]["id"] == 1
    assert todos[0]["title"] == "todo1"
    assert todos[0]["description"] == "test1"
    assert todos[0]["completed"] is False
    assert todos[1]["id"] == 2
    assert todos[1]["title"] == "todo2"
    assert todos[1]["description"] == "test2"
    assert todos[1]["completed"] is True


def test_get_todo(client: TestClient):
    id = 1
    query = f"""
    query {{
        todo(id: {id}) {{
            id
            title
            description
            completed
        }}
    }}
    """
    response = client.post("graphql", json={"query": query})
    assert response.status_code == 200
    data = response.json()
    assert "errors" not in data

    todo = data["data"]["todo"]
    assert todo["id"] == 1
    assert todo["title"] == "todo1"
    assert todo["description"] == "test1"
    assert todo["completed"] is False


def test_create_todo(client: TestClient):
    mutation = """
    mutation {
        createTodo(todo: {
            title: "todo1",
            description: "test1",
            completed: false,
        }) {
            id
            title
            description
            completed
            }
    }
    """
    response = client.post("graphql", json={"query": mutation})
    assert response.status_code == 200
    data = response.json()
    assert "errors" not in data

    todo = data["data"]["createTodo"]
    assert todo["id"] == 1
    assert todo["title"] == "todo1"
    assert todo["description"] == "test1"
    assert todo["completed"] is False


def test_update_todo(client: TestClient):
    id = 1
    mutation = f"""
    mutation {{
        updateTodo(id: {id}, todo: {{
            title: "todo1",
            description: "test1",
            completed: true
        }}) {{
            id
            title
            description
            completed
        }}
    }}
    """
    response = client.post("graphql", json={"query": mutation})
    assert response.status_code == 200
    data = response.json()
    assert "errors" not in data

    todo = data["data"]["updateTodo"]
    assert todo["id"] == 1
    assert todo["title"] == "todo1"
    assert todo["description"] == "test1"
    assert todo["completed"] is True


def test_delete_todo(client: TestClient):
    id = 1
    mutation = f"""
    mutation {{
        deleteTodo(id: {id})
    }}
    """
    response = client.post("/graphql", json={"query": mutation})
    assert response.status_code == 200
    data = response.json()
    assert "errors" not in data
    assert data["data"]["deleteTodo"] is True
