from typing import List, Union
from pydantic import BaseModel

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Recursive schema
class FileModel(BaseModel):
    file_name: str


class DirectoryModel(BaseModel):
    dir_name: str
    files: List[Union["FileModel", "DirectoryModel"]] = []


DirectoryModel.model_rebuild()

origins = "https?://localhost:.+"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/", response_model=DirectoryModel)
def index():
    return DirectoryModel(dir_name="test", files=[FileModel(file_name="test.txt"), DirectoryModel(dir_name="nested")])
