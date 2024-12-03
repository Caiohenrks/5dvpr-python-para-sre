from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class MathOperation(BaseModel):
    var1: float
    var2: float

@app.get("/")
def hello():
    return {"message": "Hello World", "timestamp": str(datetime.now())}

@app.post("/api/soma")
def api_soma(data: MathOperation):
    try:
        result = data.var1 + data.var2
        return {"soma": result}
    except ValueError:
        raise HTTPException(status_code=400, detail="Os valores devem ser números válidos")

@app.post("/api/subtracao")
def api_sub(data: MathOperation):
    try:
        result = data.var1 - data.var2
        return {"subtração": result}
    except ValueError:
        raise HTTPException(status_code=400, detail="Os valores devem ser números válidos")

@app.post("/api/divisao")
def api_div(data: MathOperation):
    try:
        if data.var2 == 0:
            raise HTTPException(status_code=400, detail="Não é possível dividir por zero")
        result = data.var1 / data.var2
        return {"divisão": result}
    except ValueError:
        raise HTTPException(status_code=400, detail="Os valores devem ser números válidos")

@app.post("/api/multiplicacao")
def api_mult(data: MathOperation):
    try:
        result = data.var1 * data.var2
        return {"multiplicação": result}
    except ValueError:
        raise HTTPException(status_code=400, detail="Os valores devem ser números válidos")
