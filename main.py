from fastapi import FastAPI
import random
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


#http://127.0.0.1:8000/teste1
@app.get("/teste1")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randit(0,1000)}
