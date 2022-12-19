from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client as client

from typing import Union

from fastapi import FastAPI

#c174e996d56b836296720aedb0bb67081ce20cc3
url = 'https://caffeine-test-6322868.dev.odoo.com'
db = 'caffeine-test-6322868'
username = 'ali'
password = '123'

common = client.ServerProxy('{}/xmlrpc/2/common'.format(url))

models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))
m = common.version()

uid = common.authenticate(db, username, password, {})

print(m)
print(uid)
app = FastAPI()

@app.get("/")
async def index():
    return "hello,world"

@app.get("/brands")
async def read_item(skip: int = 0, limit: int = 10):
    brands = models.execute_kw(db, uid, password, 'product.brand.ept', 'search_read', [[['id', '!=', 0]]],
                               {'fields': ['id','name'], 'offset': skip, 'limit': limit})
    for element in brands:
        print(element)
    return brands

@app.get("/products")
async def read_item(skip: int = 0, limit: int = 10):
    products = models.execute_kw(db, uid, password, 'product.product', 'search_read', [[['id', '!=', 0]]],
                            {'fields': ['name'], 'offset': skip, 'limit': limit})
    return products

@app.get("/products")
async def read_item(skip: int = 0, limit: int = 10):
    products = models.execute_kw(db, uid, password, 'product.product', 'search_read', [[['id', '!=', 0]]],
                            {'fields': ['name'], 'offset': skip, 'limit': limit})
    return products
@app.get("/category")
async def read_item(skip: int = 0, limit: int = 10):
    categories =models.execute_kw(db, uid, password, 'product.category', 'search_read', [[['id', '!=', 0]]], {'fields': ['name'],'offset': skip, 'limit': limit})
    return categories
@app.get("/sections")
async def read_item(skip: int = 0, limit: int = 10):
    sections = models.execute_kw(db, uid, password, 'product.category', 'search_read', [[['parent_id', '=', False]]], {'fields': ['name'],'offset': skip, 'limit': limit})
    return sections