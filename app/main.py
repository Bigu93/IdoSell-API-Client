import uvicorn
import os
from idosellapi.product_data import ProductData
from fastapi import FastAPI, Request, Depends, Form, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

static_directory = os.path.join(os.path.dirname(__file__), "static")
templates_directory = os.path.join(os.path.dirname(__file__), "templates")

templates = Jinja2Templates(templates_directory)

app = FastAPI()
app.mount("/static", StaticFiles(directory=static_directory), name="static")

product_data = ProductData()


@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/get-product")
def get_product(request: Request, product_id: list[int] = Form(...)):
    product_info = product_data.get_product_info(product_id)
    return templates.TemplateResponse(
        "index.html", {"request": request, "product": product_info}
    )


@app.put("/update-product/{id}")
def update_product(id: int):
    return "update product with id {id}"


@app.delete("/delete-product/{id}")
def delete_product(id: int):
    return "delete product with id {id}"


@app.get("/products")
def show_all_products():
    return "show all products"
