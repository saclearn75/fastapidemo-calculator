
from fastapi import FastAPI, Query
app = FastAPI()

@app.get('/')
@app.get('/about')
def home():
    return({'msg':'This is the home page'})

@app.get('/add')
def add_nums(a:int, b: int):
    return ({'add':f'Sum is {a+b}'})

@app.get('/subtract')
def sub_nums(a:int, b: int):
    return ({'subtract':f'Difference is {a-b}'})

@app.get('/multiply')
def mult_nums(a:int, b: int):
    return ({'multiply':f'Product is {a*b}'})

@app.get('/divide')
def div_nums(a:int, b: int = Query(title='MyDivider', gt=0)):
    return ({'divide':f'Division is {a/b}'})
