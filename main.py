from fastapi import FastAPI
app = FastAPI()

@app.get("/helloworld")
def read_root():
    return {"Hello": "World"}


@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": "deu certo"}

