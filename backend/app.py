from fastapi import FastAPI
from .routes import auth, api, history

app = FastAPI(title="DataNirvana Backend")

app.include_router(auth.router, prefix="/auth")
app.include_router(api.router)
app.include_router(history.router, prefix="/history")

@app.get("/")
def root():
    return {"backend": "running"}