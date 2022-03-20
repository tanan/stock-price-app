import string
import uvicorn
from fastapi import FastAPI
from yahoo_finance_api import YahooFinanceAPI

app = FastAPI()
api = YahooFinanceAPI()

@app.get('/')
def get_hello():
  return {'message': 'Hello from FastAPI Server!', "id": "1"}

# TODO: query paramsを追加
@app.get('/stock-price/{id}')
def get_stock_price(id):
  results = api.get_historical(id, "DAY", 7, "DAY", 1)
  return results

if __name__ == '__main__':
  uvicorn.run(app)