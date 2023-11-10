from os import  environ as env
from fastapi import APIRouter
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
API_KEYS = env.get("API_KEYS").split(",")


Average_router = APIRouter()



class Average(BaseModel):
    name: str
    Toefl: int
    rank: int
    Native: str | None = "Chinese"

name_list = [
            Average(name="j", Toefl=120, rank=1),
            Average(name="a", Toefl=119, rank=2, Native="English"),
            Average(name="b", Toefl=117, rank=3, Native="English"),
            Average(name="q", Toefl=116, rank=4),
            Average(name="y", Toefl=110, rank=5)
]

API_KEYS = ["060501", "060212"]

@Average_router.get("/")
async def get_all_names(api_key: str):
    if api_key in API_KEYS:
        res = []
        for last_name in name_list:
            res.append(last_name.name)
        return f"The Most unlikely to fail the class are : 1. {res[0]}, 2. {res[1]}, 3. {res[2]}, 4. {res[3]}, 5. {res[4]}"
    return {"msg": "You do not have permission to access this resource."}


@Average_router.post("/")
async def add_new_name(name: Average):
    name_list.append(name)
    return{"msg": "Name Added"}

@Average_router.get("/{student_name}")
async def get_position(student_name: str):
    return f"{student_name} seems to be failing the class"