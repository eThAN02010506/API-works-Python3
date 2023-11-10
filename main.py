from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from router import average, cps

app = FastAPI()

app.include_router(cps.cps_router, prefix="/class_fail_chance")

app.include_router(average.Average_router, prefix="/average")

app.mount("/static", StaticFiles(directory="static"))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
