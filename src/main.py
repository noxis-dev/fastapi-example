from fastapi import FastAPI

from .receipts.router import router

# from starlette.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(router)
