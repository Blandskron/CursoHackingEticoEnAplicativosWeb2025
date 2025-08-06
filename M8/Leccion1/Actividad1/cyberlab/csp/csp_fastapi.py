from fastapi import FastAPI, Request
from fastapi.responses import Response

app = FastAPI()

@app.middleware("http")
async def add_csp(request: Request, call_next):
    response: Response = await call_next(request)
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    return response

@app.get("/")
def root():
    return {"msg": "CSP aplicado"}
