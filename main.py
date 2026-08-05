from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message":"hello Arjun"}


@app.get("/about")
def about():
    return{"message":"iam arjun rathwa"}