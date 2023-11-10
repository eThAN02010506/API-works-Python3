from fastapi import APIRouter
from pydantic import BaseModel

cps_router = APIRouter()
API_KEYS = ["060501", "060212"]

class Cps(BaseModel):
    Participant: str
    chance_to_fail_the_class: str
    age: str


class_pass_chance = [
    {"Participant": "a", "chance_to_fail_the_class": 0.100, "age": 18},
    {"Participant": "b", "chance_to_fail_the_class": 0.110, "age": 17},
    {"Participant": "c", "chance_to_fail_the_class": 0.411, "age": 12},
    {"Participant": "d", "chance_to_fail_the_class": 0.541, "age": 124},
    {"Participant": "e", "chance_to_fail_the_class": 0.154, "age": 15},
    {"Participant": "f", "chance_to_fail_the_class": 0.415, "age": 16},
    {"Participant": "g", "chance_to_fail_the_class": 0.141, "age": 18},
    {"Participant": "h", "chance_to_fail_the_class": 0.114, "age": 13},
    {"Participant": "i", "chance_to_fail_the_class": 0.011, "age": 124},
    {"Participant": "j", "chance_to_fail_the_class": 0.001, "age": 15},
    {"Participant": "k", "chance_to_fail_the_class": 0.123, "age": 16},
    {"Participant": "l", "chance_to_fail_the_class": 0.200, "age": 12},
    {"Participant": "m", "chance_to_fail_the_class": 1.000, "age": 19},
    {"Participant": "o", "chance_to_fail_the_class": 1.000, "age": 18},
    {"Participant": "p", "chance_to_fail_the_class": 0.932, "age": 18},
    {"Participant": "q", "chance_to_fail_the_class": 0.211, "age": 18},
    {"Participant": "r", "chance_to_fail_the_class": 0.985, "age": 17},
    {"Participant": "y", "chance_to_fail_the_class": 0.222, "age": 17},
    {"Participant": "x", "chance_to_fail_the_class": 0.865, "age": 16},
    {"Participant": "z", "chance_to_fail_the_class": 1.000, "age": 19},

]


@cps_router.get("/class_pass_chance")
async def names(api_key: str):
    if api_key in API_KEYS:
        res = []
        for participant_names in class_pass_chance:
            res.append(participant_names['Participant'])
        return res
    return {"msg": "what are you doing here? You don't have permission"}


@cps_router.get("/class_pass_chance/{participant_name}/fail_chance")
async def get_chance(participant_name: str, api_key: str):
    print(api_key, participant_name)
    if api_key in API_KEYS:
        for name_list in class_pass_chance:
            print(participant_name.lower(), name_list["Participant"])
            if participant_name.lower() == name_list["Participant"]:
                return f"The participant {name_list['Participant']} has a fail chance of {name_list['chance to fail the class']}."
        return f"who are you looking for? Type again."
    return {"msg": "You don't have the right to access the information."}



@cps_router.get("/class_pass_chance/{participant_name}/age")
async def get_age(participant_name: str, api_key: str):
    print(api_key)
    if api_key in API_KEYS:
        for name_list in class_pass_chance:
            if participant_name.lower() == name_list["Participant"]:
                return f"The participant {name_list['Participant']} is {name_list['age']} years old."
        return f"who are you looking for? Type again."
    return {"msg": "You don't have the right to access the information."}


@cps_router.get("/class_pass_chance/get_key")
async def get_key():
    return f"api key are.... why do you think I would tell you?"

@cps_router.get("/class_pass_chance/info")
async def intro(api_key: str = None):
    if api_key in API_KEYS:
        return("Hello there! this is about the class fail chance in Gamedesign 3!")
    return f"nah man. You probably in the wrong place. Else, check the api_key!"


