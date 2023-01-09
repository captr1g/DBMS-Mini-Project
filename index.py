from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def readdb():
    return {"msf": "hello"}
