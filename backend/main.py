from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from stuff.my_router import my_router


origins = "https?://localhost:.+"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(my_router)


@app.post(
    "/",
)
def index():
    return "test"
