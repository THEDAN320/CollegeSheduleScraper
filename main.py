from fastapi import FastAPI

from routers import router

app = FastAPI(title="College Scraper")
app.include_router(router)
