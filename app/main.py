import uvicorn
from fastapi import FastAPI, Request, Depends, Form, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles


templates = Jinja2Templates(directory="templates")
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/product", status_code=status.HTTP_302_FOUND)
def create_product(request: Request, product_id: str = Form(...)):
    return RedirectResponse(
        url=f"/product/{product_id}", status_code=status.HTTP_302_FOUND
    )


@app.get("/product/{id}")
def get_product(id: int):
    return f"show product with id {id}"


@app.put("/product/{id}")
def update_product(id: int):
    return "update product with id {id}"


@app.delete("/product/{id}")
def delete_product(id: int):
    return "delete product with id {id}"


@app.get("/products")
def show_all_products():
    return "show all products"


if __name__ == "__main__":
    uvicorn.run(app)
