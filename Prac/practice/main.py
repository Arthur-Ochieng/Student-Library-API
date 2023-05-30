from fastapi import FastAPI, Query, Body
from pydantic import BaseModel
from typing import Annotated

class item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app =  FastAPI()

@app.post("/items/")
async def create_item(item: item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item

# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: int,
#     item: Annotated[
#         item,
#         Body(
#             example={
#                 "name": "Foo",
#                 "description": "A very nice Item",
#                 "price": 35.4,
#                 "tax": 3.2,
#             },
#         ),
#     ],
# ):
#     results = {"item_id": item_id, "item": item}
#     return results


@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items
