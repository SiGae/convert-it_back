from typing import Optional
from fastapi import FastAPI, Request
from typing import List
from typing import Dict
from controller.c_convert_text import c_dec_hex
app = FastAPI()

@app.on_event("startup")
async def startup():
    print("API서버 구동 시작")

@app.on_event("shutdown")
async def shutdown():
    print("API서버 구동 종료")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/upload/dec_hex/{api_type}")
async def convert_decimal_to_hex(request: Request, api_type: str, data: dict):
    data = (await request.json())
    output_data = dict()

    if api_type == 'dec_to_hex':
        output_data = c_dec_hex.convert_decimal_to_hex(data['data'])
    elif api_type == 'hex_to_dec':
        output_data = c_dec_hex.convert_hex_to_decimal(data['data'])

    return output_data
