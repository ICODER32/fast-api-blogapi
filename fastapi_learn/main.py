from fastapi import FastAPI


app=FastAPI()


@app.get("/")
def index():
    return "hello"


@app.get("/about")
def about():
    return {'data':{'about page':'about page'}}