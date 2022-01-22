from typing import Optional
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from typing import List
from typing import Dict
from controller.c_convert_text import c_dec_hex, c_radix

app = FastAPI(
    title = "Convertit",
    version = "0.0.1",
    docs_url='/api/docs',
    redoc_url='/api/redoc',
    openapi_url='/api/openapi.json'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    print("API서버 구동 시작")

@app.on_event("shutdown")
async def shutdown():
    print("API서버 구동 종료")

@app.post("/upload/dec_hex/{api_type}", deprecated=True)
async def convert_decimal_to_hex(request: Request, api_type: str, data: dict):
    data = await request.json()
    output_data = dict()
    if api_type == 'dec_to_hex':
        output_data = c_dec_hex.convert_decimal_to_hex(data['data'])
    elif api_type == 'hex_to_dec':
        output_data = c_dec_hex.convert_hex_to_decimal(data['data'])

    return output_data
    

@app.post("/api/upload/radix/{from_type}")
async def radix(request: Request, from_type: str, data: dict):
    data = await request.json()
    output_data = dict()

    if from_type == "dec":
        output_data = c_radix.convert_from_dec(data['to_type'], data['data'])
    elif from_type == "bin":
        output_data = c_radix.convert_from_bin(data['to_type'], data['data'])
    elif from_type == "oct":
        output_data = c_radix.convert_from_oct(data['to_type'], data['data'])
    elif from_type == "hex":
        output_data = c_radix.convert_from_hex(data['to_type'], data['data'])
    
    return output_data

    
