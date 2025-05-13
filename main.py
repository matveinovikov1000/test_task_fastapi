from fastapi import FastAPI
import uvicorn

from routers.routers import router as add_routers

app = FastAPI()

app.include_router(add_routers)

if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8000)
