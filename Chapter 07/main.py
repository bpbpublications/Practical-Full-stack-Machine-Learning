from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float
    in_stock: Optional[bool] = None

class request_body(BaseModel):
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float


@app.get("/")
def home_page():
    return {"Hello": "World Alok"}

@app.get("/product/{product_id}")
def read_product(product_id: int, q: Optional[str] = None):
    return {"product_id": product_id, "q": q}

@app.put("/product/{product_id}")
def update_product(product_id: int, product: Product):
    return {"product_name": product.name, "product_id": product_id}

