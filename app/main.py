import os
from idosellapi.product_data import ProductData
from idosellapi.exceptions.api_exceptions import ProductInfoError, NoProductFoundError
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
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
    try:
        product_info = product_data.get_product_info(product_id)
        return templates.TemplateResponse(
            "index.html", {"request": request, "product": product_info, "error": None}
        )
    except (ProductInfoError, NoProductFoundError) as e:
        return templates.TemplateResponse(
            "index.html", {"request": request, "product": None, "error": str(e)}
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


@app.exception_handler(ProductInfoError)
def product_info_error_handler(request: Request, exc: ProductInfoError):
    return JSONResponse(status_code=400, content={"message": str(exc)})


@app.exception_handler(NoProductFoundError)
def no_product_found_error_handler(request: Request, exc: NoProductFoundError):
    return JSONResponse(status_code=404, content={"message": str(exc)})
