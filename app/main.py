from fastapi import FastAPI

app = FastAPI(title="Content Publishing API")


@app.get("/")
def home():
    return {"message": "Content Publishing API is running"}