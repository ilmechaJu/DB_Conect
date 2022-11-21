from fastapi import FastAPI
app = FastAPI()

from fastapi.responses import FileResponse

@app.get("/")
def 작명():
    return 'hello'