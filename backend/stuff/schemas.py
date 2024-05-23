
# Recursive schema
from typing import List, Union
from pydantic import BaseModel

class FileModel(BaseModel):
    file_name: str


class DirectoryModel(BaseModel):
    dir_name: str
    files: List[Union["FileModel", "DirectoryModel"]] = []


DirectoryModel.model_rebuild()
