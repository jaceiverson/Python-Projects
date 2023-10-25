from fastapi import APIRouter, Depends
from pydantic import BaseModel

from core.auth import get_api_key, set_scope


# define our payload models
class Person(BaseModel):
    name: str
    age: int


# define our router
router = APIRouter()


@router.post("/person")
@set_scope(permissions=["test"], model=Person)
def person_object_endpoint(
    payload: Person,
    api_key: str = Depends(get_api_key),
):
    name = payload.name.upper()
    return {
        "success": f"{name} noted! Nothing special has happened, this is just a test endpoint."
    }
