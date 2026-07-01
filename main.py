from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "code": "SP001", "name": "Keyboard", "price": 500000, "is_active": True},
    {"id": 2, "code": "SP002", "name": "Mouse", "price": 300000, "is_active": True},
    {"id": 3, "code": "SP003", "name": "Monitor", "price": 2500000, "is_active": False},
]


@app.get("/products")
def get():
    return products


@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    is_found_delete = False
    for index, p in enumerate(products):
        if p["id"] == product_id:
            if not p["is_active"]:
                is_found_delete = False
                return {"status": "success", "message": "Product already inactive"}

            products[index]["is_active"] = False
            is_found_delete = True
            return {
                "status": "success",
                "message": "Ngừng kinh doanh thành công",
            }

    if not is_found_delete:
        return {"status": "success", "message": "Product not found"}
