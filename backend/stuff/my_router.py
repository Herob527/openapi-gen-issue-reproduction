
from fastapi import APIRouter

from stuff.schemas import DirectoryModel, FileModel


__all__ = ["my_router"]

my_router = APIRouter(
    tags=["Audio"],
    prefix="/audios",
    responses={404: {"description": "Not found"}},
)

@my_router.post("/", response_model=DirectoryModel)
def index():
    return DirectoryModel(dir_name="test", files=[FileModel(file_name="test.txt"), DirectoryModel(dir_name="nested")])
