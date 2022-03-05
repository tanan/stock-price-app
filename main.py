import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_hello():
    return {'message': 'Hello from FastAPI Server!', "id": "1"}

@app.get('/stock-price/{id}')
def get_stock_price(id: int):
    price = 0
    if id == 1:
        price = 100000
    elif id == 2:
        price = 200000
    else:
        print('no match id: %d' % id)

    return {'price': price}

if __name__ == '__main__':
    uvicorn.run(app)