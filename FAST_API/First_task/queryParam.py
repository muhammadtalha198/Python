#When you declare other function parameters that are not part
# of the path parameters, they are automatically interpreted as "query" parameters.


from fastapi import FastAPI

app = FastAPI()



@app.get("/item/")
async def read_item(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

# http://127.0.0.1:8000/items/
# http://127.0.0.1:8000/items/?skip=0&limit=10
# http://127.0.0.1:8000/items/?skip=20



# The same way, you can declare optional query parameters,
#  by setting their default to None:

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

# http://127.0.0.1:8000/items/123
# http://127.0.0.1:8000/items/123?q=test



@app.get("/items1/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# http://127.0.0.1:8000/items1/foo?short=1
# http://127.0.0.1:8000/items1/foo?short=true
# http://127.0.0.1:8000/items1/foo?short=True
# http://127.0.0.1:8000/items1/foo?short=on
# http://127.0.0.1:8000/items1/foo?short=yes



# Multiple path and query parameters

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
   
    item = {"item_id": item_id, "owner_id": user_id}
   
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# http://127.0.0.1:8000/users/1/items/foo?q=test
#http://127.0.0.1:8000/users/1/items/foo?short=true


# Required query parameters

@app.get("/items2/{item_id}")
async def read_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

# http://127.0.0.1:8000/items2/foo?needy=sooooneedy

# Query parameter types