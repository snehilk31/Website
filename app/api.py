from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def welcome():
  x={"message":"HELLO WORLD !!! Welcome to Okteto !!"}
  return x
